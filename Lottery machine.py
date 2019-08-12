#Lottery machine
import random

num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))
num3=int(input("Enter your third number : "))
num4=int(input("Enter your foth number : "))
num5=int(input("Enter your fifth number : "))

X=[num1,num2,num3,num4,num5] #Users number list
Y=[]# Random Numbers List
Z=[]# Matched Numbers List

print("Your Numbers : ",X)

#make 5 rondom numbers
for i in range (5):
    Y.append(random.randrange(1,50,2))

print("Lottery Numbers : ",Y)

#Numbers Matching 
def match(x):
    if X[x]==Y[x]:
        Z.append(X[x])

match(0)
match(1)
match(2)
match(3)
match(4)

print ("You have",len(Z),"Matches")
