from sbm.sbm import SBM



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