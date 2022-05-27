#!/usr/bin/env python3
"""
we will use the queue module to implement a FIFO queue.
- you can create a queue with Q = queue.Queue(max_size)
- you can inject v onto the queue with Q.put(v)
- you can eject from the queue with Q.get()
"""
import queue


def bfs(adj, start):
    """
    Implementing breadth-first search to compute distances from
    a start vertex s to every other vertex.
    """
    # example to demonstrate list of lists (you can delete)
    num_vertices = len(adj)  # the number of vertices
    dist = [None] * num_vertices
    dist[start] = 0
    Q = queue.Queue(num_vertices)
    Q.put(start)

    while not Q.empty():
        u = Q.get()
        for v in adj[u]:
            if dist[v] is None:
                Q.put(v)
                dist[v] = dist[u] + 1

    return dist
    

def shortest_v_paths(adj, vertex_s):
    """
    Input:  1) A directed graph represented as an adjacency list adj:
                adj[1] is a list containing the neighbors of vertex 1
                (by default, vertices are numbered from 0 to |V| - 1)
            2) a vertex_s in 0,...,|V|-1

    Output: a matrix of distances, where M[i,j] gives the length of the shortest
            path from vertex i to vertex j passing through vertex_s
    """
    num_vertices = len(adj)
    # first, compute shortest distance from vertex_s to every
    # other vertex
    dist_from_s = bfs(adj, vertex_s)
    
    # next, compute the distance from every vertex to vertex_s
    # an efficient way to do this is create a new graph where each
    # edge points in the opposite direction
    reverse_adj = list(list() for i in range(num_vertices))
    for vertex1, neighbors in enumerate(adj):
        for vertex2 in neighbors:
            reverse_adj[vertex2].append(vertex1)
    # now, compute dist from vertex_s to all others        
    dist_to_s = bfs(reverse_adj, vertex_s)

    # finally, loop through all vertices and fill in distances
    dist = list()
    for vertex1 in range(num_vertices):
        dists_vertex1 = list()
        for vertex2 in range(num_vertices):
            dist_1_to_2 = dist_to_s[vertex1] + dist_from_s[vertex2]
            dists_vertex1.append(dist_1_to_2)
        dist.append(dists_vertex1)

    return dist


def main():
    """
    A simple test case for your algorithm with four vertices 0,1,2,3
    """
    adj = [[1],
           [2, 3],
           [1, 3],
           [0]]

    # test case:
    print(shortest_v_paths(adj, 3))
    # In this graph, 
    # 1) the shortest path from 3 to 3 passing through 3 has length 0
    # 2) The shortest path from 0 to 2 passing through 3 is
    # 0 -> 1 -> 3 -> 0 -> 1 -> 2 having a length of 5


if __name__ == '__main__':
    main()
