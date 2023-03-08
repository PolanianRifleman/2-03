a = input("What is your name? ")
y = int(input("What is your age? "))
z = input("Have you had a birthday this year? ")

def function():
    if z == "yes":
        u = 2023-y
        o = "You were born in "+str(u)+" and your name is "+str(a)
    else:
        i = 2022-y
        o = "You were born in "+str(i)+" and your name is "+str(a)
    return o

print(function())