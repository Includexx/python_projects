class employee:
    def __init__(self,name,id):
        self.name= name
        self.id= id
    def showDetails(self):
        print(f"id of employee {self.id} and name is {self.name}")
class programmer(employee):
    def showlanguage(self):
        print("DEFAULT LANGUAGE IS PYTHON")
        
            
a= employee("karan", 455)
a.showDetails()            
b= programmer("raj kumar" , 420)
b.showDetails()
b.showlanguage()   
     