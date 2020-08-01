#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:00:50 2020

@author: luting
"""
import numpy as np

class Vertice:
    def __init__(self, a, b, c):
        self.id = a
        self.x = b
        self.y = c

#lattice-based 4-edge check
def edge_check(a, b, c, d):
    if c-a == 1 and d-b == 0:
        return True
    elif c-a == -1 and d-b == 0:
        return True
    elif c-a == 0 and d-b == 1:
        return True
    elif c-a == 0 and d-b == -1:
        return True
    else:
        return False

#import dimension, start/end details from .txt
f = open("/home/luting/Documents/DP/processingJV/segment-0.txt",'r')

arrDimSE = [] #temp array 

for line in f.readlines():
    arrDimSE.append(line)

c, r = arrDimSE[0].split('x') #number of columns, number of rows

noV = 0 #number of vertices

c_list = [] #list of coordinate objects

for i in range(int(r)): #row increment
    for j in range(int(c)): #column increment
        v = Vertice(noV, j, i)
        c_list.append(v)
        noV += 1

#print coordinate list
for obj in c_list:
    print(obj.id, obj.x, obj.y)
    
#adjancency matrix
adjMat = np.zeros([noV, noV], dtype = int)
print()
print(adjMat)

#export function    
f = open("edge.txt", "w+")

f.write(str(noV) + "\n")
f.write(arrDimSE[1])

for base in c_list:
    for target in c_list:
        #set compare all coordinate sets to each other
        tx = base.x
        ty = base.y
        #check if edge exist
        if edge_check(tx, ty, target.x, target.y) == True:
           f.write(str(base.id) + "->" + str(target.id) + "\n")
           adjMat[base.id, target.id] = 1

f.close()
arrDimSE.clear()

print()        
print(adjMat)        
