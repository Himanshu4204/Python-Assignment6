# Q10.Write a python script to print greater among three numbers. Print number only once
#  even if the numbers are the same.?
print("Enter Three Number :")
a,b,c=int(input()),int(input()),int(input())
print('Greater is',(a if a>c else c) if a>b else (b if b>c else c))

