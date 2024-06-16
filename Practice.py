#انواع متغیر لوکال و گلوبال و نان لوکال 
# x = 2

# def my_f():
#     print(x)

# my_f()
# print(x)

# x = 2 

# def my_f():
#     global x
#     x += 2
#     print(x)

# my_f()
# print(x)

# def my_f(x):
#     x += 2
#     print(x)

# my_f(5)
# print(x)
# x = 10
# def my_f1():
#     x = 2
#     print(x)
#     def my_f2():
#         print(x)
#     my_f2()
# my_f1()

# کلاس داینامیک 

# x = 3 
# y = type (x)
# print(y)

# class Cat: 
#     def __init__(self):
#         pass
#     def sound(self):
#         print('mio mio')   

# Tom = Cat()
# print(Tom)
# Tom.sound()

# def constructor(self):
#     pass
# def catsound(self):
#     print('mio mio')

# cat = type("catsound type", (), {
#    "__init": constructor,
#     "sound": catsound 
#     }) 
# tom =  cat()  
# print(tom)

# tom.sound()

#ثابت ها (constants)

# X = 400 
# print(X)

# def x():
#     return 400

# print(x())

# class Constant: 
#     __slots__ = ()
#     PI = 3.14

# const = Constant()
# print(const.PI)   
# const.PI = 5
# print(const.PI)

# import sys
# class Constant:
#     __slots__: ()
#     PI = 3.14

# const = Constant()
# print(sys.getsizeof(const))
# %timeit const.PI

# class Constant: 
#     PI = 3.14 

# const = Constant()

# print(sys.getsizeof(const))


# class Constant: 
#     __slots__=('x', 'y')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y 

# const = Constant(10, 15)
# const.x = 25
# print(const.x)

# from m import *
#import m
# if __name__ == "__main__":
#     print('ok')

#Duder method or magical methods

# class A:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return A(self.value + other.value) 

# x = A(5)
# # print(x.value)  

# y = A(6)
# z = A(1)

# # print(y.value)
# s = x+y+z
# print(s.value)

# class A:
#     def __init__(self):
#         print("a call to the constractor method")
#     def __new__(cls):
#         print("a call to the new method")
#         # return object.__new__(cls)
#     def __del__(self):
#         print("a call to the destractor method")

# x = A()
# print(x)

# private attributes and methods 

# class A:
#     def __init__(self):
#         self.val = 2
#         self._val = 4
#         self.__val = 6

# x = A()
# print(x.val)
# print(x._val)
# # print(x.__val)
# print(x._A__val)

# print(x.__dict__)

# کد همینگ
# import numpy as np 



#type hinting


















