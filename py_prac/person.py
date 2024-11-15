from abc import ABC , abstractmethod

class Person(ABC):
    def __init__(self, name, age, job = None):
        self.name = name
        self.__age = age
        self.job = job

    @abstractmethod
    def introduce(self):
        pass

    #상속시 사용가능한 메소드를 protected method 라 하고 메소드명앞 _붙임
    def _hello(self):
        print(f"Hello, I'm {self.name} and {self.__age}.")
        
    def update_age(self, age):
        if age < 0:
            raise ValueError("나이는 음수일 수 없습니다.")
        else:
            self.__age = age
            print(f"Now I'm {self.__age} years old!")
