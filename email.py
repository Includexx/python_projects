email = input("ENTER YOUR EMAIL :")
#rajk730152@gmail.com
k,d,j=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha(): 
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1            
                if k==1 or j==1 or d==1:
                    print("WRONG EMAIL 5 !!")        
            else:
                print("WRONG EMAIL 4 !!")
        else:
            print("WRON EMAIL 3 !!")
    else:
        print("WRONG EMAIL 2 !!")
else:
    print("WRONG EMAIL 1 !!! ")
