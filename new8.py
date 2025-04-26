# def greet(name):
#     print(f"hello,{name}!")

# greet("gauri")


# ----------------------------------------------------

# def say_hello(a):
#        print(a)
# say_hello("hello world!")

#---------------------------------------------------------

# def fruits(names):
#     print(f"{names}")
# fruits(str(input("enter the name of fruits=")))   
#------------------------------------------------------

# def wlcm_msg(name):
#     name = "gauri"
#     print(f"Welcome {name}!")

# wlcm_msg("name")

#-------------------------------------------------------

# def add_two_numbers(num1,num2):
#     a = num1 + num2
#     print(f"sum = {a}")

# add_two_numbers(10,56)    

#--------------------------------------------------------

# def find_square(a):
#     c = a * a
#     return c
# num = int(input("Enter a number: "))

# square = find_square(num)
# print(f"The square of the given number {num} is {square}")

#-------------------------------------------------------------------

# def multiply_by_two(a):
#     c = a * 2
#     return c
# num = int(input("Enter a number: "))

# multi = multiply_by_two(num)
# print(f"output of {num} is {multi}")

#------------------------QUESTIONS-----------------------------------------

#1 . find the maximum value from list :- l = [1, 2, 3, 1, 2]

# def value(l):
#     for i in l:
#         if i >=5:
#             print(f"maximun value = {i}")

# l = [1, 2, 90, 1, 2]
# value(l)

# 2. find sencond maximun value from list l = [1, 2, 3, 1, 2]

# def value(l):   
#     for num in range(len(l)):
#         if num < 1 :
#             print(f" second maximun value = {num}")

# l = [1, 2, 3, 1, 2]
# value(l)

#3. find minimum value from list l = [1, 2, 3, 1, 2]

# def value(l):   
#     for num in range(len(l)):
#         if num < 1 :
#             print(f" minimum value = {num}")

# l = [1, 2, 3, 1, 2]
# value(l)

#4. finnd second minimum valuefrom list l = [1, 2, 3, 1, 2]

# def value(l):   
#     for num in range(len(l)):
#         if num < 2 :
#             print(f"second  minimum value = {num}")

# l = [1, 2, 3, 1, 2]
# value(l)

#5. find dublication value form list :- l = [1, 2, 3, 1, 2]

def value(l):   
    dub = []
    for i in l:
        if i not in dub and l.count(i) > 1:
            dub.append(i)
    print(dub)

l = [1, 2, 3, 1, 2]
value(l)

#6. find target value from list :- l = [2, 4, 3, 5, 7, 8]

# def value(l):   
#     for num in range(len(l)):
#         if num == 5 :
#             print(f"target value = {num}")
# l = [2, 4, 3, 5, 7, 8]
# value(l)


#---------------------------------------------------------------------------------

# def describe_city(city, country):
#     print(f"{city} is in {country}")

# describe_city("Mumbai","India")     

# #-------------------------------------------------------------------------------------

# def order_food(main, side, drink="water"):
#     print(f"I want {main} for main ,{side} as side dish and {drink} to drink ")

# order_food("Chicken Fried Rice","Chicken 65")

# #--------------------------------------------------------------------------------------

# def even(num):
#       for num in num:
#         if num % 2 == 0:
#          print(f"{num} is even")
#         else:
#             print(f"{num} is odd")
# even([2, 4, 3, 5, 7, 8])

# #--------------------------------------------------------------------------------------------------

# def num(a):
#     print(f"Reverse order = {a[::-1]}")

# num([2, 4, 3, 5, 7, 8])

# #--------------------------------------------------------------------------------------------------

# def occurance(num):
#     a = []
#     for i in num:
#         if i not in a:
#             count = num.count(i)
#             print(f"num {i}  occurs {count} times")
#             a.append(i)

# occurance([2, 4, 3, 5, 7, 8,2, 4, 3,2, 4, 3,7, 8])            

# #---------------------------------------------------------------------------------------------------

# def dup(l):   
#     dub = []
#     for i in l:
#         if i not in dub and l.count(i) > 1:
#             dub.append(i)
#     print(dub)

# l = [1, 2, 3, 1, 2]
# dup(l)


