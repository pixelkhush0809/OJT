num = int(input("Enter a number: "))
sign = -1 if num < 0 else 1
num = abs(num)
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number =", sign * rev)