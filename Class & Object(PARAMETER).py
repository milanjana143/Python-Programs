class student:
    def __init__(self,n,s,r):
        self.name = n
        self.stream = s
        self.roll = r
    def display(self):
        print("Student Name :-",self.name)
        print("Stream :-",self.stream)
        print("Roll No :-",self.roll)

a = student("Samujjwal Patra","BCA",56)
a.display()