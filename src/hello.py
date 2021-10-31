#Read two float numbers from user and perform arithmetic operations (+, -, *, /, //, %,**).
a=float(input("Enter the first number :"))
b=float(input("Enter the second number :"))
print("ADDITION :",a+b)
print("SUBSTRACT :",a-b)
print("MULTIPLICATION :",a*b)
print("DIVISION:",a/b)
print("MOD:",a%b)
print("RAISE TO",a**b)
print("FLOOR DIVISION",a//b)
print()

# Read two integers from user and perform Bitwise operations (&, |, ^, ~, <<, >>).
c=int(input("Enter the first  number :"))
d=int(input("Enter the second  number :"))
print("c and d",c & d)
print("c OR d",c | d)
print("c NOT d", ~d)
print("c EOR d",c ^ d)
print("BITWISE RIGHT shift ",c >> d)
print("BITWISE LEFT shift ",c << d)
print()

#Read two complex numbers from user and perform its addition.
e=complex(input("Enter the first  number :"))
f=complex(input("Enter the second  number :"))
print("SUM :", e+f)
print()

#Read decimal number from user and convert it into octal, binary and hexadecimal number. 
g=int(input("Enter the number :"))
print("OCTAL",bin(g))
print("BINARY",oct(g))
print("HEXADECIMAL",hex(g))
print()

#Print type of each variable 
p=16
q=23.32
r="string"
s=2+3j

print(type (p))
print(type (q))
print(type (r))
print(type (s))