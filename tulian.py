#!/usr/bin/python3
""" Extracts data from tuples and lists. """

__author__ = "@ivanleoncz"


class Tulian:

    def __init__(self,lst):
        self.lst = lst
    

    def numbers(self):
        """ Maps all numbers, using list comprehensions with filter. 
        
        Returns a list. """
        return [n for n in self.lst if type(n) == int]


    def strings(self):
        """ Maps all strings, using list comprehensions with filter. 
        
        Returns a list. """
        return [s for s in self.lst if type(s) == str]


    def dicts(self):
        """ Maps all dicts, using list comprehensions with filter. 
        
        Returns a list. """
        return [d for d in self.lst if type(d) == dict]


    def tuples(self):
        """ Maps all tuples, using list comprehensions with filter. 
        
        Returns a list. """
        return [t for t in self.lst if type(t) == tuple]


    def lists(self):
        """ Maps all lists, using list comprehensions with filter. 
        
        Returns a list. """
        return [l for l in self.lst if type(l) == list]
