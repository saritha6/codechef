class Personal:
               a=200
               def __init__(self,name,phno):
                              self.name=name
                              self.phno=phno
               def display(self):
                              print(self.name,self.phno)
class Student(Personal):
               def __init__(self,rollno,branch,name,phno):
                              self.rollno=rollno
                              self.branch=branch
                              super().__init__(name,phno)
               def display(self):
                              print(self.rollno,self.branch)
                              super().display()
                              
s1=Student(123,"IT","saritha",6303067373)
s1.display()
