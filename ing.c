str=input("enter the string:")
if str.endswith("ing"):
       str=str+"ly"
else:
       str=str+"ing"

print(str)