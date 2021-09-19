import json
f1=open('data.json','r',encoding='utf-8')
f2=open('img_source.json','r',encoding='gbk')
f3=open('QA.json','r',encoding='utf-8')
f4=open('1.json','r',encoding='utf-8')
f5=open('naruto_knowledge_graph.json','a',encoding='utf-8')
final_json_st={}
#######################
# 读入实体
#######################
for i in f1.readlines():
    s=json.loads(i)
    final_json_st[s['name']]=s
    final_json_st[s['name']]['resource_QA']=[]
###############################
# 根据img库生成对应字典方便提取
###############################
key=[]
img=[]
tmp=[]
for i in f2.readlines():
    s=i.strip()
    if len(s)<=2:
        continue
    if not 'https:' in s:
        img.append(tmp)
        key.append(s[1:-4:])
        tmp=[]
    else:
        tmp.append(s)
del img[0]
key_and_img=dict(zip(key,img))
###########################
# 读入图片库
###########################
for i in key_and_img.keys():
    l=[]
    for j in range(len(key_and_img[i])):
        s1=i+str(j+1)
        s2=key_and_img[i][j]
        l.append([s1,s2])
    if i not in final_json_st.keys():
        print(i)
    else:
        final_json_st[i]['resource_img']=l
###########################
# 读入问答库

###########################
for i in f3.readlines():
    s=json.loads(i)
    if not s['treelable'] in final_json_st.keys():
        print(s['treelable'])
    else:
        final_json_st[s['treelable']]['resource_QA'].append([s['question'],s['answer'],[]])
print('***********************************')
###########################
# 放到该有的概念层下
con={}
for i in f4.readlines():
    s=json.loads(i.strip())
    con[s['name']]=s['conceptId']
s1=input('请输入归属：')
while s1!='-1':
    s2=input('请输入人名：')
    while s2!='-1':
        if s2 not in final_json_st.keys():
            print('Not Found!')
        else:
            final_json_st[s2]['isA']=[s1,con[s1],""]
            f5.write(json.dumps(final_json_st[s2], ensure_ascii=False) + '\n')
        s2=input('请输入人名：')
    s1=input('请输入归属：')