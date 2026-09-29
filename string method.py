Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string methods
>>> a="python"
>>> len(a)
6
>>> b="python fullstack"
>>> len(b)
16
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> #count()
>>> a="twinkle twinkle little star"
>>> a.count("teinkle")
0
>>> a.count("t")
5
>>> a.count(" ")
3
>>> #find a string
>>> a="python"
>>> a.find("o")
4
>>> a.find("p")
0
>>> b="hello"
>>> b.find("l")
2
>>> #escape sequences
>>> #\n->new line
>>> #\t->tab space
>>> a= "name\nmobileno\tcollege\nmailid\tbranch"
>>> print(a)
name
mobileno	college
mailid	branch
>>> b="name:Sriram\nmobileno:9193941234\tcollege:Veltech\nmailid:sriramkalidindi8@gmail.com\tbranch:CSE"
>>> print(b)
name:Sriram
mobileno:9193941234	college:Veltech
mailid:sriramkalidindi8@gmail.com	branch:CSE
>>> #replace()
>>> a="python java"
>>> a.replace("java","fullstack")
'python fullstack'
>>> #uppercase|lowercase
>>> a="python"
>>> a.upper()
'PYTHON'
>>> b="JAVA"
>>> b.lower()
'java'
>>> c="sriram"
>>> c.capitalize()
'Sriram'
>>> d="i am in class"
>>> d.title(0
	d.title()
	
SyntaxError: invalid syntax
>>> d.titlr()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d.titlr()
AttributeError: 'str' object has no attribute 'titlr'
>>> d.title()
'I Am In Class'
>>> #condition's
>>> a="java"
>>> a.isupper()
False
>>> a.islower()
True
>>> b="PYTHON"
>>> b.isupper(0
	  ssd
	  
SyntaxError: invalid syntax
>>> b.isupper()
True
>>> b.islower()
False
>>> c="codegnan'
SyntaxError: EOL while scanning string literal
>>> c="codegnan"
>>> c.isstart("c")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    c.isstart("c")
AttributeError: 'str' object has no attribute 'isstart'
>>> c.sartswith("c")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c.sartswith("c")
AttributeError: 'str' object has no attribute 'sartswith'
>>> c.startswith("c")
True
>>> c.endswith("m")
False
>>> d="python codining"
>>> d.isalpha()
False
>>> e="pythoncodining"
>>> e.isalpha()
True
>>> f="1235"
>>> f.isalnum()
True
>>> g="ram123"
>>> g.isalnum()
True
>>> h="ram@123"
>>> h.isascll()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    h.isascll()
AttributeError: 'str' object has no attribute 'isascll'
>>> h.isascii()
True
>>> #strip()
>>> a="   ram  "
>>> a.strip()
'ram'
>>> b="   ra  m"
>>> b.strip()
'ra  m'
>>> #concadination
>>> a="sri"
>>> b="ram"
>>> c=a+b
>>> print(c)
sriram
>>> cname="Sriram"
>>> dname="kalidindi"
>>> print(cname+dname)
Sriramkalidindi
>>> print(cname.title()+dname.title())
SriramKalidindi
>>> #split()
>>> a="c c++ python java"
>>> a.split()
['c', 'c++', 'python', 'java']
>>> b="i an in the class"
>>> b.split()
['i', 'an', 'in', 'the', 'class']
>>> #join()
>>> a="apple","banana","orange"
>>> "".join(a)
'applebananaorange'
>>> " ".join(a)
'apple banana orange'
>>> "s".join(a)
'applesbananasorange'
>>> b="apple"
>>> "l".join(b)
'alplpllle'
>>> #formatting
>>> a=6
>>> b=9
>>> print(a+b)
15
>>> print("the sum is",a+b)
the sum is 15
>>> city="vja"
>>> print("city is",city)
city is vja
>>> #format method
>>> a="Sri"
>>> b="ram"
>>> print("hello {}{}".format(a,b)
      print("hello {}{}".format(a,b))
      
SyntaxError: invalid syntax
>>>  print("hello {}{}".format(a,b))
 
SyntaxError: unexpected indent
>>> print("hello {}{}".format(a,b))
hello Sriram
>>> print("hello {} {}".format(a,b))
hello Sri ram
>>> print("hello {} hello{}".format(a,b))
hello Sri helloram
>>> print("hello {} hello {}".format(a,b)).title()
hello Sri hello ram
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    print("hello {} hello {}".format(a,b)).title()
AttributeError: 'NoneType' object has no attribute 'title'
>>> print("hello {} hello {}".format(a,b)).title())
SyntaxError: unmatched ')'
>>> print("hello {} hello {}".format(a,b).title())
Hello Sri Hello Ram
>>> print(("hello {} hello {}".format(a,b)).title())
Hello Sri Hello Ram
>>> #fstring
>>> a="Sri"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello Sriram
>>> print(f"hello {a} {b}")
hello Sri ram
>>> print(f"hello {a} hello{b}")
hello Sri helloram
>>> print((f"hello {a}{b}").title())
Hello Sriram
>>> 