from abc import ABC, abstractmethod

class Vehicle(ABC):
    # def __init__(self, start_engine, move):
    #     self.start_engine = start_engine
    #     self.move = move

    @abstractmethod
    def engine_on():
        pass

    @abstractmethod
    def move():
        pass


class Car(Vehicle):
    def __init__(self, start_engine, go):
        self.start_engine = start_engine
        self.go = go

    
    def engine_on(self):
        if self.start_engine is True:
            print("Xe khởi động")

    def stop_engine(self):
        if self.start_engine is False:
            print("Xe tắt máy")

    def move(self):
        if not self.engine_on:
            print("Vui lòng khởi động xe")
        else:
            print("Xe đã chạy")


class Bike(Vehicle):
    def __init__(self):
        pass
    def move(self):
        print("Xe đã chạy")


class Boat(Vehicle):
    def __init__(self, start_engine, go):
        self.start_engine = start_engine
        self.go = go

    def engine_on(self):
        if self.start_engine is True:
            print("tàu khởi động")

    def stop_engine(self):
        if self.start_engine is False:
            print("tàu tắt máy")

    def  move(self):
        if not self.engine_on:
            print("Vui lòng khởi động xe")
        else:
            print("Xe đã chạy")


a = Car(False, True)
a.engine_on()