import os
path=['fd','fl']
for a in path:
    if not os.path.exists(a):os.makedirs(a)
sources_list='''/media/a/3227F05080D331B7/AMirror/mirror/repo.pureos.net/pureos/dists/amber/main/binary-amd64/Packages
/media/a/3227F05080D331B7/AMirror/mirror/repo.pureos.net/pureos/dists/amber-security/main/binary-amd64/Packages
/media/a/3227F05080D331B7/AMirror/mirror/repo.pureos.net/pureos/dists/amber-updates/main/binary-amd64/Packages'''.split('\n')
i=''
for a in sources_list:f=open(a,'r');i='%s%s%s'%(i,'\n'if i!=''else'',f.read());f.close()
d={}
i=i.split('Package: ')[1:]
for a in i:
    print(a)
    if(dn:=a.split('\n')[0])not in d:
        d[dn]={'Package':dn}
        o=a.split('\n')[1:]
        for v in o:
            if v.find(': ')!=-1:
                n=v.split(': ')[0]
                d[dn][n]=': '.join(x)if isinstance(x:=v.split(': ')[1],list)else x
                if n=='Depends':
                    d[dn][n]=[[b.split(' (')[0],b.split('(')[1][:-1].split(' ')[0],b.split('(')[1][:-1].split(' ')[1]]if b.find('(')!=-1 else b for b in d[dn][n].split(', ')]
                elif n=='Suggests':
                    d[dn][n]=d[dn][n].split(', ')
                if n=='Pre-Depends':
                    d[dn][n]=[[b.split(' (')[0],b.split('(')[1][:-1].split(' ')[0],b.split('(')[1][:-1].split(' ')[1]]if b.find('(')!=-1 else b for b in d[dn][n].split(', ')]
        #print(d[dn])
        fl=open('fl/%s'%dn,'w+');fl.write(repr(d[dn]));fl.close()
for a in(dl:=d.keys()):
    print(a)
    if not os.path.exists(pa:='fd/%s'%a):os.makedirs(pa)
    if'Pre-Depends'in d[a]or'Depends'in d[a]:
        if'Pre-Depends'in d[a]:
            zv=d[a]['Pre-Depends'].copy()
            if'Depends'in d[a]:zv.extend(d[a]['Depends'])
        elif'Depends'in d[a]:
            zv=d[a]['Depends'].copy()
        zv3=[]
        zv4=[]
        for t in zv:
            if t[0]not in zv3:
                zv4.append(t)
                zv3.append(t[0])
        zv=zv4
        for b in zv:
            fl=[]
            if isinstance(b,list):
                if b[0]in dl:
                    if b[0]not in fl:fl.append(b[0])
            else:
                if b in dl:
                    if b not in fl:fl.append(b)
            while True:
                l1,l2=0,0
                l1=len(fl)
                for c in fl:
                    if'Pre-Depends'in d[c]or'Depends'in d[c]:
                        if'Pre-Depends'in d[c]:
                            zv2=d[c]['Pre-Depends'].copy()
                            if'Depends'in d[c]:zv2.extend(d[c]['Depends'])
                        elif'Depends'in d[c]:
                            zv2=d[c]['Depends'].copy()
                        zv3=[]
                        zv4=[]
                        for t in zv:
                            if t[0]not in zv3:
                                zv4.append(t)
                                zv3.append(t[0])
                        zv2=zv4
                        for e in zv2:
                            if isinstance(e,list):
                                if e[0]in dl:
                                    if e[0]not in fl:fl.append(e[0])
                            else:
                                if e in dl:
                                    if e not in fl:fl.append(e)
                l2=len(fl)
                if l1==l2:break
            for c in fl:f=open('%s/%s'%(pa,c),'w+');f.write(repr(d[c]));f.close()
    else:
        f=open('%s/%s'%(pa,a),'w+');f.write(repr(d[a]));f.close()
