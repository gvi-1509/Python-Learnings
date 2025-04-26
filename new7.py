#return function
'''def add(y):
    x = 10
    c = x+y
    d=y-x

    return c,d,50

sum,sub,a=add(20)
print(sum)
print(sub)
print(a)'''


#nested function

'''def disp(st):
    def show():
        return "show function"
    result = show() + st + "disp function"

print(disp("Gauravi"))  '''  

#pass function 

'''def disp(sh):
    return "disp function"+ sh()
def show():
    return "show function"

result = disp(show)
print(result)'''


#function return another function

def disp():
    def show():
        return "show function"
    print("disp function")
    return show

r_sh = disp()
print(r_sh())

#lambda function

# add_sub = lambda x,y : (x+y,x-y)
# a,s,= add_sub(5,2)
# print(a)
# print(s)