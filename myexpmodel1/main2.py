import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = 1000

g = nx.Graph()

for node in range(n):
    g.add_node(node)

degree_seq = np.random.power(size=n, a=3)

for node in range(n):
    for pos_nb in range(node):
        degree_sum = np.sum(degree_seq) - node
        p = float(degree_seq[pos_nb]) / (degree_sum)
        if p > np.random.rand():
            g.add_edge(node, pos_nb)
            degree_seq[node] += 1.0
            degree_seq[pos_nb] += 1.0

#d = [nx.degree(g, node) for node in g.nodes()]
d = degree_seq

#print(sorted(d)[::-1])

#print(g.number_of_nodes())

print(nx.average_clustering(g))

plt.figure()
plt.hist(d, bins=[deg for deg in np.arange(min(d)-0.5, max(d)+1, 1)])
plt.show()