class student:
    def data(self):
        self.name = input("Enter Your Name :- ")
        self.stream = input("Enter Your Stream :- ")
        self.roll = int(input("Enter Your Roll No :- "))
    def display(self):
        print("Student Name :-",self.name)
        print("Stream :-",self.stream)
        print("Roll No :-",self.roll)

a = student()
a.data()
a.display()