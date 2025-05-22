number = int(input("Enter your number "))
print(number)

for i in range(1, 11):
    if i == 5:
        continue
    print(number, "x", i , "=", number*i)
