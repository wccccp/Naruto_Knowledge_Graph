f1=open('1.txt','r',encoding='utf-8')
f2=open('2.txt','r',encoding='utf-8')
f3=open('3.txt','r',encoding='utf-8')
f4=open('4.txt','r',encoding='utf-8')
d={}
for i in f1.readlines():
    i=i.strip()
    a,b=map(str,i.split(sep='-'))
    s1='        <untitled-ontology-25:'+'is_child_of'+' rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'+a+'"/>'
    s2='        <untitled-ontology-25:'+'is_parent_of'+' rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'+b+'"/>'
    if a in d.keys():
        d[a].append(s2)
    else:
        d[a]=[s2]
    if b in d.keys():
        d[b].append(s1)
    else:
        d[b]=[s1]
for i in f2.readlines():
    i=i.strip()
    a,b=map(str,i.split(sep='-'))
    s1='        <untitled-ontology-25:'+'is_sibling_of'+' rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'+a+'"/>'
    s2='        <untitled-ontology-25:'+'is_sibling_of'+' rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'+b+'"/>'
    if a in d.keys():
        d[a].append(s2)
    else:
        d[a]=[s2]
    if b in d.keys():
        d[b].append(s1)
    else:
        d[b]=[s1]
for i in f3.readlines():
    i=i.strip()
    a,b=map(str,i.split(sep='-'))
    s1='        <untitled-ontology-25:'+'is_married_to'+' rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'+a+'"/>'
    s2='        <untitled-ontology-25:'+'is_married_to'+' rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'+b+'"/>'
    if a in d.keys():
        d[a].append(s2)
    else:
        d[a]=[s2]
    if b in d.keys():
        d[b].append(s1)
    else:
        d[b]=[s1]
for i in f4.readlines():
    i=i.strip()
    a,b=map(str,i.split(sep='-'))
    s1='        <untitled-ontology-25:'+'is_student_of'+' rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'+a+'"/>'
    s2='        <untitled-ontology-25:'+'is_teacher_of'+' rdf:resource="http://www.semanticweb.org/administrator/ontologies/2019/4/untitled-ontology-25#'+b+'"/>'
    if a in d.keys():
        d[a].append(s2)
    else:
        d[a]=[s2]
    if b in d.keys():
        d[b].append(s1)
    else:
        d[b]=[s1]

s=input()
while s!='-1':
    if s in d.keys():
        for i in range(len(d[s])):
            if i==0:
                print(d[s][i][8::])
            else:
                print(d[s][i])
    else:
        print('!')
    s=input()