## Tulian
Insights from Tuples and Lists, using Comprehensions. 

Tulian provides a summary (JSON) of data types contained in a Tuple or in a List. 


```
>>> from tulian import main
>>> 
>>> data = main.Tulian()
>>> 
>>> l = ['Python', 'Node.js', 2018, 3.14, [20, 20.2, 56.4, 86, 76.3, 22], (10, 100, 1000, 10000), 1988]
>>>
>>> print(data.summary(l))
{
    "lists": 1,
    "float": 2,
    "tuples": 1,
    "int": 2,
    "str": 2
}

```
 
It also provides the extraction/presentation of a specific data type.

```
>>> data.ints(l)
[2018, 1988]
>>>
>>> data.strs(l)
['Python', 'Node.js']
>>>
>>> data.tuples(l)
[(10, 100, 1000, 10000)]
```

For obtaining information of nested Tuples and Lists, the positional argument must be passed:


```
>>> print(data.summary(l[4]))
{
    "float": 3,
    "int": 3
}

```
