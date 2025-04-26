'''def a(rows):
    for i in range(1, rows + 1):
        print('*' * i)


rows = 5
a(rows)



def centered_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

# Example Usage
rows = 5
centered_pyramid(rows)



def number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example Usage
rows = 5
number_pyramid(rows)



def centered_number_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        print(spaces + numbers)

# Example Usage
rows = 5
centered_number_pyramid(rows)
'''


"""def a(b):
    for i in range(1,b+1):
       print('*'* i)
    return(b)   

a(5)

def a(b):
    for i in range(b,0,-1):
       print('*'* i)
    return(b)   

a(5)
"""
'''
def a(b):
        :
        x=' '*(b-i)
        y='*' * (2*i-1)
        print(x+y)

a(10)


'''
