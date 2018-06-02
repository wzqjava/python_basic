#!encoding=utf-8
class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print("--test1--")

    def __test2(self):
         print("--test2--")

    def test3(self):
        self.__test2()
        print(self.__num2)

class B(A):
    def test4(self):
       self.__test2()
       print(self.__num2)



b = B()
# b.test3()
b.__test2()
# print(b.num1)
# print(b.num2)
#b.test3()   #父类中的方法可以调用父类中的私有属性和方法
# b.test4()    #自己的方法不可以调用父类的私有属性和方法
