import multiprocessing
import os
import sys

#################
#   RADOS PUT   #
#################
def rados_put( poolname, obj_name, data_file_fullpath ) :
  cmd = "rados -p " + poolname + " put " + obj_name + " " + data_file_fullpath
  print cmd
  #os.system( "rados -p " + poolname + " put " + obj_name + " " + data_file_fullpath )

############
#   MAIN   #
############
def main() :

  # inputs
  max_num_objs = int( sys.argv[1] )
  poolname     = sys.argv[2]
  data_file    = os.path.abspath( sys.argv[3] )

  job_args_list = []
  base_name     = "obj."
  for i in range( 0, max_num_objs ) :
    job_args_list.append( ( poolname, base_name+str(i), data_file ) )

  # printing main program process id
  print("ID of main process: {}".format(os.getpid()))
  jobs = []
  if len(job_args_list) < 10 :
    max_k = len(job_args_list)
  else :
    max_k = len(job_args_list)/10
  obj_id = 0
  for k in range( 0, (len(job_args_list)/10) ) :
    for i in range( 0, 10 ) :
      job_args = job_args_list[obj_id]
      print "======================================================"
      print job_args
      print "======================================================"
      j = multiprocessing.Process( target=rados_put, args=job_args )
      jobs.append( j )
      j.start()
      print( "ID of process : {}".format( j.pid ) )
      obj_id += 1

  # wait until processes finish
  for j in jobs :
    j.join()

  # all processes finished
  print("all processes finished execution!")

if __name__ == "__main__" :
  main()
