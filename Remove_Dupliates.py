print("Try programiz.pro")
word='aabbbcccdeeeffhg'
lst=[]
for each in word:
    if each in lst:
        continue
    else:
        lst.append(each)
        
print(lst)
