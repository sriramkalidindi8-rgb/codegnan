Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> [a:]
SyntaxError: invalid syntax
>>> b=a[:6]
>>> b
[9, 1, 5, 2, 8, 4]
>>> c=a[6:]
>>> c
[6, 3, 7, 0]
>>> d=b.sort(c)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d=b.sort(c)
TypeError: sort() takes no positional arguments
>>> b.sort()
>>> b
[1, 2, 4, 5, 8, 9]
>>> c.sort()
>>> c
[0, 3, 6, 7]
>>> b.reverse()
>>> b
[9, 8, 5, 4, 2, 1]
>>> c.reverse()
>>> c
[7, 6, 3, 0]
>>> print(b,c)
[9, 8, 5, 4, 2, 1] [7, 6, 3, 0]
>>> c.append(b)
>>> c
[7, 6, 3, 0, [9, 8, 5, 4, 2, 1]]
>>> 