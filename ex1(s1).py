def calculate():
    sum = 0
    for i in range(0,100):
        if i%5==0 or i%7==0:
            sum = sum + i
    return sum

print(calculate())