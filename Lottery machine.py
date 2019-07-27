import random

num1=int(input("Enter Your First Number : "))
num2=int(input("Enter Your Second Number : "))
num3=int(input("Enter Your Third Number : "))
num4=int(input("Enter Your Foth Number : "))
num5=int(input("Enter Your Fifth Number : "))


X = [num1,num2,num3,num4,num5]
Y = []
Z = []

print("Your Number are ",X)

for i in range (5):
    Y.append(random.randrange(1,5,2))

print("Lott Numbers ",Y)

def match(i):
    if X[i]==Y[i]:
        Z.append(X[i])

match(0)
match(1)
match(2)
match(3)
match(4)

print("You Have ",len(Z)," Matches")
    
