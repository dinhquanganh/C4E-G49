#Exercise 1
inventory= {'gold' : 500,'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']}
inventory['pocket']= 'seashell','strange berry','lint'
del inventory['backpack'][1]
print(inventory)

#Exercise 2
price={'banana':4,'apple':2,'orange':1.5,'pear':3}
stock={'banana':6,'apple':0,'orange':32,'pear':15} 
x=['banana','apple','orange','pear']
for i in range(len(x)):
    print('-',x[i])
    print('  price',price[x[i]])
    print('  stock',stock[x[i]])
tong=0
for i in range(len(x)):
    a=price[x[i]]*stock[x[i]]
    tong=tong+a
    print(x[i],': ',a)
print(tong)


#Exercise 3
tl=['35','36','40','44']
print('If x=8, then what is value of 4(x+3)')
for i in range(len(tl)):
    print(i+1,'. ',tl[i])
a=int(input('Your choice: '))
x=0
for i in range(4):
    if a==4:
        print('True')
        x+=1
        break
if x==0 :
    print('False')

#
tl=['35','36','40','44']
print('If x=8, then what is value of 4(x+3)')
for i in range(len(tl)):
    print(i+1,'. ',tl[i])
a=int(input('Your choice: '))
x=0
for i in range(4):
    if a==4:
        print('True')
        x+=1
        break
if x==0 :
    print('False')
print('Jack score these marks in 5 math test: 49,81,72,66 and 52. What is mean? ')
tl1=['About 55','About 65','About 75','About 85']
for i in range(len(tl1)):
     print(i+1,'. ', tl1[i])
a=int(input('Your choice: '))
for i in range(4):
    if a==2:
        print('True')
        x+=1
        break
if x==1 :
    print('False')
print('You correct answer ',x,'out of 2 questions')






#tl=['35','36','40','44']
print('If x=8, then what is value of 4(x+3)')
for i in range(len(tl)):
    print(i+1,'. ',tl[i])
a=int(input('Your choice: '))
x=0
for i in range(4):
    if a==4:
        print('True')
        x+=1
        break
if x==0 :
    print('False')


#Viết chương trình thực hiện thuật toán nén chuối:
a=input('Nhap day can nen: ')
x=a
for i in range(len(a)):
    d=0
    for j in range(len(x)):
        if a[i]==x[j]:
            print(a[i],end=' ')
            print(x[j])
            d+=1
    if d>0:
        print(a[i],'[',d,']',end='')


s='abccccabdeeeeef'
i=0
j=i+1
while i<len(s):
    a=0
    while j<len(s):
        if s[j]==s[i]:
            j+=1
            a+=1
        else: 
            print(s[i],end='')
            break
    i=i+a
    if a>0:
        print(s[i],'[',a,']',end='')
    







        
