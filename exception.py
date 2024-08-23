import sys

try: 
    x = int(input("x : "))
    y = int(input("y : "))
except ValueError:
    print("Entered wrong value")
    sys.exit(1)
    

try:
    division = x / y
except ZeroDivisionError:
    print("Cannot divide a number with 0")
    sys.exit(1)

print(division)