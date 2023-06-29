#进制转换器
import sys
def tenton():
    n=int(input('输入要转换的数.'))
    m=int(input('转换的进制.'))
    f=''
    i=0
    if m==16:
        while n>0:
            i=n%m
            if i>=10:
                i = "ABCDEF"[i%10]
            n=n//m
            f=str(i)+f
        print(f)
    if m!=16:
        while n>0:
            i=n%m
            n=n//m
            f=str(i)+f
        print(f)



def ntoten():
    n=input('输入要转换的数.')
    m=int(input('输入的数的进制.'))
    l=len(n)
    i=0
    v=l-1
    p=0
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