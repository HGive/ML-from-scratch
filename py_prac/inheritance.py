class A:
    def method(self):
        print("I'm A")

class B(A):
    def method(self):
        print("I'm B")

class C(A):
    def method(self):
        print("I'm C")

class D(B,C):
    pass

d = D()

d.method()

#어떤 메서드가 어떤 부모클래스의 메서드가 호출되는지 파악하는것.
print(D.mro())
