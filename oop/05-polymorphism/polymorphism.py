class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

class student(person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
    
    # polymorphism. polymorphism means that the same method can have different behavior depending on the type of object that it is called on
    def get_info(self):
        return f"{self.name} is {self.age} years old and has a grade of {self.grade}"
    
class teacher(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # polymorphism
    def get_info(self):
        return f"{self.name} is {self.age} years old and teaches {self.subject}"
        
def main():
    p1 = person("John", 30)
    s1 = student("Alice", 20, "123456", "A")
    t1 = teacher("Bob", 40, "Math")
    
    print(p1.get_info())
    print(s1.get_info())
    print(t1.get_info())