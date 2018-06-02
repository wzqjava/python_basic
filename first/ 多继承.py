class A(object):
    def test1(self):
        print("-----test1")


class B(object):
    def test2(self):
        print("-------test2")


class C(A,B):
    pass

c = C()
c.test1()
c.test2()