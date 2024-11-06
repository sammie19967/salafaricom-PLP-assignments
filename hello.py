

num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the Second Number: "))

num3 = 0

print(f" value for num1:  {num1} and num2:  {num2} before exchange")

num3 = num1
num1 = num2
num2 = num3

print(num1,num2)
print(f" value for num1:  {num1} and num2:  {num2} exchanged")
