from sbm.sbm import SBM
import numpy as np


model = {}
model['sbm_N'] = 1200  # the number of nodes
#model['sbm_P'] = [[0.6, 0.2], [0.2, 0.8]]  # edge probability matrix between nodes belonging different communities
l = 3
within_p = 0.4
accros_p = 0.3
#model['sbm_P'] = [[within_p, accros_p], [accros_p, within_p]]
#model['sbm_P'] = [[within_p, accros_p, accros_p], [accros_p, within_p, accros_p], [accros_p, accros_p, within_p]]
model['sbm_P'] = np.triu(np.ones((l, l), dtype=np.float)*accros_p, 1) + np.tril(np.ones((l, l), dtype=np.float)*accros_p, -1)
model['sbm_P'] += np.diag(np.ones(l, dtype=np.float)*within_p)

print(model['sbm_P'])

model['sbm_block_sizes'] = np.ones(l, dtype=np.int)*int(model['sbm_N']/l)
output_file = "../outputs/sbm_synthetic_"
output_file += "k{}_p{}_q{}_sizes{}.gml".format(len(model['sbm_block_sizes']), within_p, accros_p, ":".join(str(v) for v in model['sbm_block_sizes']))

sbm = SBM(model=model)
sbm.build_graph()
g = sbm.get_graph()

import networkx as nx
comm = nx.get_node_attributes(g, 'community')
counts = [0, 0, 0]
for node in g.nodes():
    counts[int(comm[node][0])] += 1
print(counts)

sbm.save_graph(output_file)
#sbm.plot_graph()