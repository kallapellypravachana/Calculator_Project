from calculator import*
from history import Histroy
import math 
history=Histroy()
while True:
 print("\n 1.Add  2.Sub 3.Mul 4.Division 5.exponenial 6.square 7.modulus")
 print("H.history,Q.quit,C.clear")
 choice = input("your choice:").upper()
 if choice=="H":
   history.show()
 elif choice=="Q":
   break
 elif choice=="C":
   history.clear()
 else:
  try:
   a=int(input("Enter any number:"))
   b=int(input("Enter any number:"))
   if choice=="1":
     result=add(a,b)
   elif choice=="2":
     result=sub(a,b)
   elif choice=="3":
     result=mul(a,b)  
   elif choice=="4":
     result=divi(a,b)
   elif choice=="5":
     result=square(a)  
   elif choice=="6":
     result=power(a,b)  
   elif choice=="7":
     result=mod(a,b)  
   print("Result:",result)
   history.add(str(result))
  except ValueError:
    print("Invalid")
   