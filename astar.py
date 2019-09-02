

huristic=[10,8,7,0]
class Graph():

	def __init__(self, vertices):
		self.areas = {0:'wakad',1:'pune',2:'pimpri',3:'camp',4:'moshi',5:'Alandi'}

		self.V = vertices

		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# display function
	def disp(self, dist):
		print('------------------------------------------------------------------------------')
		print ("Vertex\t\tMinimum Distance\t\tHuristics")
		print('------------------------------------------------------------------------------')
		for node in range(self.V):
			print (self.areas[node], "\t\t", dist[node],'\t\t\t             ',huristic[node])
		print('\n\n======================================================================================================\n\n')


	def minDistance(self, dist, sptSet):



		min = 999


		# Search value with added huristic

		for v in range(self.V):
			if dist[v]+huristic[v] < min and sptSet[v] == False:

				min = dist[v]
				min_index = v





		return min_index


	# a-star function to find minimum val in row
	def astar(self, src):

		print('\nMinimum Distances Form Source:',self.areas[src],'\n')


		dist = [999] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):



			# Pick the minimum distance vertex

			u = self.minDistance(dist, sptSet)



			# Putting the minimum vertex in list

			sptSet[u] = True

			# updating dist val,& check already visited or not

			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
					dist[v] = dist[u] + self.graph[u][v]




		self.disp(dist)


# Driver program
g = Graph(6)
huristic=[10,8,9,5,3,0]
g.graph = [[0,4,2,0,0,0],[4,0,5,10,0,0],[2,5,0,0,3,0],[0,10,0,0,4,11],[0,0,3,4,0,0],[0,0,0,11,0,0]
		]

print('==========================================Application Of A* Algorithm===================================\n\n')

print('\nHello User ..! This Program Will Show You Minimum distance for below areas with destination Alandi.\n')

print('\nAreas In Our Map:')
print('-----------------------------------------------')

for i in range(6):
	print(g.areas[i])
print('-----------------------------------------------')


name = input('\nPlease Enter Your current Location...')

for id, location in g.areas.items():
	if location == name:
		src = id

		g.astar(src)

























































# NOTE-> This Code is developed by Shoaib Shaikh And Tejaswini Ugale
