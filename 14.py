def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    quotient = 0
    sign = -1 if (a < 0) ^ (b < 0) else 1
    a, b = abs(a), abs(b)
    while a >= b:
        a -= b
        quotient += 1
    return sign * quotient
result = divide(-11,2)
print("The result is:", result)
