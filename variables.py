#varibales are containers that stores the data or value..you don't need to declare a variable type explicitly
ec2_instance_name="cloud_practitioner"
print(ec2_instance_name)

#Global variables
#A global variable is declared outside any function and is accessible from anywhere in the program.
a=10
b=5
def add():
    c=a+b
    print(c)
def mul():
    d=a*b
    print(d)
add()
mul()

#local variables
#defined inside a function and can only access within that function. Can't be accessed outside the  function

def sub():
    a1=20
    print(a1-a)
def div():
    print(a1/b)   #error
sub()
div()