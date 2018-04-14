#!/usr/bin/python3
""" Extracts data and insights from tuples and lists. """

__author__ = "@ivanleoncz"


class Tulian:


    def ints(self, data):
        """
        Maps ints.

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


    def strings(self, data):
        """
        Maps all strings.

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


    def dicts(self, data):
        """
        Maps all dicts.

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
        Maps all tuples.

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
        Maps all lists.

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
        d["int"] = len(self.ints(data))
        d["str"] = len(self.strings(data))
        return d
