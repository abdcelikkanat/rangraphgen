import networkx as nx
from rangraphgen.rangraphgen import RanGraphGen
from networkx.algorithms.community.community_generators import LFR_benchmark_graph


class LFR(RanGraphGen):

    def __init__(self, model):
        RanGraphGen.__init__(self, model)

    def lfr_model(self):

        n = self._model['lfr_N']
        tau1 = self._model['lfr_tau1']  # power law exponent for node degree distribution
        tau2 = self._model['lfr_tau2']  # power law exponent for community size distribution
        mu = self._model['lfr_mu']  # fraction of edges between communities
        max_deg = self._model['lfr_max_deg'] if 'lfr_max_deg' in self._model else n
        min_comm = self._model['lfr_min_community']
        max_comm = self._model['lfr_max_community'] if 'lfr_max_community' in self._model else n

        if 'lfr_average_degree' in self._model:
            avg_deg = self._model['lfr_average_degree']
            graph = LFR_benchmark_graph(n=n, tau1=tau1, tau2=tau2, mu=mu,
                                        average_degree=avg_deg, max_degree=max_deg,
                                        min_community=min_comm, max_community=max_comm)
            return graph
        elif 'lfr_min_degree' in self._model:
            min_deg = self._model['lfr_min_degree']
            graph = LFR_benchmark_graph(n=n, tau1=tau1, tau2=tau2, mu=mu,
                                        min_degree=min_deg, max_degree=max_deg,
                                        min_community=min_comm, max_community=max_comm)

            return graph

    def build_graph(self, max_of_trials=5):

        n = self._model['lfr_N']
        tau1 = self._model['lfr_tau1']  # power law exponent for node degree distribution
        tau2 = self._model['lfr_tau2']  # power law exponent for community size distribution
        mu = self._model['lfr_mu']  # fraction of edges between communities
        max_deg = self._model['lfr_max_deg'] if 'lfr_max_deg' in self._model else n
        min_comm = self._model['lfr_min_community']
        max_comm = self._model['lfr_max_community'] if 'lfr_max_community' in self._model else n

        trial_count = 0
        while trial_count < max_of_trials:
            try:
                if 'lfr_average_degree' in self._model:
                    avg_deg = self._model['lfr_average_degree']
                    graph = LFR_benchmark_graph(n=n, tau1=tau1, tau2=tau2, mu=mu,
                                                      average_degree=avg_deg, max_degree=max_deg,
                                                      min_community=min_comm, max_community=max_comm)

                elif 'lfr_min_degree' in self._model:
                    min_deg = self._model['lfr_min_degree']
                    graph = LFR_benchmark_graph(n=n, tau1=tau1, tau2=tau2, mu=mu,
                                                      min_degree=min_deg, max_degree=max_deg,
                                                      min_community=min_comm, max_community=max_comm)

                trial_count += 1
            except nx.exception.ExceededMaxIterations:
                pass

        #mapping = {node: str(node) for node in self._graph.nodes()}
        #self._graph = nx.relabel_nodes(self._graph, mapping)
        #communities = {frozenset(graph.nodes[v]['community']) for v in graph}
        #ss = nx.get_node_attributes(self._graph, 'community')

        self._graph = nx.Graph()

        for node in graph.nodes():
            self._graph.add_node(str(node))

        for edge in graph.edges():
            self._graph.add_edge(str(edge[0]), str(edge[1]))

        communities = {frozenset(graph.nodes[v]['community']) for v in graph}
        node2communities = {node: [] for node in self._graph.nodes()}
        for comm_label, comm in enumerate(communities):
            for node in list(comm):
                node2communities[str(node)].append(comm_label)
        nx.set_node_attributes(self._graph, values=node2communities, name='community')

        """
        g = nx.Graph()
        for edge in self._graph.edges():
            g.add_edge(edge[0], edge[1])

        print(self._graph.number_of_nodes())
        nx.write_gml(g, "./t1.gml")
        """
"""

model = {}
# Parameters used for Stochastic Block Model
model['sbm_N'] = 10
model['sbm_P'] = [[0.3, 0.4], [0.4, 0.7]]
model['sbm_block_sizes'] = [5, 5]
# Parameters used for Lancichinetti-Fortunato-Radicchi (LFR)
model['lfr_N'] = 0
model['lfr_tau1'] = 0
model['lfr_tau2'] = 0
model['lfr_mu'] = 0
model['lfr_min_degree'] = 0
model['lfr_max_degree'] = 0
model['lfr_average_degree'] = 0
model['lfr_min_comm'] = 0
model['lfr_max_comm'] = 0


rg = RanGraphGen(model)
graph = rg.stochastic_block_model()
print(graph.number_of_nodes())


"""

"""
def SBM_simulate_fast(model):
    G = nx.Graph()
    b = model['a']
    J,q = alias_setup(b)
    n = model['N']
    k = model['K']
    B = model['B0']*model['alpha']
    totaledges =0
# add nodes with communities attributes
    grps = {}
    for t in range(k):
        grps[t] = []
    for key in range(n):
        comm = alias_draw(J,q)
        G.add_node(key, community = comm)
        grps[comm].append(key)
    for i in range(k):
        grp1 = grps[i]
        L1 = len(grp1)
        for j in range(i,k):
            grp2 = grps[j]
            L2 = len(grp2)
            if i==j:
                Gsub = nx.fast_gnp_random_graph(L1,B[i,i])
            else:
                Gsub = nx.algorithms.bipartite.random_graph(L1,L2,B[i,j])
            for z in Gsub.edges():
                nd1 = grp1[z[0]]
                nd2 = grp2[z[1]-L1]
                G.add_edge(nd1, nd2, weight = 1.0)
                totaledges +=1
#                if totaledges%1000 == 1:
#                    print 'constructed ', totaledges, ' number of edges'
    print 'the size of graph is ', totaledges, 'number of edges'
return G
"""