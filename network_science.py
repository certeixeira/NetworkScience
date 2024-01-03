# %%
import networkx as nx
# %%
nx.__version__
# %%
# CRIAÇÃO E LEITURA DE REDES COM O NETWORKX

g = nx.Graph()
print(g)
# %%
# ADICIONANDO NÓS(VÉRTICES)

g.add_node(1)
print(g)

# %%
g.add_nodes_from([2, 3])
print(g)
# %%

g = nx.Graph()
g.add_nodes_from(range(10))
print(g)
# %%
# ADICIONANDO ARESTAS(RELACIONAMENTOS)

g.add_edge(0,1)
print(g)
# %%

g.add_edges_from([
    (1, 2),
    (1, 9),
    (2, 3)
])
print(g)
# %%
# REMOVENDO ELEMENTOS

g.clear()
print(g)
# %%

g.add_nodes_from(range(10))
g.add_edges_from([
    (1, 2),
    (1, 9),
    (2, 3)
])
print(g)
# %%

g.remove_node(5)
print(g)
# %%

g.remove_edge(1, 2)
print(g)
# %%

# USANDO CONSTRUTOR


# %%
#Lista de arestas

edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D')
]

H = nx.Graph(edges)
print(H)
# %%
# Adjacências   

adjacency_dict = {
    'A': ['B', 'C'],
    'B': ['D'],
}

H = nx.Graph(adjacency_dict)
print(H)
# %%
# Rede direcionada

adjacency_dict = {
    'A': ['B', 'C'],
    'B': ['D'],
}

D = nx.DiGraph(adjacency_dict)
print(D)
# %%
# Exercício

import matplotlib.pyplot as plt

# Definindo o conjunto de arestas
edges = [(0, 1), (4, 2), (1, 3), (3, 4), (2, 0)]

# Criando o grafo não direcionado
G = nx.Graph()
G.add_edges_from(edges)

# Calculando a distância e o caminho mais curto entre os nós 0 e 4
distance = nx.shortest_path_length(G, source=0, target=4)
shortest_path = nx.shortest_path(G, source=0, target=4)

# Desenhando o grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray')
nx.draw_networkx_edges(G, pos, edgelist=[(0, 1), (4, 2), (1, 3), (3, 4), (2, 0)], edge_color='black', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(0, 1): ' ', (4, 2): ' ', (1, 3): ' ', (3, 4): ' ', (2, 0): ' '}, font_color='red')

# Exibindo o gráfico
plt.show()

# Exibindo os resultados
print("Distância:", distance)
print("Caminho mais curto:", shortest_path)



# %%
# Qual a densidade da rede não direcionada dada por V = {0, 1, 2, 3} e E = {(0, 2), (1, 2), (1, 0)}? 
# E qual seria sua densidade se a rede fosse direcionada?

# Definindo os vértices e as arestas para a rede não direcionada
V = {0, 1, 2, 3}
E = {(0, 2), (1, 2), (1, 0)}

# Criando o grafo não direcionado
G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)

# Calculando a densidade para a rede não direcionada
density_undirected = nx.density(G)

# Criando o grafo direcionado
G_directed = nx.DiGraph()
G_directed.add_nodes_from(V)
G_directed.add_edges_from(E)

# Calculando a densidade para a rede direcionada
density_directed = nx.density(G_directed)

# Exibindo os resultados
print(f"Densidade da rede não direcionada: {density_undirected}")
print(f"Densidade da rede direcionada: {density_directed}" )
# %%
