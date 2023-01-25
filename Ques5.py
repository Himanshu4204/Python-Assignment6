# Q5. Write a python script to print given Words in Dictionary Order?
print('Enter Two Words :')
a,b=input(),input()
print((b,a) if a>b else (a,b))
