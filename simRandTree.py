import parameters
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
from ortools.linear_solver import pywraplp
import copy 
import random
import randTreeList

node_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print("Shuffled Node List: " + str(node_list))
network_graph = nx.Graph()
network_graph.add_nodes_from(node_list)
i = 0
while i < len(node_list) - 1:
	j = i + 1
	while j < len(node_list):
		if random.randint(1, 10) <= 3:
			network_graph.add_edge(i, j)
		j += 1
	i += 1

print("network_graph is connected? " + str(nx.is_connected(network_graph)))
posGraph = nx.spring_layout(network_graph)
nx.draw(network_graph, posGraph, with_labels = True)
plt.show(block=False)
plt.savefig("NetworkGraph.pdf", format="PDF")

random.shuffle(node_list)
testTree = randTreeList.buildTreeFromListAndGraph(node_list, network_graph)

plt.clf()
posTree = nx.spring_layout(testTree)
nx.draw(testTree, posTree, node_size=10, with_labels = True)
plt.show(block=False)
plt.savefig("TestTree1.pdf", format="PDF")

random.shuffle(node_list)
testTree = randTreeList.buildTreeFromListAndGraph(node_list, network_graph)

plt.clf()
posTree = nx.spring_layout(testTree)
nx.draw(testTree, posTree, node_size=10, with_labels = True)
plt.show(block=False)
plt.savefig("TestTree2.pdf", format="PDF")

random.shuffle(node_list)
testTree = randTreeList.buildTreeFromListAndGraph(node_list, network_graph)

plt.clf()
posTree = nx.spring_layout(testTree)
nx.draw(testTree, posTree, node_size=10, with_labels = True)
plt.show(block=False)
plt.savefig("TestTree3.pdf", format="PDF")

random.shuffle(node_list)
testTree = randTreeList.buildTreeFromListAndGraph(node_list, network_graph)

plt.clf()
posTree = nx.spring_layout(testTree)
nx.draw(testTree, posTree, node_size=10, with_labels = True)
plt.show(block=False)
plt.savefig("TestTree4.pdf", format="PDF")