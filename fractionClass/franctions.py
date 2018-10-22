#!/bin/env/python3
class Fraction:

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return '%d/%d' %(self.num,self.denom)
        return ret

    def __add__(self,other):
        _num = (self.num * other.denom) + (other.num * self.denom)
        _denom = (self.denom * other.denom)
        return Fraction(_num,_denom).simplify()

    def __mul__(self,other):
        _num = self.num * other.num
        _denom = self.denom * other.denom
        return Fraction(_num,_denom).simplify()

    def __sub__(self,other):
        _num = (self.num * other.denom) - (other.num * self.denom)
        _denom = (self.denom * other.denom)
        return Fraction(_num,_denom).simplify()
        
    def __truediv__(self,other):
        _num = self.num * other.denom
        _denom = self.denom * other.num
        return Fraction(_num,_denom).simplify()

    def simplify(self):
        GCD1 = set()
        GCD2 = set()
        for i in range(1,self.num):
            if self.num % i == 0:
                GCD1.add(i)
        for i in range(1,self.denom):
            if self.denom % i == 0:
                GCD2.add(i)
        GCD = max(GCD1 & GCD2)
        return Fraction(self.num / GCD,self.denom / GCD)

x = Fraction(8,13)
y = Fraction(7,21) 

print (x+y)
print (x*y)
print (x-y)
print (x/y)

