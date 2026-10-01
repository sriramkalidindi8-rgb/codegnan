Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=["codegnan","python"]
>>> b=str(a)
>>> b
"['codegnan', 'python']"
>>> b.upper()
"['CODEGNAN', 'PYTHON']"
>>> a=[2,5,7,9,10,15]
>>> a.insert(3,8)
>>> a
[2, 5, 7, 8, 9, 10, 15]
>>> a=[10,20,30,40]
>>> a.append(50)
>>> a
[10, 20, 30, 40, 50]
>>> a=(10,20,30,40)
>>> b=list(a)
>>> b
[10, 20, 30, 40]
>>> b.append(50)
>>> b
[10, 20, 30, 40, 50]
>>> c=tuple(b)
>>> c
(10, 20, 30, 40, 50)
>>> #-------------------
>>> a=[2,3,4,5,6]
>>> a.extend("code")
>>> a
[2, 3, 4, 5, 6, 'c', 'o', 'd', 'e']
>>> #swapping of two variables
>>> a=10
>>> b=20
>>> #a->20,b->10