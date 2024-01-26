class employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
   # def showme(self):
        print(f"my name is {self.name} and my age is {self.age}")
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("_")[0],string.split("_")[1])
a = employee("raj kumar",21)
print(a.name)
print(a.age)

string = "raj_12"
b = employee.fromstr(string)
print(b.name)
print(b.age)



        
        