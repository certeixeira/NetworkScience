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

## CÁLCULO DO GRAU
# Rede não Direcionada

# %%

G = nx.star_graph(9)
nx.draw_networkx(G)

# %%
G.nodes
# %%
G.edges
# %%

# dicionário com o grau de cada nó:
G.degree
# %%
G.degree[0]
# %%
G.degree[1]
# %%

for node, degree in G.degree:
    print(f'Nó: {node}, grau {degree}')
# %%
for node, degree in G.degree:
    if degree > 1:
        print(f'Nó: {node}, grau {degree}')
# %%
list(G.adj[0])
# %%
list(G.adj[1])

# %%
# Rede Direcionada

# %%
G = nx.gnc_graph(6)
nx.draw_circular(G, with_labels=True)

# %%
G.degree(0)
# %%
G.in_degree(0)
# %%
G.out_degree(0)
# %%
# lista de adjacência vazia:
# %%
G.adj[0]
# %%

# Rede com peso:
# %%

G = nx.path_graph(range(5))
nx.set_edge_attributes(G, 1, 'weight')
G.add_edge(2, 4, weight=2)
G[2][3]['weight'] = 2
# %%

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# %%
G.degree(2, weight='weight')
# %%
G.degree(3, weight='weight')
# %%
G.degree(0, weight='weight')
# %%
