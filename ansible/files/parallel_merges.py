#!/bin/python
# python parallel_merges.py ${num_merge_objs} ${poolname} ${num_src_objs_per_merge} \"copyfrom\"

import multiprocessing
import os
import sys

def driver(
  poolname,
  start_oid,
  end_oid,
  merge_id,
  write_type ) :

  if merge_type == "copyfrom" :
    cmd = "sudo bin/run-copyfrom-merge" + \
          " --pool " + poolname + \
          " --start-oid " + start_oid + \
          " --end-oid " + end_oid + \
          " --merge-id " + merge_id
  elif merge_type == "client" :
    cmd = "sudo bin/run-client-merge" + \
          " --pool " + poolname + \
          " --start-oid " + start_oid + \
          " --end-oid " + end_oid + \
          " --merge-id " + merge_id
  else :
    print "unrecognized merge_type '" + merge_type + "'"
  print cmd
  os.system( cmd )

num_merge_objs         = int( sys.argv[1] )
poolname               = sys.argv[2]
num_src_objs_per_merge = int( sys.argv[3] )
merge_type             = sys.argv[4]

print "num_merge_objs         = " + str( num_merge_objs )
print "poolname               = " + poolname
print "num_src_objs_per_merge = " + str( num_src_objs_per_merge )
print "merge_type             = " + merge_type

# printing main program process id
print("ID of main process: {}".format(os.getpid()))

jobs = []
start_oid = 0
end_oid   = start_oid+num_src_objs_per_merge-1
for i in range( 0, num_merge_objs ) :
  job_args = ( poolname, str( start_oid ), str( end_oid ), str( i ), merge_type )
  print "======================================================"
  print job_args
  print "======================================================"
  j = multiprocessing.Process( target=driver, args=job_args )
  jobs.append( j )
  j.start()
  print( "ID of process : {}".format( j.pid ) )
  start_oid = end_oid+1
  end_oid   = start_oid+num_src_objs_per_merge-1

# wait until processes finish
for j in jobs :
  j.join()

# all processes finished
print("all processes finished execution!")
