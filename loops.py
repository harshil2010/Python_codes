'''
l=[1,2,3,4,4,5,6]
l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)
print(l1)

l=["harshil", "shyam", "vihar", "vishva", "krupali"]
l1=[]
for i in l:
    print(i)
    l1.append(i.upper())
print(l1)
'''

l=[1,2,3,4,4,"harshil", "shyam", 254, 34.26, "abc"]
l1_num=[]
l2_str=[]
for i in l:
    if type(i)==int or type(i)==float :
        l1_num.append(i)
    else:
        l2_str.append(i)
print(l1_num)
print(l2_str)