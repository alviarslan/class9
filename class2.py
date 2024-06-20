#PYTHON WRITING COMMENTS-

#this is single line comment
print("hello world")

""" 
this is comment
this is comment
this is comment
this is comment
"""

print("hello world")

#PYTHON DECLARING VARIABLES-

x=5
y= "John"
print(x)
print(y)
print(5000+500+50+5)

#x=5 ; y=500 ; z=5000 ; p=50 (if we want to declare variable in single line)

x=5
y=500
z=5000
p=50
print(x + y)
print(x + y + z)
print(x + y + z + p)

# how we declare variables
myvar= "Alvi"
MYVAR= "Alvi"
_myvar= "Alvi"
_my_var= "Alvi"
myVar= "Alvi"
Myvar1= "Alvi"

""" how we can't declare variables & why..
1myvar= "Alvi" (no numbers can be used at front)
my var= "Alvi" (no space can be used)
my-var= "Alvi" (- can not be used)
"""

name='Alvi' ; name2="Arslan" ; name3="'Mir'" #(alphabatic variables must be declared inside '')
print(x + y , name)
print(x + y + z , name2)
print(name)
print(name2)
print(name3) #(in triple quotation, it will print with single quotation)
print('name') #(it will print what is written inside quotation)

x , y , z = 'banana' , 'mango' , 'orange' #(variables can be declared like this too)
print(x)
print(y)
print(z)

# DECLARING GLOBAL & LOCAL VARIABLES-
x='awsome'
def myfunc(): #(local function heading)
    x= 'fantastic'
    print("python is " +x)
myfunc() #(local function closing)

print("python is " +x)


def myfunc():
    global x #(how we can declare global variable inside function)
    x= 'fantastic'
myfunc()

print("python is "+x)


 #PYTHON DATA TYPES-
x= "hello world"
y= 1000 
z= 10.10
p= 100j

#(to check the data type we write 'type')
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
print(p)
print(type(p))