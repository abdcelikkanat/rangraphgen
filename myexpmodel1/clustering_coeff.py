import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = 1000

g = nx.Graph()

for node in range(n):
    g.add_node(node)



for node in range(n):
    degree_seq = np.ones(node, dtype=np.float)

    for pos_nb in range(node):
        node_deg = float(nx.degree(g, node)) + 1.0
        pos_nb_deg = float(nx.degree(g, pos_nb)) + 1.0
        comm_count = float(len(list(nx.common_neighbors(g, node, pos_nb)))) + 1.0

        #p = comm_count / max(node_deg, pos_nb_deg)
        p = comm_count / (node_deg + pos_nb_deg - 1)
        #print(p)
        if p > np.random.rand():
            g.add_edge(node, pos_nb)

#d = [nx.degree(g, node) for node in g.nodes()]

#print(sorted(d)[::-1])

#print(g.number_of_nodes())

print(g.number_of_nodes())
print(g.number_of_edges())
print(nx.average_clustering(g))


"""
plt.figure()
plt.hist(d, bins=[deg for deg in np.arange(min(d)-0.5, max(d)+1, 1)])
plt.show()
"""
