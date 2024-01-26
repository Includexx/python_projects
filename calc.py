print(""""enter 0 to addition""")
print("""enter 1 for subtraction""")
print("""enter 2 for multication""")
print("""enter 3 for divion""")
x=int(input("ENTER YOUR CHOICE:"))
match x:
  case 0:
    b=int(input("ENTER FIRST NUM:"))
    c=int(input("ENTER SECOND NUM:"))
    print("addition is two number:",b+c)
  case 1:
    b=int(input("ENTER FIRST NUM:"))
    c=int(input("ENTER SECOND NUM:"))
    print("subtraction is two number:",b-c)
  case 2:
    b=int(input("ENTER FIRST NUM:"))
    c=int(input("ENTER SECOND NUM:"))
    print("multication is two number:",b*c)
  case 3:
    b=int(input("ENTER FIRST NUM:"))
    c=int(input("ENTER SECOND NUM:"))
    print("divition is two number:",b/c)
  case 4:
    print("x is for")
  case 5:
    print("x is five")
  case 6:
    print("x is six")
  case 7:
    print("x is seven")
  case _:
    print(" case is nul")
