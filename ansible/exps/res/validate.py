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
  out_filename = line_args[1]
  expected_res_filename = line_args[2]

  compare_res( out_filename, expected_res_filename )

if __name__ == "__main__" :
  main( sys.argv )
