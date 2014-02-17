pivotview
=========

We are attempting to visualize sample in Pivot with different dynamic groups

Sample Input file (data.txt)

| name   | Gender | Age | Location |
| ------ |:------:| --- | -------  |
| User1  | M      | 20  | Location1|
| User2  | M      | 18  | Location3|
| User3  | F      | 45  | Location2|
| User4  | F      | 25  | Location2|
| User4  | F      | 7   | Location2|
 
Design sample program "pivot" using python or golang

Group data based on Age

```
$ cat data.txt|piviot -by Age
```

| Gender | Count |
| ------ | ----- |
| M      |  2    |
| F      |  3    |


Group data based on Age,Location

```
$ cat data.txt|piviot -by Gender -by Location
```

| Gender |Location   | Count |
| ------ |---------- | ----- |
| M      | Location1 |  1    |     
| F      | Location2 |  3    |     
| M      | Location3 |  1    |     

Support Output format csv,html

```
$ cat data.txt|piviot -by Gender -by Location -o html
```

Output

```
<table>
<tr>
  <td>Gender</td>
  <td>Location</td>
  <td>Count</td>
</tr>
<td>
<td>M</td>
.....
.....
..
</td>
</table>
```

```
$ cat data.txt|piviot -by Gender -by Location -o csv
```

Output

```
Gender,Location,Count
M,Location1,1
F,Location2,3
M,Location3,1

```

Guidelines
==========

* Source code for the problem solution accept through Pull request to Sprint0 branch only
* Developers can take their own assumptions to solve the problem
* Take simple,smart(or dirty) approach to solve the problem with acceptable effort.
* No need of statistic frameworks like numpy,R and custom bash scripts;
* Source code is owned by developer and willing to share ecsoftware employee and it should not conflict with any commerical products or any associted licenses.

