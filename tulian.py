#!/usr/bin/python3
""" Provides insights and filtered data from method parameter. """

from json import dumps

__author__ = "@ivanleoncz"


class Tulian:


    def ints(self, data):
        """
        Maps integers.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of integers.
        """
        return [n for n in data if type(n) == int]


    def floats(self, data):
        """
        Maps Floating-point numbers.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of Floating-point numbers.
        """
        return [f for f in data if type(f) == float]


    def complex(self, data):
        """
        Maps complex numbers.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of complex numbers.
        """
        return [c for c in data if type(c) == complex]


    def strings(self, data):
        """
        Maps strings.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of strings.
        """
        return [s for s in data if type(s) == str]


    def bytes(self, data):
        """
        Maps byte strings.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of byte strings.
        """
        return [b for b in data if type(b) == bytes]


    def dicts(self, data):
        """
        Maps dicts.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of strings.
        """
        return [d for d in data if type(d) == dict]


    def tuples(self, data):
        """
        Maps tuples.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of tuples.
        """
        return [t for t in data if type(t) == tuple]


    def lists(self, data):
        """
        Maps lists.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of lists.
        """
        return [l for l in data if type(l) == list]


    def sets(self, data):
        """
        Maps sets.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of sets.
        """
        return [s for s in data if type(s) == set]


    def frozen(self, data):
        """
        Maps frozen sets.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        list : comprehension
            Composed of fronzen sets.
        """
        return [f for f in data if type(f) == frozenset]


    def summary(self, data):
        """
        Summary of all information contained on data.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        d : dictionary
            Presents a summary of all information contained in data.
        """
        d = {}
        d["int"]        = len(self.ints(data))
        d["bytes"]      = len(self.bytes(data))
        d["complex"]    = len(self.complex(data))
        d["float"]      = len(self.ints(data))
        d["str"]        = len(self.strings(data))
        d["dict"]       = len(self.dicts(data))
        d["tuples"]     = len(self.tuples(data))
        d["lists"]      = len(self.lists(data))
        d["sets"]       = len(self.sets(data))
        d["frozensets"] = len(self.frozen(data))
        new_d = { k:v for (k,v) in d.items() if d[k] != 0}
        return dumps(new_d, indent=4)
