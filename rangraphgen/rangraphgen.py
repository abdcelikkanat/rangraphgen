import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class RanGraphGen:
    def __init__(self, model=None):
        self._model = model
        self._graph = None

    def set_model(self, model):
        self._model = model

    def get_graph(self):

        if self._model is None:
            raise ValueError("No graph has been build!")

        return self._graph

    def plot_graph(self, colorful=False):

        plt.figure()
        pos = nx.spring_layout(self._graph)
        nx.draw_networkx_nodes(self._graph, pos,
                               nodelist=self._graph.nodes(),
                               node_color='r',
                               node_size=50,
                               alpha=0.6)
        nx.draw_networkx_edges(self._graph, pos,
                               edgelist=self._graph.edges(),
                               width=1, alpha=0.1, edge_color='k')
        plt.show()

    def save_graph(self, output_file):

        nx.write_gml(self._graph, output_file)
