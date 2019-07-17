# validate popper test results

import sys

def do_compare( filename0, filename1 ) :
  file0 = open( filename0, "r" )
  for line0 in file0 :
    line0 = line0.rstrip()
    file1 = open( filename1, "r" )
    line_exists = False
    for line1 in file1 :
      line1 = line1.rstrip()
      if line0 == line1 :
        line_exists = True
    file1.close()
    if not line_exists :
      sys.exit( "do_compare: '" + filename0 + "' line '" + line0 + "' does not exist in '" + filename1 + "'" )
  file0.close()

def compare_res( out_filename, res_filename ) :

  # make sure all lines in the out file are in the expected file
  do_compare( out_filename, res_filename )

  # make sure all lines in the expected file are in the out file
  do_compare( res_filename, out_filename )

def main( line_args ) :
  out_select_all   = line_args[1]
  out_project_cols = line_args[2]
  out_like         = line_args[3]

  compare_res( out_select_all, "res_select_all.txt" )
  #compare_res( out_project_cols )
  #compare_res( out_like )

if __name__ == "__main__" :
  main( sys.argv )
