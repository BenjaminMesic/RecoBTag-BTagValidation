#!/usr/bin/env python

import sys, os, subprocess, string, re
from optparse import OptionParser


# usage description
usage = """Usage: ./combineOutput.py [options]\n
Example: ./combineOutput.py -w LXBatch_Jobs\n
For more help: ./combineOutput.py  --help
"""

def main():

  # input parameters
  parser = OptionParser(usage=usage)

  parser.add_option("-w", "--main_workdir", dest="main_workdir",
                    help="Main working directory",
                    metavar="MAIN_WORKDIR")

  parser.add_option("-o", "--output_dir", dest="output_dir",
                    help="Output directory (This parameter is optional)",
                    metavar="OUTPUT_DIR")

  parser.add_option("-e", "--is_dir_at_eos", dest="is_dir_at_eos", action='store', default='false', help="Set to 'true' if files are at EOS")

  parser.add_option("-E", "--eospath", dest="eospath", action='store', help="path at EOS")

  (options, args) = parser.parse_args()

  # make sure all necessary input parameters are provided
  if not options.main_workdir:
    print usage
    sys.exit()

  main_workdir = options.main_workdir

  # redefine main_workdir as an absolute path (if not defined in such form already)
  if not re.search("^/", main_workdir):
    main_workdir = os.path.join(os.getcwd(),main_workdir)


  # if files are at eos
  if options.is_dir_at_eos=='true':
  	print 'Combining files at eos.',main_workdir
  	os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select -b fuse mount $HOME/eos')
  	main_workdir = os.path.join(options.eospath,options.main_workdir)
  	print 'main_workdir : ',main_workdir


  output_dir = main_workdir
  if options.output_dir:
    output_dir = options.output_dir
    # redefine output_dir as an absolute path (if not defined in such form already)
    if not re.search("^/", output_dir):
      output_dir = os.path.join(os.getcwd(),output_dir)

  # open and read the dataset_list file
  if options.is_dir_at_eos=='true':
  	dataset_list_file = open(os.path.join(os.path.join(os.getcwd(),options.main_workdir),'datasetList.txt'),'r')
	os.system('mkdir -v '+options.output_dir)
  else:
  	dataset_list_file = open(os.path.join(main_workdir,'datasetList.txt'),'r')
  dataset_list_lines = dataset_list_file.readlines()

  # loop over datasets
  for line in dataset_list_lines:

    line_elements = line.split()
    if (len(line_elements)==0 or line_elements[0][0]=='#'): continue

    workdir = line_elements[0].lstrip('/').replace('/','__')

    print '------------------------------------------------------------------------------------'
    print line_elements[0]

    # final output
    output_root_file = os.path.join(output_dir,workdir + '.root')

    crab_output_dir = os.path.join(main_workdir,workdir,'output')

    # combine .root files
    print 'Combining .root files...'
    cmd = 'hadd -f ' + output_root_file + ' ' + os.path.join(crab_output_dir,'*.root')
    proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
    output = proc.communicate()[0]
    if proc.returncode != 0:
      print output
      sys.exit(1)

    # final output for this dataset
    print ''
    print "Final .root file: " + output_root_file

  if options.is_dir_at_eos=='true':os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select -b fuse umount $HOME/eos')


if __name__ == "__main__":
  main()