#!/usr/bin/python
#coding=utf-8
import string
import numpy as np
from collections import Counter
nb_seq=0
with open('X1.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')


ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen
nb_seq=0
with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
with open('X2.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen
nb_seq=0
with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
with open(X3.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
nb_seq=0
with open('X4.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
nb_seq=0
with open('X5.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
nb_seq=0
with open('X6.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
nb_seq=0
with open('X7.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
nb_seq=0
with open('X8.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X9.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
nb_seq=0
with open('X10.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
nb_seq=0
with open('X11.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()
nb_seq=0
with open('X12.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X13.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()



nb_seq=0
with open('X14.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X15.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X16.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X17.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X18.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X19.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X19.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X20.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X21.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X22.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X23.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X24.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X25.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X26.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X27.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X28.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X29.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X30.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X31.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X32.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X33.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X34.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X35.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X36.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X37.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X38.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X39.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X40.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X41.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X42.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


nb_seq=0
with open('X43.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X44.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X45.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X46.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X47.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X48.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X49.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X50.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X51.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X52.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X53.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X54.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X55.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()

nb_seq=0
with open('X56.fasta','r') as A1:
	with open('sequence.fasta','w') as A1sen:
		for line in A1.readlines():
			line=line.strip('\n')
			if'>' not in line:
				A1sen.write(line)
					
			if'>'in line :
				A1sen.write('.')
                                nb_seq+=1
A1.close()
A1sen.close()
A1sen= open('sequence.fasta')
ntxt=A1sen.read()
txt=ntxt[:0]+ntxt[1:]
slist=[0 for col in range(nb_seq)]

for i in range (nb_seq): 
	slist[i]= txt.split('.')[i] 
comlist=str()
lsen=str()
for j in range(len(slist[0])):
	for i in range(nb_seq):
		comlist=comlist+slist[i][j]
	if ( Counter(comlist).most_common(1)[0][0]!='-'):
		if(Counter(comlist).most_common(1)[0][1]==nb_seq):
			lsen=lsen+Counter(comlist).most_common(1)[0][0]                        
                        print Counter(comlist).most_common(1)
                         

	comlist=''
print lsen

with open('train.fasta','a')as A1train:
        A1train.write(lsen)
        A1train.write('\n')
A1train.close()


