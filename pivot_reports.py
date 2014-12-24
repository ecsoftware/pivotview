"""
This Module contains the functions which are used to 
return the different output format such as Normal String,
HTML and CSV format.

Author: Ponveni Rajendran
Last Modified: 24, Dec 2014.

"""


def string_format(keys, data):
  """
	This function returns the Normal String Format, 
        which contains the Keys(Header) Group with Count.

	The output is given below

	********* String Format Output ************
	Location Gender Count
	Location1 M 1
	Location3 M 1
	Location2 F 3
	*******************************************
  """

  print '********* String Format Output ************'
  keys = [key.capitalize() for key in keys]
  print ' '.join(keys)

  for groups, count in data.iteritems():
    groups= [group.capitalize() for group in groups]
    groups.append(str(count))
    print ' '.join(groups)
  print '*******************************************'


def html_format(keys, data):
  """
	This function returns the HTML Format, 
        which contains the Keys(Header) Group with Count.
	
	The output is given below

	********* HTML Format Output **************
	<table>
	<th>
	<td>Location</td>
	<td>Gender</td>
	<td>Count</td>
	</th>
	<tr>
	<td>Location1</td>
	<td>M</td>
	<td>1</td>
	</tr>
	<tr>
	<td>Location3</td>
	<td>M</td>
	<td>1</td>
	</tr>
	<tr>
	<td>Location2</td>
	<td>F</td>
	<td>3</td>
	</tr>
	</table>
	*******************************************
  """
  print '********* HTML Format Output **************'
  print '<table>\n<th>'
  for key in keys:
    print ''.join(['<td>', key.capitalize(), '</td>'])
  print '</th>'

  for groups, count in data.iteritems():
    print '<tr>'
    for group in groups: 
      print ''.join(['<td>',group.capitalize(),'</td>'])
    print ''.join(['<td>',str(count),'</td>\n</tr>'])
  print'</table>'
  print '*******************************************'
  

def csv_format(keys, data):
  """
	This function returns the CSV Format, 
        which contains the Keys(Header) Group with Count.

	The output is given below

	********* CSV Format Output ***************
	Location,Gender,Count
	Location1,M,1
	Location3,M,1
	Location2,F,3
	******************************************

  """
  print '********* CSV Format Output ***************'
  keys = [key.capitalize() for key in keys]
  print ','.join(keys)

  for groups, count in data.iteritems():
    groups = [group.capitalize() for group in groups]
    groups.append(str(count))
    print ','.join(groups)
  
  print '******************************************'


