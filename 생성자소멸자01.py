# -*- 생성자와 소멸자 -*-
class MyClass:
    #생성자 필수
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #소멸자 유명무실(?)
    def __del__(self):
        print("Instance is deleted!")

