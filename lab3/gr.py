import random
import networkx as nx
from matplotlib import pyplot as plt


def create_gr(num_of_nodes,chance):

    G = nx.gnp_random_graph(num_of_nodes, chance, 1, False)
    nx.draw_random(G, node_color='red', node_size=100, with_labels=True)
    plt.show()
    return G
    #plt.savefig("Graph.png", format="PNG")


def avg_edges(G):
    sum = 0
    cnt = 0
    for j in nx.to_dict_of_dicts(G):
        for i in nx.to_dict_of_dicts(G)[cnt]:
            #print(cnt, '-', i)
            sum += 1
        cnt += 1
    print('avg_eges', sum / cnt)