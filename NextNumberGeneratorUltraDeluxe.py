import time
name = "Next number generator Ultra Delux"
creator = "Frog Millk"
print(name)
print(f"By {creator}")
code = True
while code:
 x = int(input("Input starting number: "))
 print("Using our supercomputer...")
 time.sleep(1)
 print("Asking aliens for the answer...")
 time.sleep(1)
 print("Summoning the wizard Teleknithos...")
 time.sleep(1)
 print(f"The next number is {x+1}!")
 again = input("Do you want to do it again? We will use the same process again. yes/no: ").lower()
 if again == "yes":
     code = True
 elif again == "no":
    print("Thank you for using a Frog Milk service!")
    input("Please press enter to exit") 
    code = False
 else:
   
  print("Thank you for using a Frog Milk service!")
  input("Invalid. Press enter to exit")
  code = False