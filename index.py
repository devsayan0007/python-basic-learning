# How to Build a Simple Calculator in Python
print('''
      + Add
      - Subtract
      * Multiply
      / Divide''')
num1 = float(input("Enter 1st Value "))
num2 = float(input("Enter 2nd Value "))
opr = input("Enter the Operator ")

if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("Invalid Option")