#최기영_2주차시험답안.py

#1.은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

#2.
class Developer:
    num_developer = 0
    name = "default name"


#3.
class WebDeveloper(Developer):
    def __init__(self, id, name, getSarlary):
        Developer.__init__(self, id, name)
        self.getSarlary = getSarlary
    def printInfo(self):
        print("Info(id:{0}, name: {1})".format(self.id,self.name))
        print("Info(getSarlary:{0})".format(self.getSarlary))

#4.
#함수:1개의 기능을 사용
#클래스:n개의 기능과 데이터
#모듈:1개파일(n개의 함수, n개의 클래스)
#패키지:데이터를 다루는폴더

#5.
import re
p = re.compile("[0-9]")
pChecker = p.serach("\d{5}")
print(pChecker)
