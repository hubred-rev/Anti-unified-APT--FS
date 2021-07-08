import os
z=[]
for a,b,c in os.walk('fl'):
    for d in c:
        z.append(d)
f=open('all_debs.txt','w+');f.write(repr(z));f.close()
