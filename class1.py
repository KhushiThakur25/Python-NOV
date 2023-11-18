Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 1
type(x)
<class 'int'>
x = "string"
type(x)
<class 'str'>
x = 1
x + 1
2
x
1
x = x+1
x
2
x = "string"
x[0]
's'
x[3]
'i'
del x[3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    del x[3]
TypeError: 'str' object doesn't support item deletion
x[0] = l
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x[0] = l
NameError: name 'l' is not defined
>>> x[0]="l"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x[0]="l"
TypeError: 'str' object does not support item assignment
>>> tup = (1,2,3,4,5,6)
>>> del tup[1]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    del tup[1]
TypeError: 'tuple' object doesn't support item deletion
>>> tup[0] = 6
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tup[0] = 6
TypeError: 'tuple' object does not support item assignment
>>> lists = [2,3,5,6,7]
>>> lists[0] = 5
>>> lists
[5, 3, 5, 6, 7]
>>> print(lists)
[5, 3, 5, 6, 7]
>>> print("This is python")
This is python
>>> print("kjsdhs")
kjsdhs
