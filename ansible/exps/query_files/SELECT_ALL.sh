#!/bin/bash
# SELECT_ALL.sh

numobjs=$1
poolname=$2
matchfile=$3
timefile=$4

echo "--------------------------------"
echo "numobjs   = $numobjs"
echo "poolname  = $poolname"
echo "matchfile = $matchfile"
echo "timefile  = $timefile"

{ time -p bin/run-query --num-objs $numobjs --pool $poolname --wthreads 1 --qdepth 10 --query flatbuf --select "*"  > $matchfile ; } 2>> $timefile ;
