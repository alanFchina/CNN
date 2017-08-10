#!/usr/bin/env python
# coding=utf-8
import os
path='/home/xuqi/文档/test/'
def walk_dir_file(path):
    for dir_name in os.listdir(path):
        if dir_name in ['J1.fasta','J3.fasta','D1.fasta','D2.fasta','E1.fasta','E2.fasta','O1.fasta','P1.fasta','Q1.fasta','R1.fasta','M1.fasta','M3.fasta','K1.fasta','K3.fasta','I2.fasta','I8.fasta','I12.fasta','I17.fasta','H1.fasta','H2.fasta','H3.fasta','H4.fasta','H5.fasta','H6.fasta','H7.fasta','H8.fasta']:
            f=open(os.path.join(path,dir_name),'r')
            with open('test.fasta','a')as A:
                for i in range(2):
                    A.write(f.readline())
        if dir_name in ['A1.fasta','A2.fasta','A3.fasta','A4.fasta','A5.fasta','A6.fasta','B1.fasta','C1.fasta','F1.fasta','G1.fasta','I1.fasta','I3.fasta','I4.fasta','I5.fasta','I6.fasta','I7.fasta','I9.fasta','I10.fasta','I11.fasta','I13.fasta','I14.fasta','I15.fasta','I16.fasta','I18.fasta','J2.fasta','K2.fasta','L1.fasta','M2.fasta','N1.fasta','N2.fasta']:
            f=open(os.path.join(path,dir_name),'r')
            with open('test.fasta','a')as A:
                for i in range(6):
                    A.write(f.readline())
walk_dir_file(path)
            

