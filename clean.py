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
print("3.multiply (mm yeah that sounds nice)")
print("4.divide (give everything to the cats)")

choice = input("are you ready to decide?: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   result_1 = add(num1, num2)
   wtv_usr_put_1 = int(input(f"How much is {num1} + {num2}? "))
   if wtv_usr_put_1 == result_1:
      print("Ay you got it!")
   else:
      print("try harder")    

elif choice == '2':
    result_2 = subtract(num1, num2)
    wtv_usr_put_2 = int(input(f"how much is {num1} - {num2}? "))
    if wtv_usr_put_2 == result_2:
        print("it doesn't seem like you need a calculator")
    else:
        print("get a normal calculator friend")

elif choice == '3':
    result_3 = multiply(num1, num2)
    wtv_usr_put_3 = int(input(f"how much is {num1}  {num2}?" ))
    if wtv_usr_put_3 == result_3:
        print("chat is this real 󱜹 !")
    else:
        print("never touch this file again (just kidding.. haha!)")

elif choice == '4':
   result_4 = divide(num1, num2)
   wtv_usr_put_4 = int(input(f"how much is {num1}  {num2}? "))
   if wtv_usr_put_4 == result_4:
      print("how are you so smart zamn")
   else:
      print("not cool")

else:
   print("ay pal... try again please")
