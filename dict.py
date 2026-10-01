Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dict{}
>>> a={"name":"sriram",:"year":2026,"mounth":9}
SyntaxError: invalid syntax
>>> a={"name":"sriram","year":2026,"mounth":9}
>>> print(a)
{'name': 'sriram', 'year': 2026, 'mounth': 9}
>>> type(a)
<class 'dict'>
>>> b={"name","year","mounth"}
>>> type(b)
<class 'set'>
>>> a.keys()
dict_keys(['name', 'year', 'mounth'])
>>> a.values()
dict_values(['sriram', 2026, 9])
>>> a.items()
dict_items([('name', 'sriram'), ('year', 2026), ('mounth', 9)])
>>> a={"name":"sriram","city":"vja"}
>>> a["name]
  
SyntaxError: EOL while scanning string literal
>>> a["name"]
'sriram'
>>> a.get("sriram")
>>> a
{'name': 'sriram', 'city': 'vja'}
>>> a["sriram"]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a["sriram"]
KeyError: 'sriram'
>>> a={"city":"vja","state":"ap","country":"india"}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("state")
'ap'
>>> a
{'city': 'vja', 'country': 'india'}
>>> {'city': 'vja', 'country': 'india'}
{'city': 'vja', 'country': 'india'}
>>> a.popitem()
('country', 'india')
>>> a
{'city': 'vja'}
>>> a={"course":"python","duration":100}
>>> a.update({"year":2026})
>>> a
{'course': 'python', 'duration': 100, 'year': 2026}
>>> a.update({"month":"sep"},{"date":30})
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.update({"month":"sep"},{"date":30})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"month":"sep","date":30})
>>> a
{'course': 'python', 'duration': 100, 'year': 2026, 'month': 'sep', 'date': 30}
>>> a={"date":30,"time":11}
>>> a.setdefault("hour",11)
11
>>> a
{'date': 30, 'time': 11, 'hour': 11}
>>> a.setdefault(11,"hour")
'hour'
>>> a
{'date': 30, 'time': 11, 'hour': 11, 11: 'hour'}
>>> a={"colour":"white","food":"biryani"}
>>> a.copy()
{'colour': 'white', 'food': 'biryani'}
>>> len(a)
2
>>> a.count("colour")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.count("colour")
AttributeError: 'dict' object has no attribute 'count'
>>> a.index("food")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.index("food")
AttributeError: 'dict' object has no attribute 'index'
>>> a.clear()
>>> a
{}
>>> a={"name":"sriram","city":"vja","name":"sriram"}
>>> print(a)
{'name': 'sriram', 'city': 'vja'}
>>> a={"name":"sriram","city":"vja","name":"sai"}
>>> a
{'name': 'sai', 'city': 'vja'}
>>> a={"name1":"sriram","city":"vja","name2":"sai"}
>>> a
{'name1': 'sriram', 'city': 'vja', 'name2': 'sai'}
>>> a={"idnos":[10,20,30],"names":["ambica","sai","sriram"]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['ambica', 'sai', 'sriram']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names'])
>>> a.values()
dict_values([[10, 20, 30], ['ambica', 'sai', 'sriram']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['ambica', 'sai', 'sriram'])])
>>> 