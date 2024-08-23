import sys

try: 
    x = int(input("x : "))
    y = int(input("y : "))
except ValueError:
    print("Entered wrong value")
    sys.exit(1)
    
    

division = x / y

print(division)