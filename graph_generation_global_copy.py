import parameters
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
from ortools.linear_solver import pywraplp
import copy 
import random

df = pd.read_csv(parameters.INIT_BALANCES_FILENAME)
G = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr='capacity', create_using=nx.MultiDiGraph())
edge_labels = nx.get_edge_attributes(G,'capacity')

pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
plt.show()

solver_mat = [[0 for _ in range(parameters.GRAPH_NUM_NODES)] for _ in range(parameters.GRAPH_NUM_NODES)]
solver = pywraplp.Solver.CreateSolver('SCIP')

# random demand_mat
# demand_mat = [[1000 for _ in range(parameters.GRAPH_NUM_NODES)] for _ in range(parameters.GRAPH_NUM_NODES)]
# demand_mat = [[0, 0, 10], [0, 0, 0], [10, 0, 0]]
demand_mat = parameters.DEMAND_MAT

remain_demand_sum_list = []

while len(remain_demand_sum_list) < 10 or len(set(remain_demand_sum_list)) > 1:
    i = 0
    while i < parameters.GRAPH_NUM_NODES:
        j = 0
        while j < parameters.GRAPH_NUM_NODES:
            if i == j: 
                j += 1
                continue
            solver_item_str_name = "flow" + str(i) + "to" + str(j)
            # solver_mat[i][j] = solver.NumVar(0, demand_mat[i][j], solver_item_str_name)
            if demand_mat[i][j] >= 1:
                solver_mat[i][j] = solver.IntVar(0, 1, solver_item_str_name)
            else:
                solver_mat[i][j] = solver.IntVar(0, 0, solver_item_str_name)
            j += 1
        i += 1

    # print(solver_mat)

    edge_path_dic = {}
    i = 0
    while i < parameters.GRAPH_NUM_NODES:
        j = 0
        while j < parameters.GRAPH_NUM_NODES:
            if i == j:
                j += 1
                continue
            all_paths_i_j = list(nx.edge_disjoint_paths(G, s=i, t=j))
            if len(all_paths_i_j) > 0:
                for item in all_paths_i_j:
                    current_path_iter = 0
                    while current_path_iter < len(item)-1:
                        if tuple([item[current_path_iter], item[current_path_iter+1]]) not in edge_path_dic:
                            edge_path_dic[tuple([item[current_path_iter], item[current_path_iter+1]])] = [[i,j]]
                        else:
                            temp_list = edge_path_dic.get(tuple([item[current_path_iter], item[current_path_iter+1]]))
                            temp_list.append([i,j])
                            edge_path_dic[tuple([item[current_path_iter], item[current_path_iter+1]])] = temp_list
                        current_path_iter += 1
                # print("HERE0")
                # sum_min_capability = 0
                # for item in all_paths_i_j:
                #     current_path_iter = 0
                #     current_path_min_capability = 99
                #     print("HERE1")
                #     while current_path_iter < len(item)-1:
                #         current_path_current_capability = G[item[current_path_iter]][item[current_path_iter+1]][0]['capacity']
                #         print("HERE: " + str(current_path_current_capability))
                #         if current_path_current_capability < current_path_min_capability: 
                #             current_path_min_capability = current_path_current_capability
                #         current_path_iter += 1
                #     sum_min_capability += current_path_min_capability
                # solver.Add(solver_mat[i][j] <= sum_min_capability)
            else:
                solver.Add(solver_mat[i][j] == 0)
            j += 1
        i += 1

    sum_paths_flows_mat = [[0 for _ in range(parameters.GRAPH_NUM_NODES)] for _ in range(parameters.GRAPH_NUM_NODES)]

    print(edge_path_dic)
    for key, value in edge_path_dic.items():
        # sum_paths_flows = 0
        # current_path_capability = G[key[0]][key[1]][0]['capacity']
        for pathTuple in value:
            sum_paths_flows_mat[key[0]][key[1]] += solver_mat[pathTuple[0]][pathTuple[1]]
        solver.Add(sum_paths_flows_mat[key[0]][key[1]] <= G[key[0]][key[1]][0]['capacity'])

    solver.Maximize(sum(sum(solver_mat,[])))
    status = solver.Solve()

    # send_demand_mat = [[0 for _ in range(parameters.GRAPH_NUM_NODES)] for _ in range(parameters.GRAPH_NUM_NODES)]

    # i = 0
    # while i < parameters.GRAPH_NUM_NODES:
    #     j = 0
    #     while j < parameters.GRAPH_NUM_NODES:
    #         if i == j: 
    #             j += 1
    #             continue
    #         if solver_mat[i][j].solution_value() == demand_mat[i][j]:
    #             send_demand_mat[i][j] = demand_mat[i][j]
    #         elif solver_mat[i][j].solution_value() > demand_mat[i][j]:
    #             traceback.print_exc()
    #         j += 1
    #     i += 1

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        i = 0
        while i < parameters.GRAPH_NUM_NODES:
            j = 0
            while j < parameters.GRAPH_NUM_NODES:
                if i == j:
                    j += 1
                    continue
                # print(str(solver_mat[i][j]) + ": " + str(solver_mat[i][j].solution_value()))
                # print("solution_value: " + str(solver_mat[i][j].solution_value()))
                demand_mat[i][j] -= solver_mat[i][j].solution_value()
                # print("demand_mat_value: " + str(demand_mat[i][j]))
                j += 1
            i += 1
    else:
        print('The problem does not have an optimal solution.')

    # print("sum_demand_mat_val: " + str(sum(sum(demand_mat,[]))))

    if (len(remain_demand_sum_list) < 10):
        remain_demand_sum_list.append(sum(sum(demand_mat,[])))
    else:
        remain_demand_sum_list.pop(0)
        remain_demand_sum_list.append(sum(sum(demand_mat,[])))

    print("remain_demand_sum_list: " + str(remain_demand_sum_list))

    i = 0
    while i < parameters.GRAPH_NUM_NODES:
        j = 0
        while j < parameters.GRAPH_NUM_NODES:
            if i == j:
                j += 1
                continue
                G[i][j][0]['capacity'] -= sum_paths_flows_mat[i][j]
                G[j][i][0]['capacity'] += sum_paths_flows_mat[i][j]
            j += 1
        i += 1


# print('Objective value =', solver.Objective().Value())
# print("send_demand_mat sum: " + str(sum(sum(send_demand_mat, []))))
# print(len(list(nx.all_simple_paths(G, source=5, target=4))))
# print(len(list(nx.all_simple_paths(G, source=5, target=100))))
print("demand_mat_mat: " + str(demand_mat))


# remain_demand_sum_list: [689.0, 689.0, 689.0, 689.0, 689.0, 689.0, 689.0, 689.0, 689.0, 689.0]
# demand_mat_mat: [[45, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 54, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 35, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 57, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 35, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 45, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 60, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 36, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 37, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 30, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 60, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 53, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 34, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 35, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 38, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 35]]

