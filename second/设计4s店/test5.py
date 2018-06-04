#encoding=utf-8
class CarStore(object):

    #init中初始化工厂
    def __init__(self):
        self.factory = Factory() #得到工厂对象

    def order(self, car_type):
        #   用工厂制作产品
        return self.factory.select_car_by_type(car_type)


class Factory(object):
    def select_car_by_type(self, car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "名图":
            return Mingtu()
        elif car_type == "ix35":
            return Ix35()


class Car(object):
    def move(self):
        print("车在移动....")

    def music(self):
        print("正在播放音乐....")

    def stop(self):
        print("车在停止....")


class Suonata(Car):
    pass


class Mingtu(Car):
    pass


class Ix35(Car):
    pass


car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.music()
car.stop()
