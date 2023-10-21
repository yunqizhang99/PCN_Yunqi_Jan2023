import parameters
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
from ortools.linear_solver import pywraplp
import copy 
import random

# Python code to sort a list by creating 
# another list Use of sorted()
def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2

df = pd.read_csv(parameters.INIT_BALANCES_FILENAME)
G = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='capacity', create_using=nx.MultiDiGraph())
edge_labels = nx.get_edge_attributes(G,'capacity')

pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
plt.show()

solver_mat = [[0 for _ in range(parameters.GRAPH_NUM_NODES)] for _ in range(parameters.GRAPH_NUM_NODES)]
solver = pywraplp.Solver.CreateSolver('GLOP')

# random demand_mat
# demand_mat = [[random.randint(0,3) for _ in range(parameters.GRAPH_NUM_NODES)] for _ in range(parameters.GRAPH_NUM_NODES)]
# print("DM: " + str(demand_mat))
demand_mat = parameters.DEMAND_MAT
# demand_mat = [[0, 0, 10], [0, 0, 0], [10, 0, 0]]

nodes_i = []
i = 0
while i < parameters.GRAPH_NUM_NODES: 
    nodes_i.append(i)
    i += 1

total_utility = 0

current_sum_edge_capacity = 0
for e in nx.edges(G):
    current_sum_edge_capacity += G[e[0]][e[1]][0]['capacity']
while current_sum_edge_capacity > 0 and sum(sum(demand_mat,[])) > 0:
    nodes_i = []
    i = 0
    while i < parameters.GRAPH_NUM_NODES: 
        nodes_i.append(i)
        i += 1
    while len(nodes_i) > 0:
        current_i = random.choice(nodes_i)
        nodes_j = []
        j = 0
        while j < parameters.GRAPH_NUM_NODES:
            nodes_j.append(j)
            j += 1
        while len(nodes_j) > 0:
            current_j = random.choice(nodes_j)
            if current_i == current_j:
                nodes_j.remove(current_j)
                continue
            all_paths_i_j = list(nx.edge_disjoint_paths(G, current_i, current_j))
            all_paths_i_j_sorted = Sorting(all_paths_i_j)
            print(str(current_i) + " " + str(current_j) + " " + str(all_paths_i_j_sorted))
            for path in all_paths_i_j_sorted:
                if (demand_mat[i][j]) > 0:
                    current_path_available = True
                    current_path_iter = 0
                    while current_path_iter < len(path)-1:
                        if 1 > G[path[current_path_iter]][path[current_path_iter+1]][0]['capacity']:
                            current_path_available = False
                            break
                        current_path_iter += 1
                    if current_path_available:
                        current_path_iter = 0
                        while current_path_iter < len(path)-1:
                            G[path[current_path_iter]][path[current_path_iter+1]][0]['capacity'] -= 1
                            demand_mat[i][j] -= 1
                            current_path_iter += 1
                        total_utility += 1
                        print("path: " + str(path))
                        break
                # current_path_available = True
                # current_path_iter = 0
                # while current_path_iter < len(path)-1:
                #     if demand_mat[current_i][current_j] > G[path[current_path_iter]][path[current_path_iter+1]][0]['capacity']:
                #         current_path_available = False
                #         break
                #     current_path_iter += 1
                # if current_path_available:
                #     current_path_iter = 0
                #     while current_path_iter < len(path)-1:
                #         G[path[current_path_iter]][path[current_path_iter+1]][0]['capacity'] -= demand_mat[current_i][current_j]
                #         current_path_iter += 1
                #     total_utility += demand_mat[current_i][current_j]
                #     print("path: " + str(path))
                #     break

            nodes_j.remove(current_j)
        nodes_i.remove(current_i)
    current_sum_edge_capacity = 0
    for e in nx.edges(G):
        current_sum_edge_capacity += G[e[0]][e[1]][0]['capacity']

print("utility: " + str(total_utility))

# i = 0
# while i < parameters.GRAPH_NUM_NODES:
#     j = 0
#     while j < parameters.GRAPH_NUM_NODES:
#         if i == j: 
#             j += 1
#             continue
#         