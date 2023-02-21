a=int(input("Enter value"))
b=int(input("Enter value"))
p=int(input("enter value"))
r=int(input("Enter value"))
t=int(input("Enter value"))
n=int(input("Enter value"))
def add(a,b):
     return a+b
 
def sub(a,b):
     return a-b
 
def multi(a,b):
     return a * b
 
def div(a,b):
     return a / b
 
def si(p, r, t):
    return (p*r*t) / 100
 
def ci(p, r ,t):
    return p * pow((1 + r/100), t)
 
def sqr(n):
    return n**2
 
def sqrt(n):
    return n**0.5
 
print(add(a,b))
print(sub(a,b))
print(multi(a,b))
print(div(a,b))
print(si(p,r,t))
print(sqr(n))
print(sqrt(n))