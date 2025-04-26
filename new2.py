'''
import json

x = '{"name": "gauri" , "age":21 , "city" : "new york"}'

y = json.loads(x)
print(y["age"])
'''
'''
import json
x = { "name": "gauri" , "age":21 , "city" : "new york"}
y = json.dumps(x)

print(y)
'''
'''
import json

print(json.dumps({"name": "gauri", "age": 21}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(56))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''

import json

x = {
  "name": "gauri",
  "age": 21,
  "married": True,
  "divorced": False,
  "children": ("ritvik","varnika"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(json.dumps(x,indent = 4))
print(json.dumps(x,indent = 4,separators=(".","=")))
print(json.dumps(x,indent = 4 , sort_keys=True))
