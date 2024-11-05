from programmer import Programmer
from actor import Actor
from farmer import Farmer

people = [
    Programmer("dave",42,"Python"),
    Actor("Song", 55,"Parasite"),
    Farmer("Kim",40,"Apple")
]

for person in people:
    person.introduce()

dave = Programmer("dave",42,"Python")
dave.__age = -1

dave._hello()
