# Q12. Write a python script to accept one complex number from the user and display the
#   greater number between real part and imaginary part
a=complex(input("Enter a Complex Number :"))
if a.real>a.imag:
    print('Real part is Greater')
else:
    print('Imaginary part is Greater')