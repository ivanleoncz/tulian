# -*- coding: utf-8 -*-

class Immutable:
    """ Separate class for treatment of immutable data types. """


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


    def strs(self, data):
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


    def frozens(self, data):
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


    def booleans(self, data):
        """
        Maps booleans.
        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.
        Returns
        -------
        list : comprehension
            Composed of booleans.
        """
        return [b for b in data if type(b) == bool]
