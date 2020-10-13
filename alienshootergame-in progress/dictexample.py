f=open('example.txt')
dict={}
for lines in f:
    data=lines.rstrip().split(',')
    name=data[0]
    regno=data[1]
    month=data[3]

