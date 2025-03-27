# add your Student class here!
class Student:
    def __init__ (self, name: str, year: str, classes: list):
        self.name = name
        self.year = year
        self.classes = classes

    def add_class(self, subject):
        self.classes.append(subject)

    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        return f"{self.name} is a {self.year} with {self.get_num_classes()} classes"