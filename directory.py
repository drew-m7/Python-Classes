# Drew Martin
# HW 10_18 on python classes
# Create the 4 classes where all have a print directory method as stated in assignment
# Person is superclass, the other 3 inherit parts of it, faculty also inherits directly
# from employee because they are similar
# Main creates the 8 objects and loops through them as a list and printing the directory

# Person class is the superclass for the other 3 classes
class Person(object):
   
    # init constructor for a basic person with no other distinctions
    def __init__(self, name, email):
        self.name = name
        self.email = email
   
    # Print directory
    def print_directory(self):
        print(self.name, '\n', self.email)

# Student class inheriting from person and adding major and grade level
class Student(Person):
   
    # init constructor creating major and level, gets the rest from person
    def __init__(self, name, email, major, level):
        super().__init__(name, email)
        self.major = major
        self.level = level
   
    # Print directory
    def print_directory(self):
        print(self.name, '\n', self.email, '\n', self.major, '\n', self.level)

# Employee class inheriting from person and adding dept and office
class Employee(Person):
   
    # init constructor creating dept and office, gets the rest from person
    def __init__(self, name, email, department, office):
        super().__init__(name, email)
        self.department = department
        self.office = office
   
    # Print directory
    def print_directory(self):
        print(self.name, '\n', self.email, '\n', self.department, '\n', self.office)

# Faculty class inheriting from employee and adding a research area
class Faculty(Employee):
   
    # init constructor creating research area, gets everything else from employee
    def __init__(self, name, email, department, office, research):
        super().__init__(name, email, department, office)
        self.research = research
   
    # Print directory
    def print_directory(self):
        print(self.name, '\n', self.email, '\n', self.department, '\n', self.office, '\n', self.research)

def main():
    
    # Created 8 objects demonstrating 2 of each
    p1 = Person('Jonathon Doe', 'jonthedoe@ilstu.edu')
    p2 = Person('Marilyn Monroe', 'marymo@ilstu.edu')
    p3 = Student('Steve Wozniak', 'thewoz@ilstu.edu', 'Biology', 'Freshman')
    p4 = Student('Drew Martin', 'drewmartin@ilstu.edu', 'Computer Science', 'Senior')
    p5 = Employee('Alan Turing', 'alan@ilstu.edu', 'Computer Science', 'STV 404B')
    p6 = Employee('Frank Sinatra', 'frankyboy@ilstu.edu', 'Finance', 'STV 169A')
    p7 = Faculty('Mark Zuckerberg', 'markyzucks@ilstu.edu', 'Information Technology', 'AAC 401C', 'Machine Learning, Natural Language Processing')
    p8 = Faculty('Elon Musk', 'captainmusk@ilstu.edu', 'Business', 'STV 101Q', 'Statistical Analysis, Financial Modeling')
    # loop through objects from a list and display them
    # creating list       
    list = [] 
    # appending instances to the list 
    list.append(p1)
    list.append(p2)
    list.append(p3)
    list.append(p4)
    list.append(p5)
    list.append(p6)
    list.append(p7)
    list.append(p8)
    # printing the directory out for each object in my list
    for obj in list:
        obj.print_directory()
        print('\n')

main()
