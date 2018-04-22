# -*- coding: utf-8 -*-

class Mutable:
    """ Separate class for treatment of mutable data types. """


    def bytearrays(self, data):
        """
        Maps byte arrays.
        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.
        Returns
        -------
        list : comprehension
            Composed of byte arrays.
        """
        return [b for b in data if type(b) == bytearray]


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
