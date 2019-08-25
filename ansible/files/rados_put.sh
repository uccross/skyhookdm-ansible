#!/bin/bash
pool_name=$1
format_secondary_device=$2
filename=$3
objnum=$4
sudo bash rados-store-glob.sh $pool_name /mnt/$format_secondary_device/$filename $objnum ;
