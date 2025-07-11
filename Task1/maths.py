a = int(input("Enter First Number:\n"))
b = int(input("Enter Second Number:\n"))

sum = a + b
print("Sum is:\n",sum)

# Absolute difference
if a > b:
    diff = a - b
else:
    diff = b - a
print("Difference is:\n",diff)

# Multiplication
if a == 0 or b == 0:
    mult = 0
else:
    mult = a * b
print("Product is:\n",mult)

# Division
if b != 0:
    div = a / b
    div1 = a // b
    div2 = a % b
else:
    print("Division is invalid!")
print("Value with decimal is:\n",div)
print("Value is:\n",div1)
print("Mod value is:\n",div2)