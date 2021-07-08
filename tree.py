import os
t=os.popen('cd /media/a/3227F05080D331B7/AMirror/mirror/repo.pureos.net/pureos/pool/main;tree').read()
f=open('indexes.txt','w+');f.write(t);f.close()
