# validate popper test results

import sys

def compare_res( out_file ) :

  # extract results table
  # make sure headers are identical
  # make sure all rows in the out file are in the expected file
  # make sure all rows in the expected file are in the out file


def main( line_args ) :
  out_select_all   = line_args[1]
  out_project_cols = line_args[2]
  out_like         = line_args[3]

  compare_res( out_select_all )
  compare_res( out_project_cols )
  compare_res( out_like )

if __name__ == "__main__" :
  main( sys.argv )
