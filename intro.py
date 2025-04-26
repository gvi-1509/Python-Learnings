# print("hello world!")

#if(5>2):
  # print("Five is greater than two")
"""
if 5 > 2:
 print("Five is greater than two!")
 print("Five is greater than two!")
"""
"""
a=5
b="Gauravi"

print(type(a))
print(b)
"""
"""
a,b="old","young"
print(a)
#print(b)
"""
"""
fruits=("pineapple","berries","grapes","mango")
(a,*b,c,d)= fruits

print(a)
print(b)
print(c)
print(d)
"""
"""
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

fruits=("pineapple","berries","grapes","mango")
for i in range(len(fruits)):
  print(fruits[i])

  """
"""
tuple1=('a','b','c','c','b','a')
tuple2=("pineapple","berries","grapes","mango")

tuple3=tuple1+tuple2
#print(tuple3)
z=tuple1.count('a')
print(z)

"""
'''
set = {"apple", "banana", "cherry","grapes","mango"}
set2= {"pineapple","berries","grapes","mango"}
#print("banana" not in set)
set.add("grapes")
'''

#set.copy
#set.difference
#set.difference_update(set2)
#set.discard("banana")
#set.intersection(set2)
#set.intersection_update(set2)
#z=set.issubset(set2)
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference_update(y)

print(z)
"""
"""
thisdict = {
  "brand": "mochi",
  "model": "shoes",
  "year": 2000
}

if "year" in thisdict:
   print("Yes, 'year' is one of the keys in the thisdict dictionary")
"""
#print(thisdict["brand"])
#print(len(thisdict))
#print(type(thisdict))

#y=thisdict["year"]

#y=thisdict.get("model")
"""
y= thisdict.keys()
#before change
print(y)

thisdict["color"]="brown"
print(y)
""""""
y=thisdict.values()
print(y)
thisdict["year"]=2020
print(y)
"""
'''
myfamily = {
  "child1" : {
    "name" : "gvi",
    "year" : 2004
  },
  "child2" : {
    "name" : "pagu",
    "year" : 2007
  },
  "child3" : {
    "name" : "eshu",
    "year" : 2011
  }
}
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
'''
'''
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)
'''
'''
a = 33
b = 35
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
'''
'''
a = 500
b = 33
c= 95
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  '''
'''
if a > b and c > a:
  print("both conditions are true") 

'''
'''
x = 51

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
'''
'''
a = 99
b = 500

if b > a:
  pass
'''
'''
i = 1
while i < 10:
  print(i)
  i += 1
'''
'''
i = 1
while i < 10  :
  print(i)
  if i == 5:
    break
  i += 1
'''
'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
'''
'''
i = 1
while i < 10:
  print(i)
  i += 1
else:
  print("i is no longer less than 10")
'''
'''
def my_function(fname):
  print(fname + " Pal")

my_function("Gauri")
my_function("Manish")
my_function("Shreyash")

'''
'''
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("gauri", "manish", "shreyash")

'''
'''
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
'''
