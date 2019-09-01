#!/bin/bash

set -ex

result_dir_path=$1
pool_name=$2
tset_type=$3
obj_name=$4
optype=$5

bin/run-papertests {{ result_dir_path }} {{ pool_name }} {{ test_type }} {{ obj_name }} {{ optype }} > res_$obj_name_match.txt ;
