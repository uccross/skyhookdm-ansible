import multiprocessing
import os
import sys

#################
#   RADOS PUT   #
#################
def rados_put( poolname, obj_name, data_file_fullpath, actually_do_it ) :

  if os.path.isfile( data_file_fullpath ) :
    cmd = "rados -p " + poolname + " put " + obj_name + " " + data_file_fullpath
    print cmd
    if actually_do_it :
      os.system( "rados -p " + poolname + " put " + obj_name + " " + data_file_fullpath )
  else :
    print "could not find file '" + data_file_fullpath + "'"
    sys.exit(0)

############
#   MAIN   #
############
def main() :

  # inputs
  num_objs       = int( sys.argv[1] )
  poolname       = sys.argv[2]
  data_file      = os.path.abspath( sys.argv[3] )
  actually_do_it = sys.argv[4]
  group_id       = int( sys.argv[5] )

  if actually_do_it == "True" :
    actually_do_it = True
  else :
    actually_do_it = False

  start_id = group_id*num_objs
  max_num_objs = start_id + num_objs

  job_args_list = []
  base_name     = "obj."
  for i in range( 0, num_objs ) :
    job_args_list.append( ( poolname, base_name+str(start_id+i), data_file, actually_do_it ) )

  # printing main program process id
  print("ID of main process: {}".format(os.getpid()))
  jobs = []
  if len(job_args_list) < 10 :
    max_k = len(job_args_list)
    max_concurrent = len(job_args_list)
  else :
    max_k = len(job_args_list)/10
    max_concurrent = 10
  obj_count = 0
  for k in range( 0, max_k ) :
    for i in range( 0, max_concurrent ) :
      job_args = job_args_list[obj_count]
      print "======================================================"
      print job_args
      print "======================================================"
      j = multiprocessing.Process( target=rados_put, args=job_args )
      jobs.append( j )
      j.start()
      print( "ID of process : {}".format( j.pid ) )
      obj_count += 1

  # wait until processes finish
  for j in jobs :
    j.join()

  # all processes finished
  print("all processes finished execution!")

if __name__ == "__main__" :
  main()
