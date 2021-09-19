
import json
f=open('data.json','r',encoding='utf-8')
l=[]
for i in f.readlines():
    dic=json.loads(i)
    l.append(dic)
name=[]
zf=[]
for i in l:
    name.append(i['name'])
    s=''
    if '性别' in i.keys():
        s+='        <untitled-ontogogy-25:性别>'+str(i['性别'][0][0])+'<untitled-ontogogy-25:性别>\n'
    if '生日' in i.keys():
        s+='        <untitled-ontogogy-25:生日>'+str(i['生日'][0][0])+'<untitled-ontogogy-25:生日>\n'
    elif '出生日期' in i.keys():
        s+='        <untitled-ontogogy-25:出生日期>'+str(i['出生日期'][0][0])+'<untitled-ontogogy-25:出生日期>\n'
    if '查克拉属性' in i.keys():
        s+='        <untitled-ontogogy-25:查克拉属性>'+str(i['查克拉属性'][0][0])+'<untitled-ontogogy-25:查克拉属性>\n'
    if '身高' in i.keys():
        s+='        <untitled-ontogogy-25:身高>'+str(i['身高'][0][0])+'<untitled-ontogogy-25:身高>\n'
    if '体重' in i.keys():
        s+='        <untitled-ontogogy-25:体重>'+str(i['体重'][0][0])+'<untitled-ontogogy-25:体重>\n'
    if '血型' in i.keys():
        s+='        <untitled-ontogogy-25:血型>'+str(i['血型'][0][0])+'<untitled-ontogogy-25:血型>\n'
    zf.append(s[8:-1:])
d=dict(zip(name,zf))
s=input()
while s!='0':
    if s in d.keys():
        print(d[s])
    else:
        print('Not Found!')
    s=input()

