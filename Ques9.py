# Q3.Write a python script to check whether the year is a Leap year or Non Leap year?
a=int(input("Enter a Year :"))
if a%400==0:
    print("Leap Year")
elif a%100!=0 and a%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")
