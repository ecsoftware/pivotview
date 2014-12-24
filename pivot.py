#!/usr/bin/env python

"""
Pivot program to visualize the data set with different dynamic groups and different output format.

I assumed the input text file contains the data. We need to read the data and group the data by the passed argument by the command line.
Here space is the delimiter and also first line will be the header/keys

Sample Input File(data.txt)
---------------------------
name Gender age Location
User1 M 20  Location1
User2 M 18  Location3
User3 F 45  Location2
User4 F 25  Location2
User4 F 7 Location2

Author: Ponveni Rajendran
Last Modified: 24, Dec 2014.
"""

# Default Python Modules Import
import sys
import os
import argparse

from collections import defaultdict
from pivot_reports import (string_format, html_format,
                           csv_format)

output_formats = ['csv', 'html']


def pivot_output(keys, data, output=None):
  """
	This function returns the Group Data based on the given arguments.
	
        The arguments are keys (Header Data), data (Group Count Data Dict) and Output format.

	Keys may be [Age], [Gender, Location], [Age, Gender, Location], etc
	data: Dict contains tuple as a key and count as a value.
        output may be HTML, CSV. Default format is string.
  """
  # Add the Count in Header
  keys.append("Count")
  
  # Normal String Format
  if not output:
    string_format(keys, data)
  # HTML Format
  elif output.lower() == 'html':
    html_format(keys, data)
  # CSV Format
  elif output.lower() == 'csv':
    csv_format(keys, data)
  # Unsupported Format
  else:
    print 'Unsupported output format.'


def main():
  """
	Main Function group the Count Dict and call the pivot output function with
        the output format type if any.
  """
  # argparser is the python module 
  # which is used to parse the arguments from the command line.
  parser = argparse.ArgumentParser()
  parser.add_argument('-by', action='append', help='Group data by.')
  parser.add_argument('-o', action='append', help='Output data format.')
  args = parser.parse_args()

  # sys.stdin.readlines read the lines from the input file.
  #['name Gender age Location\n', 'User1 M 20  Location1\n', 'User2 M 18  Location3\n', 'User3 F 45  Location2\n', 
  #'User4 F 25  Location2\n', 'User4 F #7 Location2\n', '\n']
  
  data = sys.stdin.readlines() 

  # TODO: uncomment the line if the command line is not working
  #data = open('data.txt').readlines()
  
  grouped_dict = defaultdict(int)

  # Assuming first line will be header, as problem doesnt specifies anything
  # exactly. Separate the values by space.
  keys = [key.strip().lower() for key in data[0].split(' ') if key.strip()]

  # Testing keys to test different groups
  manual_keys = ['Gender', 'Location', 'name'] 

  group_by = args.by if args.by else manual_keys
  try: 
      indices = [keys.index(key.lower()) for key in group_by]
  except:
    print 'Please specify the valid groups. For Example Name, Location, Gender and Age'
    exit()

  # data[1:] exclude the first line, contains the keys/header
  for line in data[1:]:
    try:
      row = [val.rstrip('\n').lower() for val in line.split(' ') if val.strip()]
      grouped_dict[tuple([row[index] for index in indices])] += 1
    except:
      continue

  if args.by:
      if args.o:
        # Check the output format is available or not in 
        # the output formats list
        if agrs.o[0].strip().lower() in output_formats:
          pivot_output(args.by, grouped_dict, args.o[0])
        else:
          print 'Please specify the valid output format.'
      else:
        pivot_output(args.by, grouped_dict)
  else:
    print 'Please specify the required arguments.'
    #exit()

    # TODO: uncomment the line if the command line is not working
    #pivot_output(group_by, grouped_dict)
    #pivot_output(group_by, grouped_dict, 'HTML')
    #pivot_output(group_by, grouped_dict, 'CSV')
    #pivot_output(group_by, grouped_dict, 'XML')

if __name__ == '__main__':
  main()

