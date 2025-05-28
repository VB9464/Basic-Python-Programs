# Method 1: Using tuple unpacking (recommended)

a , b = 5 , 10   # here we declare variables 

a , b = b , a      # then here the swaping is done

print("a=" , a)
print("b=" , b)

# Method 2: Using a temporary variable

a , b = 1 , 2

temp = a   # Step 1: Store a into temp, Now temp = 5
a = b      # Step 2: Assign b to a ,Now a = 10
b = temp   # tep 3: Assign temp (original a) to b , Now b = 5

print("a =",a)
print("b =",b)

# Method 3: Using arithmetic operations (not recommended for readability and precision)

a , b = 10 ,20

a = a + b
b = a - b
a = a - b

print("a =",a)
print("b =",b)
