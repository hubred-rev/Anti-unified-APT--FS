import os
a=[a.replace('\n','').split('/')for a in os.popen('apt list --installed').readlines()]
b={}
for c in a[1:]:
    b[c[0]]=c[1]
t,n=[],0
for d in b.keys():
    t.append(d)
print('listed debs.')
f=open('list_dict_installed.txt','w+');f.write(repr(b));f.close()
f=open('list_installed.txt','w+');f.write(repr(t));f.close()
