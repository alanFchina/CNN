#!/usr/bin/env python
# coding=utf-8
import string
import numpy as np
import os
test_squ=open('test.fasta','r')
test_list=[0 for col in range(2)]
for i in range(2):
    test_list[i]=test_squ.readline().strip('\n')
print test_list
test=test_list[0]+'\n'+test_list[1]

#test_squ=open('test.fasta','r')
#test=test_squ.readlines()

with open ('1.fasta','a')as A:
    	A.write(test)
A.close()
with open ('2.fasta','a')as A:
    	A.write(test)
A.close()
with open ('3.fasta','a')as A:
    	A.write(test)
A.close()
with open ('4.fasta','a')as A:
    	A.write(test)
A.close()
with open ('5.fasta','a')as A:
    	A.write(test)
A.close()
with open ('6.fasta','a')as A:
    	A.write(test)
A.close()
with open ('7.fasta','a')as A:
    	A.write(test)
A.close()
with open ('8.fasta','a')as A:
    	A.write(test)
A.close()
with open ('9.fasta','a')as A:
    	A.write(test)
A.close()
with open ('10.fasta','a')as A:
    	A.write(test)
A.close()
with open ('11.fasta','a')as A:
    	A.write(test)
A.close()
with open ('12.fasta','a')as A:
    	A.write(test)
A.close()

test_squ.close()

