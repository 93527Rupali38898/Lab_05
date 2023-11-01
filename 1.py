N = int(input("Enter a positive integer between 1 - 20:"))
if N < 1 or N > 20:
    print("Invalid input")
else:
    i = 1
    while i<= N:
        f = 1
        while f <= 20:
            print(i, "x", f, "=", i*f)
            f += 1
        i+= 1