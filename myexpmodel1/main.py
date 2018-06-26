import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = 1000

g = nx.Graph()

for node in range(n):
    g.add_node(node)
    for pos_nb in range(node):
        pos_degree_seq = [nx.degree(g, cand) for cand in range(node)]
        total_degree = np.sum(pos_degree_seq)
        pos_nb_deg = pos_degree_seq[pos_nb]
        if pos_nb_deg != 0:
            p = float(pos_nb_deg) / float(total_degree)
            #print(p)
        else:
            p = 0.5
        if p > np.random.rand():
            g.add_edge(node, pos_nb)


d = [nx.degree(g, node) for node in g.nodes()]
print(sorted(d)[::-1])

print(g.number_of_nodes())


plt.figure()
plt.hist(d, bins=[deg for deg in np.arange(min(d)-0.5, max(d)+1, 1)])
plt.show()