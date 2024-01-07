n = int(input("Enter a number which you want to find factorial:"));
fact = 1

if n ==0:
    print("factorial is 1")

for i in range(1,n+1):
    fact = fact*i
    if n == 0:
        break
    print(fact)