l1=(input("Enter the string: ")).split()
print(l1)
l2=[]
result=['a','e','i','o','u' ]
for each_value in l1:
    if each_value in result:
        print("we found the vowel", each_value)
        l2.append(each_value)
print("Number of volwes ", len(l2))
