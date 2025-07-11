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
