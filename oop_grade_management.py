class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        pass


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print(
            f"Student: {self.name}, Marks: {self.marks}"
        )

    def __str__(self):
        return (
            f"Student,{self.name},{self.marks}"
        )


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(
            f"Teacher: {self.name}, Subject: {self.subject}"
        )

    def __str__(self):
        return (
            f"Teacher,{self.name},{self.subject}"
        )


student = Student("Rahul", 85)
teacher = Teacher("Sharma", "Python")

student.display()
teacher.display()

with open("records.txt", "w") as file:
    file.write(str(student) + "\n")
    file.write(str(teacher) + "\n")

print("Data Saved")
