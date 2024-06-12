a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
modulus = a
while modulus >= b:
    modulus -= b
print("The modulus of", modulus)