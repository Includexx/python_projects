import random
def check(comp,user):
    if(comp==0 and user==1):
        return 1
    if(comp==user):
        return 0
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1
comp= random.randint(0,2)
user=int(input("0 FOR SNAKE , 1 FOR WATER , 2 FOR GUN   "))
score= check(comp,user)
if(score==0):
    print("DRAW")
elif(score==-1):
    print("YOU LOSE")
else:
    print("YOU WON")      