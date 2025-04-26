import re

txt = "The rain in Spain 65"
x = re.search("^The.*Spain$", txt)
y = re.findall("[a-m]", txt)
z = re.findall("\d", txt)
a = re.findall("^hello", txt)

if a:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

if x:
  print("YES! We have a match!")
else:
  print("No match")

print(y)
print(z)