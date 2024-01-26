def greet(fx):
    def mfx():
        print("GOOD MORNING")
        fx()
        print("thanks for using this function")
        return mfx
@greet
def hello():
    print("hello world")
    
def add(a,b):
 print(a+b)
 hello()   
    
    