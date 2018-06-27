from networkx.algorithms.community import LFR_benchmark_graph
import networkx as nx

n = 1000
tau1 = 2.2
tau2 = 2.3
mu = 0.35

generated_sample_count = 0
num_of_samples = 5

while generated_sample_count < num_of_samples:

    try:
        #G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=5, min_community=20)
        G = LFR_benchmark_graph(n, tau1, tau2, mu, min_degree=1, min_community=20)
        communities = {frozenset(G.nodes[v]['community']) for v in G}

        generated_sample_count += 1
        print(communities)

    except nx.exception.ExceededMaxIterations:
        #generated_sample_count -= 1
        print("exception")

    print(generated_sample_count)

