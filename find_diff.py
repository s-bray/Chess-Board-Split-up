

import string
file = open("val_1.txt", "r")
data = file.read()
words = data.split()
length=int(len(words)/2)
l1=[]
l1=[words[i] for i in range(len(words)) if (i%2!=0)]


file = open("val_2.txt", "r")
data = file.read()
words = data.split()
length=int(len(words)/2)
l2=[]
l2=[words[i] for i in range(len(words)) if (i%2!=0)]

l3=[(int(l2[i])-int(l1[i])) for i in range(len(l1))]

p=0;
while p!=64:
    with open('values_diff.txt', 'w') as file:
        for k in range(0,8):
            for j in range(1,9):
                file.write(string.ascii_lowercase[k]+str(j)+".jpg"+"  %i\n" % l3[p])
                p=p+1
                


