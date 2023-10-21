""" parameters for graph generation """
# number of nodes 
GRAPH_NUM_NODES = 42
# node list
NODE_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
# filename for initial balances
INIT_BALANCES_FILENAME = "initial_balances_12052022.csv"
# filename for initial demands
INIT_DEMANDS_FILENAME = "initial_demands_12052022.csv"
# demand matrix
# DEMAND_MAT = [[0, 123, 105], [99, 0, 108], [110, 89, 0]]
# DEMAND_MAT = [[0, 33, 29], [28, 0, 23], [13, 23, 0]]
DEMAND_MAT = [[1, 0, 2, 0, 3, 0, 3, 3, 2, 3, 2, 3, 3, 0, 3, 3, 3, 1, 0, 1, 0, 1, 1, 2, 3, 3, 1, 2, 2, 2, 0, 2, 0, 3, 2, 1, 0, 1, 0, 0, 3, 3], [1, 0, 1, 1, 1, 3, 2, 1, 1, 0, 0, 1, 2, 2, 2, 1, 3, 1, 0, 2, 2, 2, 3, 2, 2, 2, 0, 1, 2, 1, 3, 3, 1, 1, 2, 2, 2, 2, 0, 1, 3, 0], [2, 3, 0, 2, 0, 1, 3, 0, 3, 3, 0, 1, 0, 1, 1, 0, 1, 0, 3, 2, 0, 0, 0, 3, 3, 3, 0, 3, 1, 0, 1, 3, 0, 3, 3, 1, 0, 1, 2, 0, 2, 3], [2, 1, 0, 0, 0, 2, 1, 3, 0, 3, 1, 3, 0, 0, 3, 2, 3, 1, 0, 2, 0, 0, 2, 1, 3, 3, 3, 3, 0, 1, 0, 2, 0, 0, 2, 0, 2, 0, 1, 2, 1, 0], [0, 1, 3, 1, 2, 3, 1, 1, 3, 0, 1, 0, 1, 2, 3, 3, 1, 3, 0, 3, 1, 2, 2, 0, 3, 3, 0, 3, 2, 0, 1, 3, 1, 1, 3, 1, 0, 3, 1, 1, 0, 0], [0, 2, 0, 3, 1, 3, 0, 2, 1, 1, 2, 2, 3, 0, 2, 2, 1, 1, 2, 1, 1, 1, 0, 2, 3, 3, 2, 0, 3, 2, 3, 2, 3, 0, 1, 1, 2, 2, 0, 0, 1, 1], [1, 0, 2, 2, 3, 1, 2, 1, 2, 1, 0, 0, 0, 3, 2, 1, 3, 1, 2, 2, 2, 1, 1, 2, 3, 0, 3, 2, 1, 0, 3, 0, 2, 1, 1, 0, 3, 0, 2, 1, 2, 0], [0, 0, 2, 3, 0, 0, 1, 1, 0, 3, 1, 3, 2, 3, 1, 3, 2, 3, 0, 0, 2, 3, 1, 1, 0, 2, 0, 2, 0, 0, 0, 3, 1, 2, 0, 3, 3, 3, 1, 1, 1, 1], [3, 3, 0, 0, 2, 3, 0, 3, 3, 1, 1, 0, 1, 3, 3, 1, 0, 1, 0, 3, 0, 1, 1, 0, 1, 0, 0, 1, 2, 1, 1, 0, 1, 1, 3, 0, 0, 2, 3, 2, 0, 1], [3, 0, 2, 2, 1, 2, 1, 2, 2, 2, 0, 0, 0, 2, 1, 2, 0, 3, 0, 2, 3, 0, 2, 1, 2, 2, 1, 1, 2, 1, 0, 3, 3, 2, 2, 2, 2, 0, 3, 1, 2, 2], [2, 1, 3, 1, 0, 3, 0, 3, 2, 1, 0, 1, 1, 3, 1, 0, 1, 2, 0, 3, 1, 1, 3, 0, 3, 2, 1, 1, 3, 3, 1, 0, 1, 2, 2, 1, 2, 2, 2, 0, 1, 0], [0, 2, 0, 3, 0, 2, 2, 0, 1, 2, 2, 2, 1, 3, 2, 1, 3, 0, 3, 0, 1, 0, 1, 3, 2, 3, 0, 2, 2, 2, 3, 2, 3, 3, 0, 2, 3, 2, 1, 0, 0, 3], [0, 2, 2, 2, 0, 2, 2, 2, 3, 0, 1, 3, 3, 3, 0, 2, 0, 2, 2, 3, 2, 1, 3, 1, 3, 3, 1, 3, 3, 1, 0, 1, 1, 1, 3, 2, 3, 1, 3, 2, 1, 2], [1, 2, 0, 2, 1, 2, 0, 0, 1, 2, 2, 1, 2, 0, 2, 3, 3, 3, 0, 3, 3, 3, 1, 1, 3, 1, 1, 3, 0, 3, 3, 2, 0, 3, 0, 0, 3, 2, 0, 3, 0, 1], [2, 0, 2, 1, 1, 3, 1, 0, 2, 3, 2, 0, 0, 0, 1, 0, 2, 0, 3, 1, 2, 3, 1, 3, 2, 2, 2, 0, 3, 3, 3, 3, 3, 1, 3, 3, 0, 3, 0, 1, 3, 2], [2, 0, 0, 2, 2, 3, 2, 0, 3, 1, 3, 2, 1, 0, 0, 2, 3, 3, 0, 3, 2, 3, 3, 0, 2, 0, 1, 2, 3, 1, 3, 1, 3, 0, 0, 2, 2, 1, 2, 1, 2, 2], [3, 1, 1, 3, 0, 2, 1, 2, 2, 1, 0, 2, 3, 0, 2, 2, 3, 2, 0, 2, 3, 1, 2, 3, 3, 1, 3, 0, 3, 3, 2, 0, 2, 2, 3, 1, 1, 2, 3, 0, 3, 0], [2, 1, 2, 2, 0, 0, 3, 1, 2, 1, 0, 1, 0, 2, 1, 2, 0, 0, 0, 2, 0, 2, 0, 1, 1, 3, 0, 2, 3, 2, 2, 0, 2, 1, 0, 3, 1, 3, 0, 2, 2, 2], [0, 2, 0, 0, 0, 2, 3, 3, 0, 1, 2, 3, 2, 1, 2, 3, 1, 1, 2, 1, 0, 1, 0, 3, 0, 2, 1, 3, 0, 2, 1, 2, 2, 0, 0, 1, 0, 1, 1, 1, 1, 0], [3, 1, 0, 3, 0, 3, 2, 0, 0, 2, 2, 1, 3, 1, 3, 3, 1, 1, 0, 2, 3, 2, 0, 2, 1, 1, 3, 2, 3, 3, 0, 0, 1, 3, 3, 0, 0, 3, 1, 0, 0, 2], [0, 1, 1, 1, 3, 3, 0, 0, 3, 2, 2, 3, 1, 0, 3, 1, 3, 0, 0, 3, 2, 1, 3, 1, 2, 1, 2, 1, 0, 1, 1, 2, 2, 1, 1, 1, 1, 0, 1, 3, 2, 3], [3, 2, 1, 1, 2, 1, 1, 3, 1, 3, 1, 3, 3, 3, 2, 2, 3, 0, 2, 2, 3, 2, 2, 0, 2, 3, 1, 3, 0, 0, 3, 0, 1, 1, 3, 3, 3, 1, 0, 0, 1, 3], [2, 3, 3, 1, 3, 3, 3, 1, 0, 1, 2, 1, 0, 2, 0, 3, 2, 0, 3, 1, 0, 0, 0, 0, 1, 3, 1, 2, 0, 1, 1, 3, 2, 1, 1, 2, 3, 0, 2, 0, 1, 3], [3, 2, 3, 0, 1, 3, 2, 2, 3, 2, 0, 0, 3, 2, 0, 1, 2, 3, 3, 0, 0, 0, 2, 2, 3, 3, 2, 3, 0, 2, 0, 2, 3, 3, 0, 0, 3, 0, 1, 1, 0, 3], [2, 2, 0, 1, 2, 2, 3, 1, 2, 3, 2, 1, 1, 2, 2, 2, 2, 0, 3, 2, 3, 0, 2, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 3, 1, 0, 1, 3, 2, 0, 1, 0], [3, 3, 3, 1, 3, 1, 2, 3, 3, 1, 3, 3, 0, 1, 3, 1, 0, 0, 2, 3, 1, 0, 0, 3, 3, 2, 2, 0, 3, 1, 2, 1, 1, 3, 0, 0, 0, 1, 0, 0, 2, 0], [1, 2, 2, 1, 2, 1, 2, 3, 1, 1, 3, 3, 0, 3, 1, 3, 0, 3, 3, 2, 2, 1, 2, 2, 0, 0, 0, 3, 3, 0, 1, 3, 2, 0, 0, 2, 0, 0, 1, 0, 2, 3], [1, 0, 0, 3, 1, 3, 0, 2, 2, 2, 1, 0, 3, 1, 1, 2, 1, 1, 0, 2, 3, 0, 3, 3, 2, 1, 3, 2, 0, 3, 3, 1, 2, 1, 0, 0, 0, 1, 1, 2, 2, 2], [1, 2, 3, 3, 1, 2, 3, 0, 3, 1, 3, 3, 0, 2, 1, 0, 0, 0, 3, 2, 0, 0, 1, 0, 0, 0, 2, 2, 1, 1, 0, 1, 1, 1, 3, 3, 2, 3, 2, 3, 3, 0], [1, 1, 1, 3, 0, 1, 2, 3, 2, 1, 3, 2, 0, 0, 3, 0, 2, 0, 3, 0, 3, 1, 2, 3, 0, 0, 2, 3, 2, 1, 3, 2, 0, 3, 0, 0, 2, 1, 1, 0, 0, 2], [0, 1, 0, 3, 2, 0, 3, 0, 3, 0, 1, 2, 0, 1, 2, 2, 2, 2, 3, 3, 1, 3, 1, 3, 0, 3, 1, 2, 2, 0, 2, 3, 2, 1, 1, 3, 2, 2, 2, 1, 0, 1], [0, 0, 1, 3, 2, 0, 2, 1, 1, 2, 0, 0, 0, 1, 2, 3, 0, 0, 1, 1, 0, 0, 2, 1, 1, 3, 0, 0, 1, 2, 1, 0, 2, 0, 2, 3, 2, 1, 1, 1, 0, 2], [3, 2, 0, 2, 0, 2, 0, 1, 2, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 3, 2, 2, 3, 2, 2, 0, 2, 2, 2, 2, 3, 3, 2, 1, 3, 1, 3, 0, 0, 0, 1, 0], [2, 0, 3, 1, 0, 0, 3, 2, 1, 3, 0, 3, 2, 1, 0, 1, 2, 3, 1, 3, 0, 1, 2, 3, 3, 1, 1, 3, 1, 3, 0, 2, 1, 0, 0, 3, 3, 1, 1, 2, 2, 1], [2, 3, 1, 1, 1, 3, 3, 0, 3, 2, 0, 2, 2, 1, 0, 3, 0, 3, 3, 2, 3, 1, 1, 3, 0, 1, 0, 1, 0, 3, 2, 0, 1, 0, 1, 0, 0, 1, 3, 0, 1, 0], [3, 0, 1, 0, 0, 2, 3, 2, 3, 0, 2, 0, 0, 1, 1, 0, 2, 0, 0, 0, 2, 0, 2, 2, 3, 3, 2, 1, 3, 3, 3, 3, 3, 2, 3, 0, 0, 1, 2, 0, 2, 0], [0, 2, 3, 0, 3, 3, 3, 3, 1, 1, 0, 1, 3, 0, 0, 3, 2, 1, 0, 1, 1, 3, 1, 2, 0, 0, 3, 0, 0, 0, 0, 0, 1, 2, 3, 3, 3, 1, 2, 3, 0, 0], [2, 1, 3, 0, 2, 2, 2, 3, 3, 3, 3, 1, 3, 2, 0, 1, 2, 0, 2, 0, 3, 0, 3, 1, 0, 0, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 3, 0, 0, 2, 3], [2, 1, 0, 0, 2, 1, 1, 3, 1, 2, 3, 3, 2, 3, 3, 0, 0, 2, 0, 2, 3, 1, 2, 0, 2, 3, 3, 3, 2, 0, 3, 1, 0, 0, 3, 3, 0, 2, 2, 3, 1, 1], [1, 1, 2, 2, 1, 3, 0, 0, 2, 2, 0, 0, 1, 2, 0, 2, 3, 0, 1, 3, 0, 0, 1, 2, 3, 0, 1, 1, 3, 3, 2, 1, 0, 3, 2, 3, 2, 0, 3, 3, 2, 1], [1, 2, 1, 2, 3, 0, 3, 3, 3, 1, 3, 3, 0, 1, 1, 2, 3, 1, 3, 2, 0, 3, 3, 1, 2, 0, 3, 0, 2, 2, 3, 1, 0, 1, 3, 0, 0, 0, 0, 2, 3, 0], [3, 1, 3, 1, 0, 3, 2, 3, 3, 1, 0, 3, 1, 3, 3, 1, 1, 2, 2, 1, 0, 3, 0, 1, 0, 3, 0, 1, 3, 2, 2, 3, 0, 0, 1, 3, 3, 0, 0, 3, 2, 2]]
# DEMAND_MAT = [[45, 32, 33, 59, 45, 58, 44, 44, 33, 40, 43, 37, 30, 55, 39, 59], [47, 54, 55, 54, 47, 31, 30, 33, 59, 37, 56, 49, 37, 55, 56, 45], [60, 34, 35, 32, 46, 44, 35, 55, 49, 58, 40, 57, 31, 41, 46, 55], [44, 55, 59, 57, 59, 30, 41, 31, 39, 40, 59, 46, 34, 31, 54, 40], [44, 48, 39, 35, 35, 59, 55, 37, 45, 49, 34, 45, 44, 47, 58, 31], [35, 38, 36, 59, 53, 45, 43, 52, 51, 45, 32, 37, 56, 44, 43, 45], [48, 37, 37, 51, 38, 47, 60, 32, 39, 46, 38, 45, 32, 30, 31, 38], [30, 46, 54, 58, 42, 31, 54, 36, 54, 45, 60, 31, 49, 47, 33, 38], [57, 47, 44, 52, 44, 52, 47, 55, 37, 39, 60, 37, 60, 48, 53, 36], [45, 37, 58, 37, 33, 31, 53, 35, 37, 30, 45, 47, 55, 42, 59, 41], [60, 54, 55, 50, 37, 49, 47, 59, 53, 51, 60, 49, 31, 37, 39, 32], [36, 48, 55, 57, 32, 30, 33, 34, 52, 47, 39, 53, 51, 52, 35, 43], [53, 37, 45, 57, 55, 31, 41, 49, 56, 34, 37, 30, 34, 44, 55, 50], [49, 39, 46, 31, 38, 59, 47, 52, 51, 42, 48, 43, 34, 35, 32, 34], [42, 32, 37, 33, 60, 44, 43, 36, 38, 36, 55, 58, 30, 40, 38, 39], [44, 47, 35, 40, 58, 35, 40, 57, 56, 36, 30, 48, 57, 48, 42, 35]]