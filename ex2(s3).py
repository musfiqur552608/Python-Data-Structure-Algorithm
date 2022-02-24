def calculate():
    return sum([i for i in range(100) if i % 5 == 0 or i % 7 == 0])
 
 
print(calculate())