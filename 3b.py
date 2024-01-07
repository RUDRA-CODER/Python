a = int(input("Enter Value of a:"));
b = int(input("Enter Value of b:"));
c = int(input("Enter Value of c:"));

if a>b and b>c:
    print("THIS NUMBER " + str(a) + " IS GREATER")
elif b>a and b>c:
    print(f"THIS NUMBER {b} IS GREATER")
else :
     print(f"THIS NUMBER {c} IS GREATER")