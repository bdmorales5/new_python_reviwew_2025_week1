#
#variables are used tp store data values
x= 15 #integer
y= 3.14 #float
name= "brandon" # string
#a letter is a list of characters in
#quotation makrs
is_student= True  #boolean true or false 
#print the values of the variables 
print(x)
print(y)
print(name)
print(is_student)
#place in sentence without f-strings
print(" my name is " + name + " , i am " + str(x) + " years old. ")
#the plus sign (+) is used to concatenaye strings
#str(x) converts the integer x to a srting
#type()function returns the type of a variable 
print(type(x))      #<class 'int'>
print(type(y))      #<class 'float'>
print(type(name))    #<class 'str'>
print(type(is_student))     #class 'bool'>

#lets practice
a=10
b=2.5
c="bob"
d=False 

print(" my name " + c + " , i am " + str(a) + " years old ")
#print the values of the new variables in a sentence
#using concatenation


#using the f string method

print(f" my name is {c} , i have {a} apples.")
