#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:00:50 2020

@author: luting
"""

class Vertice:
    def __init__(self, a, b, c):
        self.id = a
        self.x = b
        self.y = c

class Edge:
    def __init__(self, a, b):
        self.root = a
        self.branch = b

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

#insert code to open .txt to state the lattice dimension
# ---> here    
r = 2
c = 2

#number of vertices
noV = 0 

#list of coordinate objects
c_list = []

#row increment
for i in range(r):
    #column increment
    for j in range(c):
        v = Vertice(noV, j, i)
        c_list.append(v)
        noV += 1

#print coordinate list
for obj in c_list:
    print(obj.id, obj.x, obj.y)
 
f = open("edge.txt", "w+")
    
for base in c_list:
    for target in c_list:
        #set compare all coordinate sets to each other
        tx = base.x
        ty = base.y
        #check if edge exist
        if edge_check(tx, ty, target.x, target.y) == True:
           e = Edge(base.id, target.id)
           f.write(str(base.id) + " -> " + str(target.id) + "\n")

f.close()
