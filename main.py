from animals import Animal, Dog, Bird, Fish, Cat


def main():
    # Create one instance of each animal subclass
    my_dog = Dog("Billy", "3 years", "Dalmatian")
    my_bird = Bird("Bob","6 months", True)
    my_fish = Fish("Timmy", "4 weeks", "Saltwater")
    my_cat = Cat("Bob", "4 years", "indoor")
    animals = [my_dog, my_bird, my_fish, my_cat]

    # TODO: instantiate your animals and add them to the list
   
    # Loop over all animals and call speak(), move(), and describe()
    for animal in animals:
        print(animal.speak())
        print(animal.move())
        print()
        pass


if __name__ == "__main__":
    main()
