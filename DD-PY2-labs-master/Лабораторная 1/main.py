import datetime

class pen:
    """Класс ручка"""
    def __init__(self, colour: str, gel_amount: int, name:str):
        if gel_amount < 0:
            raise ValueError("количество геля не может быть отрицательным")
        if colour not in ["red", "black", "blue", "green", "pink", "yellow", "violet"]:
            raise ValueError("введен некорректный цвет")
        self.colour = colour
        self.gel_amount = gel_amount
        self.name = name

    def write(self, text:str)-> str:

        """Метод для написания текстов ручкой"""

class door:
    """класс дверь"""
    def __init__ (self, status:str, number:str):
        if status not in ["open", "closed"]:
            raise ValueError("Введено некорректное положение двери")
        self.status = status
        self.number = number

    def open(self):

        """метод открытия двери"""
    def close(self):

        """метод закрытия двери"""
    def lock(self):

        """метод блокироовки двери"""


class alarmclock:
    """класс будильник"""
    def __init__(self, set_time:datetime):
         if not isinstance(set_time, (datetime)):
            raise ValueError("введено некорректное время и дата")
         self.set_time =set_time

    def set_time(self, time:datetime):
        """метод установки будильника"""

    def ring(self):
        """метод звонка будильника"""
