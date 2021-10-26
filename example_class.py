#!/usr/bin/python3

class TestClass:

    def __init__(self, name, home):
        self.name = name
        self.home = home

    def printName(self):
        print(self.name)

    def printHome(self):
        print(self.home)


class1 = TestClass("Aaron", "Canada")
class2 = TestClass("Isaac", "Ghana")
class1.printName()
class2.printName()
class2.printHome()
class2.home = "Canada"
class2.printHome()
