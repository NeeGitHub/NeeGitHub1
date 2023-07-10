class Animal:
    def sound(self):
        print("Animal makes a sound.")
class Cow(Animal):
    def mooes(self):
        print("Cow mooes.")
cow=Cow()
cow.sound() #Output: Animal makes a sound.
cow.mooes() #Output: Cow mooes.

class Mammal(Animal):
     def feed_milk(self):
        print("Mammal feeds milk.")
class Dog(Mammal):
     def bark(self):
        print("Dog barks.")
dog = Dog()
dog.feed_milk() #Output:Mammal feeds milk.
dog.bark() #Output:Dog barks.
class Insect(Animal):
     def lay_eggs(self):
        print("Insects lay eggs.")
class Mosquito(Insect):
    def fly(self):
        print("Mosquito flies.")
mosquito = Mosquito()
mosquito.lay_eggs() #Output: Insects lay eggs.
mosquito.fly() #Output: Mosquito flies.




  
        
        
        
        








