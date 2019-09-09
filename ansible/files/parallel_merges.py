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

  DATA_SCHEMA_NCOLS100 = "0 8 1 0 ATT0; 1 8 0 0 ATT1; 2 8 0 0 ATT2; 3 8 0 0 ATT3; 4 8 0 0 ATT4; 5 8 0 0 ATT5; 6 8 0 0 ATT6; 7 8 0 0 ATT7; 8 8 0 0 ATT8; 9 8 0 0 ATT9; 10 8 0 0 ATT10; 11 8 0 0 ATT11; 12 8 0 0 ATT12; 13 8 0 0 ATT13; 14 8 0 0 ATT14; 15 8 0 0 ATT15; 16 8 0 0 ATT16; 17 8 0 0 ATT17; 18 8 0 0 ATT18; 19 8 0 0 ATT19; 20 8 0 0 ATT20; 21 8 0 0 ATT21; 22 8 0 0 ATT22; 23 8 0 0 ATT23; 24 8 0 0 ATT24; 25 8 0 0 ATT25; 26 8 0 0 ATT26; 27 8 0 0 ATT27; 28 8 0 0 ATT28; 29 8 0 0 ATT29; 30 8 0 0 ATT30; 31 8 0 0 ATT31; 32 8 0 0 ATT32; 33 8 0 0 ATT33; 34 8 0 0 ATT34; 35 8 0 0 ATT35; 36 8 0 0 ATT36; 37 8 0 0 ATT37; 38 8 0 0 ATT38; 39 8 0 0 ATT39; 40 8 0 0 ATT40; 41 8 0 0 ATT41; 42 8 0 0 ATT42; 43 8 0 0 ATT43; 44 8 0 0 ATT44; 45 8 0 0 ATT45; 46 8 0 0 ATT46; 47 8 0 0 ATT47; 48 8 0 0 ATT48; 49 8 0 0 ATT49; 50 8 0 0 ATT50; 51 8 0 0 ATT51; 52 8 0 0 ATT52; 53 8 0 0 ATT53; 54 8 0 0 ATT54; 55 8 0 0 ATT55; 56 8 0 0 ATT56; 57 8 0 0 ATT57; 58 8 0 0 ATT58; 59 8 0 0 ATT59; 60 8 0 0 ATT60; 61 8 0 0 ATT61; 62 8 0 0 ATT62; 63 8 0 0 ATT63; 64 8 0 0 ATT64; 65 8 0 0 ATT65; 66 8 0 0 ATT66; 67 8 0 0 ATT67; 68 8 0 0 ATT68; 69 8 0 0 ATT69; 70 8 0 0 ATT70; 71 8 0 0 ATT71; 72 8 0 0 ATT72; 73 8 0 0 ATT73; 74 8 0 0 ATT74; 75 8 0 0 ATT75; 76 8 0 0 ATT76; 77 8 0 0 ATT77; 78 8 0 0 ATT78; 79 8 0 0 ATT79; 80 8 1 0 ATT80; 81 8 0 0 ATT81; 82 8 0 0 ATT82; 83 8 0 0 ATT83; 84 8 0 0 ATT84; 85 8 0 0 ATT85; 86 8 0 0 ATT86; 87 8 0 0 ATT87; 88 8 0 0 ATT88; 89 8 0 0 ATT89; 90 8 0 0 ATT90; 91 8 0 0 ATT91; 92 8 0 0 ATT92; 93 8 0 0 ATT93; 94 8 0 0 ATT94; 95 8 0 0 ATT95; 96 8 0 0 ATT96; 97 8 0 0 ATT97; 98 8 0 0 ATT98; 99 8 0 0 ATT99"
  PROJECT_COLS_NCOLS100 = "att0"

  if merge_type == "copyfrom" :
    cmd = "sudo bin/run-copyfrom-merge" + \
          " --pool " + poolname + \
          " --start-oid " + start_oid + \
          " --end-oid " + end_oid + \
          " --merge-id " + merge_id + \
          " --debug false"
  elif merge_type == "client" :
    cmd = "sudo bin/run-client-merge" + \
          " --pool " + poolname + \
          " --start-oid " + start_oid + \
          " --end-oid " + end_oid + \
          " --merge-id " + merge_id + \
          " --project-cols " + PROJECT_COLS_NCOLS100 + \
          " --data-schema \"" + DATA_SCHEMA_NCOLS100 + "\"" + \
          " --debug false"
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
