from tkinter import *
root = Tk()

from englisttohindi.englisttohindi import EngtoHindi
translate = input(" ENTER TRANSLATE = ")
read = EngtoHindi(translate)
print(read.convert) 