# encode=utf-8
#  Основная программа

import pygame
import tkinter

class Application(object):
    instance = None

    def __new__(cls,title,mode):
        print("Создание нового приложения")         
        if cls.instance is None:
            cls.instance = super(Application,cls).__new__(cls)
            return cls.instance
        else:
            print("Приложение уже запущено!")
            return None

    def __init__(self,title,mode):
        print("Инициализация приложения")
        self.title=title
        self.mode=mode
        if self.mode=='tkinter':
            print("Создание простого оконного приложения "+"'"+self.title+"'")
        elif self.mode=='pygame':
            print("Создание приложения с графическим ускорением "+ "'"+self.title+"'")

a=Application("Super","tkinter")









        
     
        

