from time import *
import random as r

def mistack(pratest,usertest):
    error = 0
    for i in range(len(pratest)):
       try :
                error=error+1
       except :
               error=error+1   
    return error

def speed_time(time_s,time_e,userinput):
    time_delay= time_e-time_s
    time_R= round(time_delay,2)
    speed= len(userinput)/time_R
    return round(speed)


test =["my name is raj kumar","and your name is rohit","i am from india"]

test1 = r.choice(test)
print("  ***  TYPING SPEED  ***   ")
print(test1)
print()
print()
time_1 = time()
testinput=input("ENTER  :")
time_2 = time()
print("speed  :",speed_time(time_1,time_2,testinput),"w/sec")
print("ERROR  :", mistack(test1,testinput))
