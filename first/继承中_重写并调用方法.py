#!/usr/bin/python3
#! encoding=utf-8

class Animal(object):
    def eat(self):
        print("--吃---")

    def sleep(self):
        print("--睡觉--")

class Dog(Animal):
    def bark(self ):
        print("--汪汪叫--")

class Cat(Animal):
    def catch(self):
        print("--抓老鼠--")

class HaShiQi(Dog):
    def bark(self ):
        print("--吼吼叫--")
        # 调用父类的第一种方法
        Dog.bark(self)




haShiQi =  HaShiQi()

haShiQi.bark()







