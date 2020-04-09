"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import sys


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        v1_edge_set = self.vertices[v1]
        v1_edge_set.add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            curr_node = q.dequeue()

            if curr_node not in visited:
                print(curr_node)
                visited.add(curr_node)
                neighbors = self.get_neighbors(curr_node)

                for neighbor in neighbors:
                    q.enqueue(neighbor)

        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            curr_node = s.pop()

            if curr_node not in visited:
                print(curr_node)

                visited.add(curr_node)

                neighbors = self.get_neighbors(curr_node)

                for neighbor in neighbors:
                    s.push(neighbor)

        return visited

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check if visited exists
        if starting_vertex in visited:
            return
        else:
            print(starting_vertex)
            visited.add(starting_vertex)
            # iterate through neighbors of starting_vertex
            for n in self.get_neighbors(starting_vertex):
                # call func
                self.dft_recursive(n, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        q = Queue()

        # enqueue starting_vertex into queue
        q.enqueue([starting_vertex])

        # create empty set to track visited vertices
        visited = set()

        # iterate through all until all verts are visited
        while q.size() > 0:
            path = q.dequeue()
            vtx = path[-1]

            if vtx not in visited:
                if vtx == destination_vertex:
                    return path
                visited.add(vtx)
                for nxt_vtx in self.get_neighbors(vtx):
                    new_path = list(path)
                    new_path.append(nxt_vtx)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        s = Stack()

        # push starting_vertex onto stack
        s.push([starting_vertex])

        # create empty set to track visited vertices
        visited = set()

        # iterate through until all verts have been visited
        while s.size() > 0:
            path = s.pop()
            vtx = path[-1]

            if vtx not in visited:
                if vtx == destination_vertex:
                    return path
                visited.add(vtx)
                for nxt_vtx in self.get_neighbors(vtx):
                    # copy path
                    new_path = list(path)
                    new_path.append(nxt_vtx)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
