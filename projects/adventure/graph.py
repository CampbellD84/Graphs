"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = {}

    def add_edge(self, v1, v2, nav_direction):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][nav_direction] = v2

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    # def bft(self, starting_vertex):
    #     """
    #     Print each vertex in breadth-first order
    #     beginning from starting_vertex.
    #     """
    #     q = Queue()
    #     q.enqueue(starting_vertex)
    #     visited = set()

    #     while q.size() > 0:
    #         curr_node = q.dequeue()

    #         if curr_node not in visited:
    #             print(curr_node)
    #             visited.add(curr_node)
    #             neighbors = self.get_neighbors(curr_node)

    #             for neighbor in neighbors:
    #                 q.enqueue(neighbor)

    #     return visited

    # def dft(self, starting_vertex):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.
    #     """
    #     s = Stack()
    #     s.push(starting_vertex)
    #     visited = set()

    #     while s.size() > 0:
    #         curr_node = s.pop()

    #         if curr_node not in visited:
    #             print(curr_node)

    #             visited.add(curr_node)

    #             neighbors = self.get_neighbors(curr_node)

    #             for neighbor in neighbors:
    #                 s.push(neighbor)

    #     return visited

    # def dft_recursive(self, starting_vertex, visited=set()):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.

    #     This should be done using recursion.
    #     """
    #     # check if starting_vertex is not in visited
    #     if starting_vertex not in visited:
    #         visited.add(starting_vertex)

    #         print(starting_vertex)
    #         adj_verts = self.get_neighbors(starting_vertex)
    #         # iterate through neighbors of starting_vertex
    #         for n in adj_verts:
    #             # call func
    #             self.dft_recursive(n, visited)

    # def bfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing the shortest path from
    #     starting_vertex to destination_vertex in
    #     breath-first order.
    #     """
    #     # create a queue
    #     q = Queue()

    #     # enqueue starting_vertex into queue
    #     q.enqueue([starting_vertex])

    #     # create empty set to track visited vertices
    #     visited = set()

    #     # iterate through all until all verts are visited
    #     while q.size() > 0:
    #         path = q.dequeue()
    #         vtx = path[-1]

    #         if vtx not in visited:
    #             if vtx == destination_vertex:
    #                 return path
    #             visited.add(vtx)
    #             for nxt_vtx in self.get_neighbors(vtx):
    #                 new_path = list(path)
    #                 new_path.append(nxt_vtx)
    #                 q.enqueue(new_path)

    # def dfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     """
    #     # create a stack
    #     s = Stack()

    #     # push starting_vertex onto stack
    #     s.push([starting_vertex])

    #     # create empty set to track visited vertices
    #     visited = set()

    #     # iterate through until all verts have been visited
    #     while s.size() > 0:
    #         path = s.pop()
    #         vtx = path[-1]

    #         if vtx not in visited:
    #             if vtx == destination_vertex:
    #                 return path
    #             visited.add(vtx)
    #             for nxt_vtx in self.get_neighbors(vtx):
    #                 # copy path
    #                 new_path = list(path)
    #                 new_path.append(nxt_vtx)
    #                 s.push(new_path)

    # def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     if starting_vertex in visited:
    #         return

    #     visited.add(starting_vertex)
    #     path_curr = path.copy()
    #     path_curr.append(starting_vertex)

    #     if starting_vertex == destination_vertex:
    #         return path_curr

    #     for n in self.get_neighbors(starting_vertex):
    #         nxt_path = self.dfs_recursive(
    #             n, destination_vertex, path_curr, visited)
    #         if nxt_path:
    #             return nxt_path
