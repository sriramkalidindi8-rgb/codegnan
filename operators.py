Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #arthematic
>>> a=6
>>> b=7
>>> print(a+b)
13
>>> print(a-b)
-1
>>> print(a//b)
0
>>> print(a/b)
0.8571428571428571
>>> print(a*b)
42
>>> print(a**b)
279936
>>> print(a%b)
6
>>> 
KeyboardInterrupt
>>> #assigment
>>> a=8
>>> b=3
>>> a+=b
>>> a
11
>>> a-=b
>>> a
8
>>> a*=b
>>> a
24
>>> a//=b
>>> a
8
>>> a/=b
>>> a
2.6666666666666665
>>> a**=b
>>> a
18.96296296296296
>>> a%=b
>>> a
0.9629629629629584
>>> 
>>> b+=a
>>> b
3.9629629629629584
>>> b-=a
>>> b
3.0
>>> b*=a
>>> b
2.888888888888875
>>> b//=a
>>> b
3.0
>>> b/=a
>>> b
3.11538461538463
>>> b**=a
>>> a
0.9629629629629584
>>> b
2.9869878831603494
>>> b%=a
>>> b
0.09809899427147428
>>> #comparision
>>> a=6
>>> b=9
>>> a>b
False
>>> a<b
True
>>> a>=b
False
>>> a<=b
True
>>> a!=b
True
>>> a==b
False
>>> #logical
>>> a=10
>>> b=20
>>> a<b and b>a
True
>>> a<=b and b>=a
True
>>> a!=b and a==b
False
>>> a<b or b>a
True
>>> a<=b or b>=a
True
>>> a!=b or a==b
True
>>> not True
False
>>> not False
True
>>> #identify
>>> a=3
>>> type(a)is int
True
>>> type(a) is not int
False
>>> type(a0 is float
     type(a) is float
     
SyntaxError: invalid syntax
>>> type(a) is not float
True
>>> a=6.94
>>> type(a) is float
True
>>> type(a) is int
False
>>> type(a) is str
False
>>> type(a) is complex
False
>>> type(a) is bool
False
>>> #membership
>>> a=1,2,3,4,5,6,7,8,9,10
>>> 7 in a
True
>>> 34 not in a
True
>>> 357 in a
False
>>> #bitwise
>>> a=3
>>> b=6
>>> bin(a)
'0b11'
>>> bin(b)
'0b110'
>>> a&b
2
>>> a=3
>>> b=9
>>> a&b
1
>>> a=68
>>> -(a+1)
-69
>>> a=-70
>>> ~a
69
>>> a=12
>>> b=28
>>> a^b
16
>>> a=3
>>> a<<2
12
>>> a=12
>>> a<<4
192
>>> 
>>> a=8
>>> a>>3
1
>>> 