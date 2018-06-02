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


dog =  Dog()
dog.eat()
dog.bark()

cat = Cat()
cat.eat()
cat.sleep()





