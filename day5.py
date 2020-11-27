num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
#addition of two numbers
def add_num(a,b):
    sum =   a+b;
    return sum;
print("The addition of two number is",add_num(num1,num2))
#subraction of two numbers
def sub_num(a,b):
    sub =   a-b;
    return sub;
print("The subraction two number is",sub_num(num1,num2))
#multiplicatin of two numbers
def mul_num(a,b):
    mul =a*b;
    return mul;
print("The multiplication of two number is",mul_num(num1,num2))
#divison of two nummber
def div_num(a,b):
    div =   a//b;
    return div;
print("The division of two number is",div_num(num1,num2))


#create a function covid()it should accept patient name & body temperature
def covid(patient_name,body_temperature):
    print("covid satatement:"+patient_name+","+body_temperature)

covid('ram','98 degree')


def covid(patient_name)
print("Body temperature of the patient:"+body_temperature+"")
