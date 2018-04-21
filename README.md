## Tulian
Insights from Tuples and Lists.

## Concept
Performs analysis of Tuples and Lists, using comprehensions.

## Usage

```
>>> from tulian import Tulian
>>> 
>>> data = Tulian()
>>> 
>>> l = ['Python', 'Node.js', 2018, 365, 3.14, 'Guido', ['GNU', 'Linux'], (10, 100, 1000, 10000), 1988]
>>>
```
 
Counting data types:

```
>>> data.ints(l)
[2018, 365, 1988]
>>>
>>> data.strings(l)
['Python', 'Node.js', 'Guido']
>>>
```

Denerating a summary of how all present data types:

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



