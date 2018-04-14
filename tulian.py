#!/usr/bin/python3
""" Extracts data and insights from tuples and lists. """

__author__ = "@ivanleoncz"


class Tulian:


    def numbers(self, data):
        """
        Maps numbers.

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
