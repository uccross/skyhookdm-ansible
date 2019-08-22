#!/bin/bash
# AGG_QUERY.sh

numobjs=$1
poolname=$2
matchfile=$3
timefile=$4
select_preds=$5
table_name=$6
data_schema=$7

echo "--------------------------------"
echo "numobjs      = $numobjs"
echo "poolname     = $poolname"
echo "matchfile    = $matchfile"
echo "timefile     = $timefile"
echo "select_preds = $select_preds"
echo "project_cols = $project_cols"
echo "data_schema  = $data_schema"

{ time bin/run-query --num-objs $numobjs --pool $poolname --wthreads 1 --qdepth 10 --query flatbuf --select "$select_preds" --table-name "$table_name" --data-schema "$data_schema" > $matchfile ; } 2>> $timefile ;
