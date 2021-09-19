def func(s):
    s=s.replace('</p>','')
    s=s.replace('<p>','')
    s=s.replace('</b>','')
    s=s.replace('<br>','')
    s=s.replace('<b>','')
    s=s.replace('<h2>','')
    s=s.replace('<\h2>','')
    return s
import json
f1=open('result.txt','r',encoding='utf-8')
f2=open('QA.json','a',encoding='utf-8')
q=''
a=''
l=f1.readlines()
start=int(input('从哪里开始？'))
j=start
for index in range(start,len(l)):
    i=l[index]
    j=j+1
    if j-start>30:
        break
    if len(i)>1:
        if i[0]=='Q':
            q=i[2:-1:]
        elif i[0]=='A':
            a=i[2:-1:]
    else:
        q=func(q)
        a=func(a)
        print(q)
        flag=input('Needed?  [y/n/u]  ')
        if flag=='u':
            print(a)
            flag = input('Needed?  [y/n]  ')
        if flag=='y':
            tag=input('请输入标签：')
            l1=['treelable','question','answer']
            l2=[tag,q,a]
            d=dict(zip(l1,l2))
            f2.write(json.dumps(d,ensure_ascii=False)+'\n')
        print(j,'*'*40)
f2.close()