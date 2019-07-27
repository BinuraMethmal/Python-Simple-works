#Leap Year Finder

year=int(input("Enter the year, "))

x= year % 4
y= year % 100
z = year % 400

if z==0:
    print(year," is a leap year.")

elif x==0 and y!=0:
    print(year," is a leap year.")

else:
    print(year," is not a leap year.")
