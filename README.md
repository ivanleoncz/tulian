## Tulian
Insights from Tuples and Lists, using Comprehensions. 

Tulian provides a summary (JSON) of data types contained in a Tuple or in a List. 


```
>>> from tulian import main
>>> 
>>> data = main.Tulian()
>>> 
>>> l = ['Python', 'Node.js', 2018, 365, 3.14, 'Guido', ['GNU', 'Linux'], (10, 100, 1000, 10000), 1988]
>>>
>>> print(data.summary(l))
{
    "float": 3,
    "lists": 1,
    "tuples": 1,
    "int": 3,
    "str": 3
}

```
 
It also provides the extraction/presentation of a specific data type.

```
>>> data.ints(l)
[2018, 365, 1988]
>>>
>>> data.strs(l)
['Python', 'Node.js', 'Guido']
>>>
>>> data.tuples(l)
[(10, 100, 1000, 10000)]
```
