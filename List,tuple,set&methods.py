Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list[]
>>> a=[2,3.4,"python",6+9j,True,False]
>>> print(a)
[2, 3.4, 'python', (6+9j), True, False]
>>> type(a)
<class 'list'>
>>> b=23.3
>>> type(b)
<class 'float'>
>>> c=[23.3]
>>> type(c)
<class 'list'>
>>> #append
>>> a=["python","java","c"]
>>> a.append("c++")
>>> a
['python', 'java', 'c', 'c++']
>>> a.append("ai","ml")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ai","ml")
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append(["ai","ml"])
>>> a
['python', 'java', 'c', 'c++', ['ai', 'ml']]
>>> #extend
>>> a=["ds","ai"]
>>> a.extend(["c","c++"])
>>> a
['ds', 'ai', 'c', 'c++']
>>> #insert
>>> a=["python","java","c"]
>>> a.insert(1,"ds")
>>> a
['python', 'ds', 'java', 'c']
>>> #index
>>> a=["hyd","vja","vzg"]
>>> a.index("vja")
1
>>> a.copy()
['hyd', 'vja', 'vzg']
>>> #copy()
>>> b=a.copy()
>>> b
['hyd', 'vja', 'vzg']
>>> #sort()
>>> a=["mango","apple","grapes","banana"]
>>> a.sort()
>>> a
['apple', 'banana', 'grapes', 'mango']
>>> b=[23,43,34,2,5,92,4,6,8,12,44,10,22,0]
>>> b.sort(0
       b
       
SyntaxError: invalid syntax
>>> b.sort()
>>> b
[0, 2, 4, 5, 6, 8, 10, 12, 22, 23, 34, 43, 44, 92]
>>> c=["mango","Apple","Grapes","banana"]
>>> c.sort()
>>> c
['Apple', 'Grapes', 'banana', 'mango']
>>> #reverse()
>>> a=["black","white","red","blue"]
>>> a.reverse()
>>> a
['blue', 'red', 'white', 'black']
>>> b=[1,2,3,4,5,6,7,8,9,0]
>>> b.reverse()
>>> b
[0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> #pop()
>>> a=["java","ds","ai"]
>>> a.pop()
'ai'
>>> a.pop(1)
'ds'
>>> a.pop("java")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.pop("java")
TypeError: 'str' object cannot be interpreted as an integer
>>> #remove
>>> a.remove("java")
>>> a
[]
>>> #clear()
>>> a=["chair","table"]
>>> a.clear()
>>> a
[]
>>> #length()
>>> a["hi","hello"]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a["hi","hello"]
TypeError: list indices must be integers or slices, not tuple
>>> a=["hi","hello"]
>>> len(a)
2
>>> b="hello"
>>> len(b)
5
>>> c=["hello"]
>>> len(c)
1
>>> #count
>>> a.count("hi")
1
>>> #Tuple---------------------
>>> a=[2,3.4,"python",6+9j,True,False]
>>> type(a)
<class 'list'>
>>> b=(2,3.4,"python",6+9j,True,False)
>>> typr(b)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    typr(b)
NameError: name 'typr' is not defined
>>> type(b)
<class 'tuple'>
>>> b.count(6+9j)
1
>>> b.index(True)
4
>>> len(b)
6
>>> #sets{}-----------------
>>> a={2,3.4,"python",6+9j,True,False}
>>> type(a)
<class 'set'>
>>> print(a)
{False, (6+9j), 2, 3.4, True, 'python'}
>>> #methods======================================================================================================================
>>> a={4,5,6,7,8,9}
>>> a.add(10)
>>> a
{4, 5, 6, 7, 8, 9, 10}
>>> a={1,2,3,4,5,6)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> a={1,2,3,4,5,6}
>>> b={5,6,7,8,9,10}
>>> a.issubset(b)
False
>>> b.issubset(a)
False
>>> a={1,2,3,4,5,6,7,8,9}
>>> b={3,4,5,6,7}
>>> a.issubset(b)
False
>>> b.issubset(a)
True
>>> #superset
>>> a={1,2,3,4,5,6,7,8,9}
>>> b={3,4,5,6,7}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> #union
>>> a={10,11,12,13,14,15}
>>> b={14,15,16,17,18,19}
>>> a.union(b)
{10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
>>> #intersection
>>> a={10,11,12,13,14,15}
>>> b={14,15,16,17,18,19}
>>> a.intersection(b)
{14, 15}
>>> #update
>>> a={3,4,5,6,7}
>>> b={6,7,8,9,10}
>>> a.update(b)
>>> a
{3, 4, 5, 6, 7, 8, 9, 10}
>>> b
{6, 7, 8, 9, 10}
>>> b.update(a)
>>> b
{3, 4, 5, 6, 7, 8, 9, 10}
>>> #difference
>>> a={5,6,7,8,9,10,11}
>>> b={9,10,11,12,13,14}
>>> a.difference(b)
{8, 5, 6, 7}
>>> b.difference(a)
{12, 13, 14}
>>> #symmetric_difference
>>> a={3,4,5,6,7,8}
>>> b={5,6,7,8,9,10}
>>> a.symmetric_difference(b)
{3, 4, 9, 10}
>>> #difference_update
>>> a={4,5,6,7,8,9}
>>> b={6,7,8,9,10,11}
>>> a.difference_update(b)
>>> a
{4, 5}
>>> b.difference_update(a)
>>> b
{6, 7, 8, 9, 10, 11}
>>> #intersection_update
>>> a={5,6,7,8,9,10,11}
>>> b={9,10,11,12,13,14}
>>> a.intersection_update(b)
>>> a
{9, 10, 11}
>>> b.intersection_update(a)
>>> b
{9, 10, 11}
>>> #symmetric_difference_update
>>> a={10,20,30,40,50}
>>> b={30,40,50,60,70}
>>> a.symmetric_difference_update(b)
>>> a
{20, 70, 10, 60}
>>> b.symmetric_difference_update(a)
>>> b
{50, 20, 40, 10, 30}
>>> #pop-
>>> a={2,3,4,5,6,7}
>>> a,pop()
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    a,pop()
NameError: name 'pop' is not defined
>>> a.pop()
2
>>> a
{3, 4, 5, 6, 7}
>>> a.remove(5)
>>> a
{3, 4, 6, 7}
>>> a.pop(7)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    a.pop(7)
TypeError: set.pop() takes no arguments (1 given)
>>> a.discard(7)
>>> a
{3, 4, 6}
>>> a={5,6,7,8,9,10}
>>> a.copy()
{5, 6, 7, 8, 9, 10}
>>> a
{5, 6, 7, 8, 9, 10}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(60)
>>> b
{60}
>>> a={4,5,6,7,8}
>>> b={9,10,11,12}
>>> a.isdisjoint(b)
True
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> a.count(4)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    a.count(4)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(7)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    a.index(7)
AttributeError: 'set' object has no attribute 'index'
>>> 