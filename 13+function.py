
def greet():
    print("Hello World")

greet()

def fuct1():
    print('hello my function  1')

def funt2():
    print('hello my function  2')

def funt3():
    print('hello my function  3')

fuct1()
funt2()
funt3()


def add(a,b):
    return a+b

add(1,2)

def greet(name):  # prameyr funtion name is prametr
    print("Hello", name)

greet("Rahul")


def add(a, b):
    return a + b  # return result back to funct

result = add(10, 20)

print(result)

# type of argumnt

def student(name, age):
    print(name, age)

student("Rahul", 25)


def student(name, age):
    print(name, age)

student(age=25, name="Rahul")

def total(*numbers):  # argumnt 
    print(sum(numbers))

total(10,20,30)

def info(**data): # kword arugmnt
    print(data)

info(name="Rahul", age=25)


def test():
    x = 10  # local vriabl
    print(x)

test()


x = 100  # globl vriable

def test():
    print(x)

test()