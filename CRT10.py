n=int(input())
if (n % 2 == 1):
    ptint(f"Weird")
else:
    if 2 <= n <= 5:
        print("not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Weird")        