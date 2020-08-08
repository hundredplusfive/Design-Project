# Python program for solution of 
# hamiltonian cycle problem 
# This code (line 4 to 77) is contributed by Divyanshu Mehta. The remaining codes are extended from it   
class Graph(): 
	def __init__(self, vertices): 
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
		self.V = vertices 

	''' Check if this vertex is an adjacent vertex 
		of the previously added vertex and is not 
		included in the path earlier '''
	def isSafe(self, v, pos, path): 
		# Check if current vertex and last vertex 
		# in path are adjacent 
		if self.graph[ path[pos-1] ][v] == 0: 
			return False

		# Check if current vertex not already in path 
		for vertex in path: 
			if vertex == v: 
				return False

		return True

	# A recursive utility function to solve 
	# hamiltonian cycle problem 
	def hamCycleUtil(self, path, pos): 

		# base case: if all vertices are 
		# included in the path 
		if pos == self.V: 
			# Last vertex must be adjacent to the 
			# first vertex in path to make a cyle 
			if self.graph[ path[pos-1] ][ path[0] ] == 1: 
				return True
			else: 
				return False

		# Try different vertices as a next candidate 
		# in Hamiltonian Cycle. We don't try for 0 as 
		# we included 0 as starting point in hamCycle() 
		for v in range(0,self.V): 

			if self.isSafe(v, pos, path) == True: 

				path[pos] = v 

				if self.hamCycleUtil(path, pos+1) == True: 
					return True

				# Remove current vertex if it doesn't 
				# lead to a solution 
				path[pos] = -1

		return False

	def hamCycle(self, s): 
		path = [-1] * self.V 

		''' Let us put vertex 0 as the first vertex 
			in the path. If there is a Hamiltonian Cycle, 
			then the path can be started from any point 
			of the cycle as the graph is undirected '''
		path[0] = s

		if self.hamCycleUtil(path,1) == False: 
			print ("Solution does not exist\n") 
			return False

		self.printSolution(path, s) 
		return True

	def printSolution(self, path, s): 
		print ("Starting from Vertice " + str(s)) 
		for vertex in path: 
			print (vertex, end = " ") 
		print (path[0], "\n") 

#adjacncey list to matrix conversion integrated
f = open('edge.txt','r')

arrVerAdj = []

for line in f.readlines():
    arrVerAdj.append(line)
    
g = Graph(int(arrVerAdj[0]))  

s, e = arrVerAdj[1].split(">>")

for element in arrVerAdj[2:]: #skips first two lines
    ver, adj = element.split('->')
    g.graph[int(ver)][int(adj)] = 1

arrVerAdj.clear()

# Print the solution 
g.hamCycle(int(s)); 
