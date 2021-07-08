import sys,os
repo='/media/a/3227F05080D331B7/AMirror/mirror/repo.pureos.net/pureos'
try:
    print(sys.argv)
    a=[sys.argv[1],sys.argv[2]]
except:print('Please check your name and try again.');quit()
f,z,y=open('list_installed.txt','r'),{},open('all_debs.txt','r');hp,ap=eval(f.read()),eval(y.read());f.close();y.close()
if a[0]=='install':
    if a[1]not in hp:
        if a[1]in ap:
            print('Start install software %s.'%a[1])
            for b,c,d in os.walk('%s/fd/%s'%(sys.path[0],a[1])):
                for e in d:
                    f=open('%s/%s'%(b,e),'r');i=eval(f.read());f.close()
                    if i['Package']not in hp:
                        z[i['Package']]=i['Filename']
                    print(i)
                print(repr(z).replace(', ','\n'))
            #這裡輸入原版
            f=open('fl/%s'%a[1],'r');i=eval(f.read());f.close()
            if i['Package']not in hp:
                z[i['Package']]=i['Filename']
            for b in z.values():
                os.system('sudo dpkg -i %s/%s'%(repo,b))
            print(i)
        else:print('No Software.')
    else:print('Software %s was install.'%a[1])
elif a[1]=='remove':
    if a[1]in hp:
        if a[1]in ap:
            print('Start remove software %s.'%a[1])
        else:print('No Software.')
    else:print('Software %s was remove.'%a[1])
else:print('no operations.')
