import pandas as pd

#Firstly upload files in  a  = questions be like notpad and questions were typed in one by one
#Secondly upload files in b = answers were typed in one by one

a = []
file1 = open("question1.txt",'r')
for i in range(10):
    s = file1.readline()
    s = s.replace(",\n","")
    a.append(s)   
print(a)



b = []
file1 = open("answer2.txt",'r')
for i in range(10):
    s = file1.readline()
    s = s.replace(",\n","") 
    b.append(s)    
print(b)

c = pd.DataFrame(b,index=[a])
print(c)
c.to_csv("datas.csv")
 