class Validateage(Exception):
    def __init__(self,msg):
        self.msg=msg

def Validaeteage(age):
    if age<0:
        raise Validateage("age is in negative ")
    elif age>200:
        raise Validateage("age is very very high ")
    else:
        print("age is valid ")

try:
    age = int(input("enter the age:- "))
    Validaeteage(age)
except Validateage as e:
    print(e)