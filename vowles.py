l1=(input("Enter the string: "))
l1.split()
print(l1)
l2=[]
result=['a','e','i','o','u' ]
for each_value in l1:
    if each_value in result:
        #print("we found the vowel", each_value)
        l2.append(each_value)
print("Number of volwes ", len(l2))


l1=(input("Enter the string: "))
l1.split()
result=['a','e','i','o','u' ]
wcount=0
for i in range(0, len(l1)):
    if l1[i] in result:
        wcount += 1
print("Number of volwes ",wcount)
