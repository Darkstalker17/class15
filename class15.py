'''
Well wishes
Outline:
Write a program to create a function name well wishes that will give output hello, how are you!
'''
def wellwishes():
    print("Hello, How are you?")
#wellwishes()

'''Weather condition
Outline:
Write a program to display the weather in autumn and spring:'''

def weather1():
    print("Weather is pleasant in autumn.")
def weather2():
    print("Weahther is more pleasant in spring than autumn.")
w = "spring"#input("Enter wheter You like autumn or spring: ")
if w == "autumn":
    weather1()
elif w == "spring":
    weather2()
else:
    print("Nice choice!")

'''Calculator
Outline:
Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide.
Ask for a choice from users which operation they want to perform. Take user input whatever operation they want
to perform And call that function accordingly.'''
num1 = int(input("Please enter the first Number: "))
num2 = int(input("Please enter the second Number: "))
choice = input("Enter the operator: '+', '-', '/', '*' : ")
def add(p, q):
    return p + q
def subtract(p, q):
    return p - q
def multiply(p, q):
    return p * q
def divide(p, q):
    return p / q
if choice == "+":
    print("The sum of the numbers are: ",add(num1, num2))
elif choice == "-":
    print("The difference of the numbers are: ",subtract(num1, num2))
elif choice == "*":
    print("The product of the numbers are: ",multiply(num1, num2))
elif choice == "/":
    print("The quotient of the numbers are: ",divide(num1, num2))
else:
    print("Please enter a valid operator '+', '-', '/', '*'.")


