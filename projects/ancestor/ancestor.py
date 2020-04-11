from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):

    # create instance of Graph
    ancestor_graph = Graph()

    # iterate through ancestors, add pairs (parent, child) verts to graph
    for anc in ancestors:
        parent, child = anc

        # check to see if parent not in graph
        if parent not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(parent)

        # check to see if child not in graph
        if child not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(child)
        # add edge between child and parent
        ancestor_graph.add_edge(child, parent)

    # if the starting node has no parents, return -1
    if len(ancestor_graph.get_neighbors(starting_node)) == 0:
        return -1

    # create queue
    q = Queue()

    # enqueue starting node and interval between parent,child
    q.enqueue([starting_node, 0])

    # keep track of visited ancestors
    visited_ancestors = {}

    while q.size() > 0:
        parent_searcher, anc_interval = q.dequeue()

        # check if parent_searcher in visitd_ancestors,
        # add interval to visited_ancestors
        if anc_interval in visited_ancestors:
            visited_ancestors[anc_interval].append(parent_searcher)
        else:
            visited_ancestors[anc_interval] = [parent_searcher]

        # retrieve ancestor of parent_searcher
        possible_parents = ancestor_graph.get_neighbors(parent_searcher)
        if len(possible_parents) > 0:
            for parent in possible_parents:
                q.enqueue([parent, anc_interval + 1])

    # look for largest key then return smallest id based off of key
    lrg_interval = max(visited_ancestors.keys())
    return min(visited_ancestors[lrg_interval])
