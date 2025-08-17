# pythoncodes
Codes during practice


################################################################
Average of 3 number: 
number=[int(x) for x in input("enter the 3 number seperated by sapce: ").split()]
print(number)
average=sum(number)//len(number)
print(average)

################################################################
Area of circle: #A=πr2
pie=3.14
radius=float(input("Enter the radius of the circle: "))
Area=radius**2 * pie
print(Area).

################################################################
#A=πr2
import math
radius=float(input("Enter the radius of the circle: "))
Area=math.pi*radius**2 
print(Area) 
################################################################
 EVEN or ODD: 
number=int(input("enter the numbers:"))
print(number)
if (number%2 == 0):
    print("The number is EVEN ")
else:
    print("The number is ODD ")

################################################################
****function to check what spacer tab*****
import re
def isWhiteLine(input1):
    pattern=r'^[\t]*$'
    return bool(re.fullmatch(pattern, input1))
user_input=input("Enter the string: ")
if isWhiteLine(user_input):
    print("True")
else:
    print("False")


################################################################
******grading system**** 
maths=int(input("enter the marks: "))
science=int(input("enter the marks: "))
social=int(input("enter the marks: "))
if maths>35 and science>35 and social>35:
    total=[]
    total.append(maths)
    total.append(science)
    total.append(social)
    TotalMarks=sum(total)
    print(TotalMarks)
    average_marks=TotalMarks/len(total)
    print("Average of your marks is: " , average_marks)
    if (average_marks<=59):
        print("Your Grade is : C " )
    elif (average_marks<=69 and average_marks>59):
        print("Your Grade is : B " )
    else:
        print("Your Grade is : A " )
else:
    print("Oops!! you failed the Exam.")

################################################################

********print 1 to 20 ********** 
x=1
while(x<=20):
    print(x)
    x+=1  
################################################################ 
Print odd numbers between the given 2 numbers

MIN_number=int(input("enter the number:"))
MAX_number=int(input("enter the number:"))
print(f"The ODD numbers between the range of {MIN_number} and {MAX_number} are")
i=MIN_number
while(i<=MAX_number):
    if (i%2!=0):
        print("The ODD numbers between the range are : ", i)
    else:
        i=+1
    i+=2

 ################################################################

Table of given number:  
Table_number=int(input("Enter the number : "))
x=Table_number
i=0
for i in range(0,11):
    y=x*i
    print(f" {x} * {i} = {y} ")
    i+=1

 ################################################################

Break if 5 is in the list:

number=[int(x) for x in input("enter the 3 number seperated by space: ").split()]
print(number)
for i in number:
    if i==5:
        break
    print(i)

 ################################################################

Continue  and skip multiple of 3

number=[int(x) for x in input("enter the 3 number seperated by sapce: ").split()]
print(number)
for i in number:
    if (i%3==0):
        continue
    print(i)


 ################################################################
 ################################################################
 ################################################################
 ################################################################
