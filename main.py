import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(range(1, 11))
G.add_edges_from([(1, 2), (5, 9), (5, 4), (5, 1), (10, 6), (5, 7), (10, 3), (10, 2), (8, 1)])
plt.figure("Graph")
color_map = []
for i in range(0, G.number_of_nodes()):
    if i == 2:
        color_map.append('gold')
    elif i == 4:
        color_map.append('lightgreen')
    else:
        color_map.append('lightgray')
nx.draw_networkx(G, node_color=color_map, pos=nx.spring_layout(G, iterations=100), arrows=False, with_labels=True)
plt.show()
