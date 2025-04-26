#Write a Python program to check if a given number is odd or even.
'''

a = int(input("Enter a number: "))
if a % 2 == 0:
    print("even")
else:
    print("odd")
    '''
#Write a program that prints numbers from 1 to 100. For multiples of 3, print "Fizz";
#  for multiples of 5, print "Buzz"; and for multiples of both, print "FizzBuzz".

'''x = range(1,101)
for i in x:
  print(i)
if i % 3 == 0 & i % 5 == 0 :
  print ("fizzbuzz ")
elif i % 5 == 0:
  print("buzz")
elif i % 3 == 0:
  print("fizz")

'''
#Write a Python function to check if a string is a palindrome.
'''
a = str(input("put string value:-"))
if a == a[::-1]:
    print("is palindrome")
else:
    print("not a palindrome")
'''
#Write a program that takes a list of numbers and returns the largest number.

'''a = range(21)
b = max(a)
if  b > 19:
    print({b})
'''

#Create a program that takes a temperature in 
#Fahrenheit and converts it to celsius.

'''def a(b):
  c=(b-32)*(5/9)
  return(c)
b=float(input ("Enter temprature:-"))

print(a(b))
'''
#takes a temperature in Celsius and converts it to Fahrenheit.

'''def a(b):
  c=(b*(9/5)+32)
  return(c)
b=float(input ("Enter temprature:-"))

print(a(b))
'''

#Write a Python program to find the factorial of a number.
'''
from math import factorial

result = factorial (int(input("enter num:-")))
print(result)
'''
##Write a function to count the number of vowels in a given string.

def a(b):
    vowels="aeiouAEIOU"
    count=0

    for char in b:
        if char in vowels:
          count +=1
    
    return count

c = str(input("Enter string--"))

print(a(c))

#Write a Python program to generate the Fibonacci sequence up to a given number.

'''def a(n):
    f=[]
    x,y=0,1

    for i in range(n):
        f.append(x)
        x,y=y,x+y

    return f

n = int(input("enter number:-"))
print(a(n))'''






