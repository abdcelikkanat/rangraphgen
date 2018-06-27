import numpy as np
import networkx as nx
from rangraphgen.rangraphgen import RanGraphGen


class SBM(RanGraphGen):

    def __init__(self, model):
        RanGraphGen.__init__(self, model)

    def build_graph(self):

        n = self._model['sbm_N']  # the number of nodes
        p = self._model['sbm_P']  # edge probability matrix between nodes belonging different communities
        block_sizes = self._model['sbm_block_sizes']
        K = len(p)  # number of communities

        assert n == np.sum(block_sizes), "The sum of the block sizes must be equal to the number of nodes, N"

        p = np.asarray(p, dtype=np.float)
        assert np.allclose(p, p.T, atol=1e-8), "The matrix must be symmetric!"

        graph = nx.Graph()
        node2community = {}

        communities = [[] for _ in range(K)]

        k = 0
        for node in range(n):
            if node == np.sum(block_sizes[:k+1]):
                k += 1
            #k = int(np.rint(float(node) / np.sum(block_sizes)))
            communities[k].append(str(node))
            graph.add_node(str(node))
            node2community.update({str(node): [k]})

        for k1 in range(K):
            for k2 in range(k1, K):
                # Generate edges for each community
                if k1 == k2:
                    subg = nx.fast_gnp_random_graph(n=len(communities[k1]), p=p[k1][k2])

                else:
                    subg = nx.algorithms.bipartite.random_graph(n=len(communities[k1]), m=len(communities[k2]), p=p[k1][k2])

                for edge in subg.edges():
                    n1 = communities[k1][int(edge[0])]
                    n2 = communities[k2][int(edge[1])-len(communities[k1])]
                    graph.add_edge(n1, n2)

        nx.set_node_attributes(graph, values=node2community, name='community')

        self._graph = graph

