n = int(input("ВВедите число:"))
if n % 2 != 0:
    print("Yes")
elif 2 <= n <= 5 and n % 2 == 0:
    print("No")
elif 6 <= n <= 20 and n % 2 == 0:
    print("Yes")
elif n > 20 and n % 2 == 0:
    print("No")
