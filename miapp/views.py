from django.shortcuts import render
#  ------  classes ---------
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def info(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.color}"

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    
    def greeting(self):
        return f"Hi, I am {self.name}, I am {self.age} years old and I am a {self.occupation}."

# --------------view---------------

def home(request):
    # instantiating the objects
    car1 = Car("Toyota", "Supra", 2022, "White")
    person1 = Person("Mike Schmidt", 28, "Mechanic")
    
    context = {
        'car': car1,
        'person': person1,
    }
    
    return render(request, 'home.html', context)