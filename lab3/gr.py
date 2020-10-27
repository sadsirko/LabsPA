import random
import networkx as nx
from matplotlib import pyplot as plt
#def create_graph()

def print_hi(num_of_nodes):

    chance = 0.3
    G = nx.gnp_random_graph(num_of_nodes, chance, 1, False)
    nx.draw_circular(G, node_color='red', node_size=100, with_labels=True)
    plt.show()
    return G
    #plt.savefig("Graph.png", format="PNG")


def print_edges(G):
    cnt = 0
    for j in nx.to_dict_of_dicts(G):
        for i in nx.to_dict_of_dicts(G)[cnt]:
            print(cnt, '-', i)
        cnt += 1