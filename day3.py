Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a={"one":"1","two":"2","three":"3"}
>>> b={"four":"4","five":"5","six":"6"}
>>> a.update(b)
>>> print(a)
{'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6'}
>>> a={"national animal":"tiger","national bird":"peacock","national flower":"lotus"}
>>> del a["national flower"]
>>> print(a)
{'national animal': 'tiger', 'national bird': 'peacock'}
>>> keys=['name','age','sex']
>>> values=['ram','20','male']
>>> myDict=dict(zip(keys,values))
>>> print("Dictionary Items  :  ",  myDict)
Dictionary Items  :   {'name': 'ram', 'age': '20', 'sex': 'male'}
>>> #python program to find the length of the list
>>> seta=set([1,2,3,4,5,6,7,8,9])
>>> print(len(seta))
9
>>> #python program to remove the intersection of 2nd set from 1st set
>>> a={1,2,3,4,5,6,7}
>>> b={3,7,5,9,8,0,13}
>>> print(a & b)
{3, 5, 7}
>>> 