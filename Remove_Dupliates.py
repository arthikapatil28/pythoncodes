word='aabbbcccdeeeffhg'
lst=[]
for each in word:
    if each in lst:
        continue
    else:
        lst.append(each)
print(lst). #['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g']
output=' '.join(lst)
print(output) #a b c d e f h g
