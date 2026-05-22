class Animal:
    def __init__(self, name, age, sound, type):
        self.name =name
        self.age = age
        self.sound =  sound
        self.type = type
        pass

    def speak(self):
        print(self.sound)
        
    def move(self):
        print("The animal moved five feet")

    def describe(self):
        print(f"Name: {self.name}, Age: {self.age}, Type: {self.type}")

    def __str__(self):
        return f"""{Animal.speak}
        {Animal.move}
        {Animal.describe}
        """


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "WOOF!", "Mamamal")
        self.__breed = breed

    def move(self):
        print(f"{self.name} runs five steps")

    def __str__(self):
        return f"""{Dog.speak}
        {Dog.move}
        """


class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age, "Tweet", "Flying thing")
        self.__can_fly = can_fly

    def move(self):
        print(f"{self.name} flys around")

    def __str__(self):
        return f"""{Bird.move}
        {Bird.speak}
        """

class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age, "Gubble", "Swimming creatures")
        self.__water_type = water_type


    def move(self):
        print(f"{self.name} swims around")

    def __str__(self):
        return f"""{Fish.move}
        {Fish.speak}
        """



class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age, "Meow", "mammal")
        self.__indoor = indoor

    def move(self):
        print(f"{self.__name} walks around")

    def __str__(self):
        return f"""{Cat.speak}
        {Cat.move}
        """