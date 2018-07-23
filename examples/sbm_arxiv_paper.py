from sbm.sbm import SBM


"""
model = {}
model['sbm_N'] = 100  # the number of nodes
model['sbm_P'] = [[0.6, 0.2], [0.2, 0.8]]  # edge probability matrix between nodes belonging different communities
model['sbm_block_sizes'] = [40, 60]

output_file = "../outputs/synthetic_"
output_file += "n{}_p{}_sizes{}.gml".format(model['sbm_N'], 1, ":".join(str(v) for v in model['sbm_block_sizes']))

sbm = SBM(model=model)
sbm.build_graph()
g = sbm.get_graph()
sbm.save_graph(output_file)
#sbm.plot_graph()
"""

model = {}
N = 10000
c = 3.5
model['sbm_block_sizes'] = [N/2, N/2]

K = 2
mylambda = 0.9

model['sbm_N'] = N
model['sbm_P'] = [[0.0 for _ in range(K)] for _ in range(K)]


for i in range(K):
    for j in range(K):
        if i == j:
            model['sbm_P'][i][j] = float(c) / float(N)
        else:
            model['sbm_P'][i][j] = float(c)*(1.0 - mylambda) / float(N)

output_file = "../outputs/sbm_"
output_file += "n{}_k{}_lambda{}_c{}.gml".format(N, K, mylambda, c)


sbm = SBM(model=model)
sbm.build_graph()
g = sbm.get_graph()
sbm.save_graph(output_file)
#sbm.plot_graph()