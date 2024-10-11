# define functions
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

# take input from the user
print("what do you wanna do?")
print("1.add (if you do this you're probably a big nerd  )")
print("2.subtract (actually pretty cool bro)")
print("3.multiply (DEEZ NUTZ)")
print("4.divide (give everything to the cats)")

choice = input("DECIDE ALREADY YOU SICK MF: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   result_1 = add(num1, num2)
   wtv_usr_put_1 = int(input(f"How much is {num1} + {num2}? "))
   if wtv_usr_put_1 == result_1:
      print("Holy shit you did it yourself!")
   else:
      print("Kinda took the L here lmfao")    

elif choice == '2':
    result_2 = subtract(num1, num2)
    wtv_usr_put_2 = int(input(f"how much is {num1} - {num2}? "))
    if wtv_usr_put_2 == result_2:
        print("can't believe you didn't a fucking CALCULATOR")
    else:
        print("get a normal calculator dumbass")

elif choice == '3':
   print(f"{num1} * {num2} = {multiply(num1,num2)}")

elif choice == '4':
   print(f"{num1} / {num2} = {divide(num1,num2)}")

else:
   print("Invalid input")
