#!/bin/python

import os
import subprocess
import sys

this_user               = sys.argv[1]
data_node_addr          = sys.argv[2]
data_path               = sys.argv[3]
data_dir                = sys.argv[4]
format_secondary_device = sys.argv[5]
pool_name               = sys.argv[6]

# get file names from remote storage
remote_files_str = subprocess.check_output(["bash", \
                                            "rsync_command.sh", \
                                            "kat", \
                                            data_node_addr, \
                                            "/mnt/sda4/arity3datasets/flatflex/fbxrows-arity3-1mb-100objs/"])
remote_files_str = remote_files_str.rstrip() ;
remote_files_list = [ f1.split()[-1] for f1 in [ f for f in remote_files_str.split("\n") ] ]
#print remote_files_list

for f in remote_files_list :
  # scp one object file at a time into secondary storage on local
  cmd0 = "su - " + this_user + " -c 'scp -o StrictHostKeyChecking=no -r " + \
             this_user + "@" + data_node_addr + ":" + data_path + "/" + \
             data_dir +" /mnt/" + format_secondary_device + "/'"

  # load object file into ceph
  cmd1 = "yes | PATH=$PATH:bin ../src/progly/rados-store-glob.sh " +  \
         pool_name + " /mnt/" + format_secondary_device + "/" +  \
         data_dir + "/" + f

  # delete the object file from local
  cmd2 = "rm -rf /mnt/" + format_secondary_device + "/" + \
         data_dir + "/" + f


  print cmd0
  print cmd1
  print cmd2
  os.system( cmd0 )
  os.system( cmd1 )
  os.system( cmd2 )
