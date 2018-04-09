#!/usr/bin/python3
""" Extracts data from tuples and lists. """

__author__ = "@ivanleoncz"


class Tulian:


    def numbers(self, data):
        """ Maps all numbers, using list comprehensions.

        Arg:
            tuple or list

        Returns:
            list
        """
        return [n for n in data if type(n) == int]


    def strings(self, data):
        """ Maps all strings, using list comprehensions.

        Arg:
            tuple or list

        Returns:
            list
        """
        return [s for s in data if type(s) == str]


    def dicts(self, data):
        """ Maps all dicts, using list comprehensions.

        Arg:
            tuple or list
        
        Returns:
            list
        """
        return [d for d in data if type(d) == dict]


    def tuples(self, data):
        """ Maps all tuples, using list comprehensions.

        Arg:
            tuple or list
        
        Returns:
            list
        """
        return [t for t in data if type(t) == tuple]


    def lists(self, data):
        """ Maps all lists, using list comprehensions.

        Arg:
            tuple or list
        
        Returns:
            list
        """
        return [l for l in data if type(l) == list]
