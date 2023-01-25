# Q11.Write a pyhton script to take the month value in numeric Format and display the number of days in it ?
a=int(input('Enter Month Number :'))
if a in (1,3,5,7,8,10,12):
    print('31 Days')
elif a in (4,6,9,11):
    print('30 Days')
elif a==2:
    print('28 or 29 Days')
else:
    print('Enter a Valid Month')