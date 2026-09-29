Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=13
>>> b=24
>>> print("ram of {}{}".format(a*b))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("ram of {}{}".format(a*b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> c=a*b
>>> print("ram of {}".format(a*b))
ram of 312
>>> print("ram of {c}")
ram of {c}
>>> print(f"ram of {c}")
ram of 312
>>> 