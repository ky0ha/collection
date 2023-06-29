#进制转换器
import sys
def tenton():
    n=int(input('输入要转换的数.'))
    m=input('转换的进制.')
    m=int(m)
    f=''
    i=0
    if m==16:
        while n>0:
            i=n%m
            if i==10:
                i='A'
            elif i==11:
                i='B'
            elif i==12:
                i='C'
            elif i==13:
                i='D'
            elif i==14:
                i='E'
            elif i==15:
                i='F'
            n=n//m
            f=f+str(i)
        l=len(f)
        v=''
        for x in range(l):
            v=v+f[l-1]
            l-=1
        print(v)
    if m!=16:
        while n>0:
            i=n%m
            n=n//m
            f=f+str(i)
        l=len(f)
        v=''
        for x in range(l):
            v=v+f[l-1]
            l-=1
        print(v)



def ntoten():
    n=input('输入要转换的数.')
    m=input('输入的数的进制.')
    m=int(m)
    l=len(n)
    i=0
    v=l-1
    p=0
    for x in range(l):
        if int(n[l-1])>=m:
            print('输入的数字不能大于或等于进制数!')
            sys.exit()
        else:
            l-=1
    l=len(n)
    if m==16:
        for x in range(l):
            hex_mapping = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
            if n[v] in 'ABCDEF':
                i=i+hex_mapping[n[v]]*m**p
            else:
                i=i+int(n[v])*m**p
            p+=1
            v-=1
        print(i)
    elif m!=16:
        for x in range(l):
            i=i+int(n[v])*m**p
            p+=1
            v-=1
        print(i)
        

a=input('n进制转十进制还是十进制转n进制（n转十添1，十转n添2）.')
if a=='1':
    ntoten()
elif a=='2':
    tenton()
