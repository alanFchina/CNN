from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from keras.models import Sequential
from keras.layers import Dense,Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils, generic_utils
from keras.callbacks import Callback
from keras.models import model_from_json
import os
import theano
import h5py
import gzip
import numpy as np
import matplotlib.pyplot as plt
import math
import re
import shutil
from numpy import random

fq=open('blosum.txt','r')
blosum=fq.read()

fw=open('train3.fasta', 'r')
index=1
score=1
matrix=[]
matrix1=[]
matrix2=[]

for line in fw.readlines():
    length=len(line)
    if(length==0):
        length+=1
    if(index < 57):
#        matrix2.append(length)
        for i in range(20):
            for j in range(20):
                str=blosum[i]+blosum[j]
                strnum=0
                for k in range(length-1):
                    str1=line[k]+line[k+1]
                    if(str1==str):
                        strnum+=1
#                matrixint=round((strnum/(length)),3)*1000
                matrix.append(strnum)
        for i in range(20):
            strnum=0
            for j in range(length):
                if(line[j]==blosum[i]):
                    strnum+=1
#            matrixint=round((strnum/(length)),1)*10
            matrix.append(strnum)
        for i in range(20):
            for j in range(20):
                for k in range(16):
                    str=blosum[i]+blosum[j]+blosum[k]
                    strnum=0
                    for w in range(length-2):
                        str1=line[w]+line[w+1]+line[w+2]
                        if(str1==str):
                            strnum+=1
#                    matrixint=round((strnum/(length)),3)*1000
                    matrix.append(strnum)
    if(index>56):
#        if(index<1737):
#            index1=((index-56)//56)
#        if(index>1736):
#            index1=(30+((index-1736)//168))
#        score=length/matrix2[index1]
        for i in range(20):
            for j in range(20):
                str=blosum[i]+blosum[j]
                strnum1=0
                for k in range(length-1):
                    str1=line[k]+line[k+1]
                    if(str1==str):
                        strnum1+=1
#                matrix1int=round((strnum1/(length)),3)*1000
                matrix1.append(strnum1)
        for i in range(20):
            strnum1=0
            for j in range(length):
                if(line[j]==blosum[i]):
                    strnum1+=1
#             matrix1int=round((strnum1/(length)),1)*10
            matrix1.append(strnum1)
        for i in range(20):
            for j in range(20):
                for k in range(16):
                    str=blosum[i]+blosum[j]+blosum[k]
                    strnum1=0
                    for w in range(length-2):
                        str1=line[w]+line[w+1]+line[w+2]
                        if(str1==str):
                            strnum1+=1
#                    matrix1int=round((strnum1/(length)),3)*1000
                    matrix1.append(strnum1)
    index+=1
train_label=[]
for i in range (56):
    train_label.append(i)
'''train_label.append(0)
train_label.append(1)
train_label.append(2)
train_label.append(3)
train_label.append(4)
train_label.append(5)
'''
newshape_train=(56,1,341,20)
X_train=np.reshape(matrix,newshape_train)
train_label= np_utils.to_categorical(train_label,56)

model = Sequential()

model.add(Convolution2D(4, 1,1,init='uniform', border_mode='valid',input_shape=(1,341,20) ,weights=None , subsample=(1,1)))
model.add(Activation('tanh'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Convolution2D(16, 1, 1, border_mode='valid',subsample=(1, 1)))
#model.add(Activation('tanh'))
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Convolution2D(32, 1, 1, border_mode='valid'))    
#model.add(Activation('tanh'))

model.add(Flatten())
model.add(Dense(240,init='normal'))
model.add(Activation('tanh'))
#model.add(Dropout(0.5))
#model.add(Dense(120,init='normal'))
#model.add(Activation('tanh'))
#model.add(Dropout(0.25))
#model.add(Dense(60,init='normal'))
#model.add(Activation('relu'))
model.add(Dense(56,init='normal'))
model.add(Activation('softmax'))

sgd = SGD(lr=0.01, decay=0.0001, momentum=0.6, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=["accuracy"])
#early_stopping = EarlyStopping(monitor='loss', patience=5,mode='auto')callbacks=[early_stopping]
model.fit(X_train,train_label, batch_size=5,nb_epoch=1000,shuffle=True,verbose=1)

json_string = model.to_json()
open('my_model_architecture.json','w').write(json_string)
model.save_weights('my_model_weights.h5')

model = model_from_json(open('my_model_architecture.json').read())
model.load_weights('my_model_weights.h5')

newshape_test=(6048,1,341,20)
X_test=np.reshape(matrix1,newshape_test)
result=model.predict(X_test, batch_size=15, verbose=1)
result2=model.predict_classes(X_test, batch_size=15, verbose=1)
result1=model.predict_proba(X_test, batch_size=15, verbose=1)
acc=0.0
truelabel=0
max1=0.0
j=0
num=0
        
for i in range(30):
    for j in range(56):
        num=i*56+j
        if(j==0):
            max1=result[num][0]
            index1=0
        for s in range(0,56):
            if(result[num][s]>max1):
                max1=result[num][s]
                index1=s
    if(index1==(i)):   
        truelabel+=1
    print(index1)    
for i in range(30,108):
    for j in range(56):
        num=i*56+j
        if(j==0):
            max1=result[num][0]
            index1=0
        for s in range(0,56):
            if(result[num][s]>max1):
                max1=result[num][s]
                index1=s
    if(index1==(30+((i-30)//3))):
        truelabel+=1
    print(index1)                                                                                                                   
   
                                                                                                                                             
            
'''        
    if((result2[i]==index1))
for s in range(0,3):
    if ((result2[s])==0):
        truelabel=truelabel+1
for s in range(3,6):
    if ((result2[s])==1):
        truelabel=truelabel+1
for s in range(6,9):
    if ((result2[s])==2):
        truelabel=truelabel+1
for s in range(9,12):
    if ((result2[s])==3):
        truelabel=truelabel+1
for s in range(12,14):
    if ((result2[s])==4):
        truelabel=truelabel+1
for s in range(14,17):
    if ((result2[s])==5):
        truelabel=truelabel+1
'''                    
acc=truelabel/108.0

print("\n pro:\n",result)
print("test_accuracy:",acc)
print(truelabel)

fw.close()













                                                                                                    
