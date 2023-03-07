a = input("What is your name? ")
y = int(input("What is your age? "))
z = input("Have you had a birthday this year? ")

def function():
    if z == "yes":
        u = 2023-y
        print("You were born in",u,"and your name is",a)
    else:
        i = 2022-y
        print("You were born in",i,"and your name is",a)

function()