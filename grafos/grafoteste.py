class Grafo:
    def __init__(self):
        self.vertices = {}
 
    def adicionar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}
 
    def adicionar_aresta(self, u, v, peso=0):
        if u not in self.vertices:
            self.vertices[u] = {}
        self.vertices[u][v] = peso
 
    def remover_aresta(self, u, v):
        if u in self.vertices and v in self.vertices[u]:
            del self.vertices[u][v]
 
    def remover_vertice(self, v):
        if v in self.vertices:
            del self.vertices[v]
        for u in self.vertices:
            if v in self.vertices[u]:
                del self.vertices[u][v]
 
    def obter_vertices(self):
        return list(self.vertices.keys())
 
    def obter_arestas(self):
        arestas = []
        for u in self.vertices:
            for v in self.vertices[u]:
                arestas.append((u, v, self.vertices[u][v]))
        return arestas
 
    def obter_adjacentes(self, v):
        if v in self.vertices:
            return list(self.vertices[v].keys())
 
    def existe_aresta(self, u, v):
        return u in self.vertices and v in self.vertices[u]


g = Grafo()
g.adicionar_vertice('A')
g.adicionar_vertice('B')
g.adicionar_vertice('C')
g.adicionar_vertice('D')
g.adicionar_aresta('A', 'B', 1)
g.adicionar_aresta('B', 'C', 2)
g.adicionar_aresta('C', 'D', 3)
