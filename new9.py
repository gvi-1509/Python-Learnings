#Count the number of vowels and consonants in a string.

def a(b):
    vowels="aeiouAEIOU"
    count=0
    count_c=0

    for char in b:
        if char in vowels:
          count +=1

        else:
           count_c +=1

    print(f"vowels = {count}")
    print(f"consonants = {count_c}")
    # return count
c = str(input("Enter string--"))
a(c)
