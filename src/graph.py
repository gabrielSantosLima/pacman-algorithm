class Vertex:
    ID: int
    vertices: list['Vertex', str]

    def __init__(self, ID: int):
        self.ID = ID
        self.vertices = []

    def __get_vertex_id(self, vertex: 'Vertex'):
        return vertex[0].ID

    def __str__(self) -> str:
        ids = list(map(self.__get_vertex_id, self.vertices))
        return f'{self.ID} - {ids}'

class Graph:
    size: int
    length: int
    vertices: list[Vertex]

    def __init__(self, size: int):
        self.size = size
        self.length = 0
        self.vertices = [None] * size

    def add_vertex(self, ID: int):
        if self.length == self.size:
            return
        new_vertex = Vertex(ID)
        self.vertices[self.length] = new_vertex
        self.length += 1
        return new_vertex

    def get_vertex(self, ID: int):
        for vertex in self.vertices:
            if vertex.ID == ID:
                return vertex.vertices
        return None

    def has_key(self, ID: int):
        for vertex in self.vertices:
            if vertex.ID == ID:
                return True
        return False

    def add_edge(self, source: Vertex, target: Vertex, direction: str):
        for vertex in source.vertices:
            if vertex[0].ID == target.ID:
                return
        source.vertices.append([target, direction])

    def get_edges(self, source:Vertex):
        return source.vertices


    def remove_edge(self, source: Vertex, target: Vertex):
        source.vertices = list(filter(lambda vertex: vertex.ID != target.ID, source.vertices))

    def remove_vertex(self, ID: int):
        if self.length == 0:
            return
        self.vertices = list(filter(lambda vertex: vertex == None or vertex.ID != ID, self.vertices))
        for vertex in self.vertices:
            if vertex is not None:
                vertex.vertices = list(filter(lambda vertex: vertex.ID != ID, vertex.vertices))

    def print_vertices(self):
        for vertex in self.vertices:
            print(vertex)