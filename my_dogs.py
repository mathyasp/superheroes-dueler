# my_dogs.py
from dog import Dog # we need to specify exactly what we want

my_dog = Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)

# Stretch Challenges

my_first_dog = Dog("Ralph", "Rottweiler")
my_first_dog.bark()

my_second_dog = Dog("Buddy", "Bulldog")
my_second_dog.sit()

my_third_dog = Dog("Daisy", "Dachshund")
my_third_dog.roll_over()