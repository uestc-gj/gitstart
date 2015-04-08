# -*- coding:utf-8
'''
Dynamic binding in python 
'''

class Person:
    '''Defines a general person '''
  
    def _description(self):
        return "Person function"

    def printInfo(self):
        print self._description()

class Parent(Person):
    '''Defines a parent '''
    def _description(self):
        return "Parent function"
