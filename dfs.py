from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end = ' ')
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
                
    def DFS(self, v):
        visited = [False] * (max(self.graph)+1)
        self.DFSUtil(v,visited)
        
    def printSolution(self, s):
        print("Starting from Vertice " + s)
        self.DFS(int(s))
        
g = Graph()

f = open('edge.txt','r')

arrVerAdj = []

for line in f.readlines():
    arrVerAdj.append(line)  

s, e = arrVerAdj[1].split(">>")

for element in arrVerAdj[2:]:
    ver, adj = element.split('->')
    g.addEdge(int(ver),int(adj))
    
arrVerAdj.clear()
 
g.printSolution(s) 
