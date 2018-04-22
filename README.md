## Tulian
Insights from Tuples and Lists, using Comprehensions. 

Tulian provides a summary (JSON) of data types present on such source 
and provides the extraction of a specific data type, present as List.

## Usage

```
>>> from tulian import Tulian
>>> 
>>> data = Tulian()
>>> 
>>> l = ['Python', 'Node.js', 2018, 365, 3.14, 'Guido', ['GNU', 'Linux'], (10, 100, 1000, 10000), 1988]
>>>
```

- Generating summary of all data types:

```
>>> print(data.summary(l))
{
    "float": 3,
    "lists": 1,
    "tuples": 1,
    "int": 3,
    "str": 3
}

```
 
- Extracting specific data types:

```
>>> data.ints(l)
[2018, 365, 1988]
>>>
>>> data.strs(l)
['Python', 'Node.js', 'Guido']
>>>
```
