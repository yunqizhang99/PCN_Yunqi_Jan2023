import parameters
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
from ortools.linear_solver import pywraplp
import copy 
import random

def buildTreeFromListAndGraph(nodeList, networkGraph):
	counter = 0
	visited = []
	resTree = nx.Graph()
	while counter < len(nodeList):
		if counter + 1 < len(nodeList):
			if resTree.has_node(nodeList[counter+1]):
				counter += 1
				continue
			else:
				current_shortest_path = list(nx.shortest_path(networkGraph, nodeList[counter], nodeList[counter+1]))
				copyResTree = copy.deepcopy(resTree)
				copyResTree.add_nodes_from(current_shortest_path)
				current_shortest_path_counter = 0
				while current_shortest_path_counter < len(current_shortest_path) - 1:
					copyResTree.add_edge(current_shortest_path[current_shortest_path_counter], current_shortest_path[current_shortest_path_counter+1])
					current_shortest_path_counter += 1
				existCycle = True
				try:
					nx.find_cycle(copyResTree, orientation=None)
					print("Counter: " + str(counter))
				except nx.exception.NetworkXNoCycle:
					existCycle = False
					print("Counter: " + str(counter))
					print("NO CYCLE")
					resTree = copy.deepcopy(copyResTree)
				print("existCycle: " + str(existCycle))
				if existCycle:
					print("CYCLE")
					branchPtPos = 0
					branchPt = -1
					current_shortest_path_counter = 0
					while current_shortest_path_counter < len(current_shortest_path):
						if resTree.has_node(current_shortest_path[current_shortest_path_counter]) and current_shortest_path.index(current_shortest_path[current_shortest_path_counter]) > branchPtPos:
							branchPtPos = current_shortest_path.index(current_shortest_path[current_shortest_path_counter])
							branchPt = current_shortest_path[current_shortest_path_counter]
						current_shortest_path_counter += 1
					branched_current_shortest_path = current_shortest_path[branchPtPos:]
					resTree.add_nodes_from(branched_current_shortest_path)
					branched_current_shortest_path_counter = 0
					while branched_current_shortest_path_counter < len(branched_current_shortest_path) - 1:
						resTree.add_edge(branched_current_shortest_path[branched_current_shortest_path_counter], branched_current_shortest_path[branched_current_shortest_path_counter+1])
						branched_current_shortest_path_counter += 1
		counter += 1
	# copyResTree = copy.deepcopy(resTree)
	# for e in copyResTree.edges:
	# 	resTree.add_edge(e[1], e[0])
	print("resTree has cycle: ")
	try:
		nx.find_cycle(resTree, orientation=None)
		print("YES")
	except nx.exception.NetworkXNoCycle:
		print("NO")
	return resTree
