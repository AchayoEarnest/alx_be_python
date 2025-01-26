class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f"Created {self.name} successfully")
    
    def __del__(self):
        print(f"{self.name} has been deleted. Goodbye!")

p = Person("Earnest", 32);
del p