# d = {}
# type(d)
'''
d1 = {'key':"Harshil"}
print(d1)
   
d2 = {'name':"Harshil" , 'Surname':"Kathiriya", 'email_id':"hnkathiriya21@gmail.com"}  
print(d2)
print(d2['Surname'])

d3 = {True : 234}
#print(d3[True])
print(d3[1])

d4 = {'name':"Harshil", 'mail_id': "hnk@gmail.com", 'name': "hnk"}
print(d4)

d5 = {'company': "hk", 'courses': ["wd", "ds", "java"]}
print(d5)
print(d5['courses'][0])
'''
d6 = {'numbers' : [2,3,4,5,6,7], 'assignment': (1,2,3,4,5,6), 'launch_Date': {4,5,6},
      'class_time' : {'web': 6, 'ds': 7, 'java': 8}}
#print(d6['class_time']['java'])
#print(d6)
d6['mentor']=["vishal", "krish"]
#print(d6)
#del d6['numbers']
#print(d6)
#print(list(d6.keys()))
#print(list(d6.values()))
#print(list(d6.items()))
print(list(d6.pop('numbers')))
print(d6)
