#!/bin/bash
# PRED_QUERY.sh

numobjs=$1
poolname=$2
matchfile=$3
timefile=$4
select_preds=$5
project_cols=$6
data_schema=$7
use_cls=$8

echo "--------------------------------" ;
echo "numobjs      = $numobjs" ;
echo "poolname     = $poolname" ;
echo "matchfile    = $matchfile" ;
echo "timefile     = $timefile" ;
echo "select_preds = $select_preds" ;
echo "project_cols = $project_cols" ;
echo "data_schema  = $data_schema" ;
echo "use_cls      = $use_cls" ;

if [ "$use_cls" = True ]
then
  echo "using cls." ;
  echo "{ time bin/run-query --num-objs $numobjs --pool $poolname --wthreads 1 --qdepth 10 --query flatbuf --select "$select_preds" --project-cols $project_cols --data-schema \"$data_schema\" --use-cls > $matchfile ; }" >> $timefile ;
  { time bin/run-query --num-objs $numobjs --pool $poolname --wthreads 1 --qdepth 10 --query flatbuf --select "$select_preds" --project-cols $project_cols --data-schema "$data_schema" --use-cls > $matchfile ; } 2>> $timefile ;
else
  echo "{ time bin/run-query --num-objs $numobjs --pool $poolname --wthreads 1 --qdepth 10 --query flatbuf --select "$select_preds" --project-cols $project_cols --data-schema \"$data_schema\" > $matchfile ; }" >> $timefile ;
  echo "not using cls." ;
  { time bin/run-query --num-objs $numobjs --pool $poolname --wthreads 1 --qdepth 10 --query flatbuf --select "$select_preds" --project-cols $project_cols --data-schema "$data_schema" > $matchfile ; } 2>> $timefile ;
fi