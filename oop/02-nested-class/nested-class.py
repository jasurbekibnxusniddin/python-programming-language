class Student:
    def __init__(self, name, age, student_id, grade, address):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grade = grade
        self.address = address

    def get_info(self):
        return f"{self.name} is {self.age} years old and has a grade of {self.grade}"
    

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def get_address(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"
    

def main():
    student = Student("John", 20, "123456", "A", Address("123 Main St", "New York", "NY", "10001"))
    print(student.get_info())
    print(student.address.get_address())


if __name__ == "__main__":
    main()
