import json
f1=open('concept.json','r',encoding='utf-8')
f2=open('1.json','w',encoding='utf-8')
d={}
lst=[]
for i in f1.readlines():
    s=i.strip()
    print(s)
    j=0
    d={}
    while j<len(s):
        # 3 15
        if s[j:j+9:]=='conceptId':
            j=j+13
            tmp=''
            while s[j]!='"':
                tmp+=s[j]
                j=j+1
            d['conceptId']=tmp
            #print(tmp)
        if s[j:j+4:]=='name':
            j=j+8
            tmp=''
            while s[j]!='"':
                tmp+=s[j]
                j=j+1
            #print(tmp)
            d['name']=tmp
        if s[j:j+3:]=='isA':
            j=j+6
            tmp=''
            while s[j-3]!=']' and s[j-4]!=']':
                tmp+=s[j]
                j=j+1
            tmp=tmp[:-1:]
            flag=0
            t=''
            l=[]
            for i in tmp:
                if i =='"':
                    flag+=1
                    if flag==1:
                        t=''
                    elif flag==2:
                        l.append(t)
                    elif flag==3:
                        t=''
                    elif flag==4:
                        l.append(t)
                    else:
                        break
                elif t==',':
                    pass
                else:
                    t=t+i
            l.append('')
            d['isA']=[l]
            print(d['isA'])
        if s[j:j+11:]=='description':
            j=j+15
            tmp=''
            while s[j]!='"':
                tmp+=s[j]
                j=j+1
            #print(tmp)
            d['description']=tmp
        j=j+1
    f2.write(json.dumps(d, ensure_ascii=False) + '\n')
    print('****************************')