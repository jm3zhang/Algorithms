#!/usr/bin/python
from queue import Queue
from collections import deque

def BFS(start,end): 
    y = start[1]
    x = start[0]
    end_x = end[0]
    end_y = end[1]
    Map = maze_mapping([y,x], [end_y,end_x])
    num_of_nodes_visitied = 0

    fringe = deque( [(y,x,None)])

    while (len(fringe)>0): 
        # print(list(fringe.queue))
        node = fringe.popleft()
        num_of_nodes_visitied = num_of_nodes_visitied + 1 
        # print(node)
        y = node[1] 
        x = node[0] 
        if Map[y][x] == 3:  
            path = [] 
            output = []
            cost = 0
            while(node != None): 
                if cost % 2 != 0:
                    path.append((node[1],node[0])) 
                else:
                    path.append((node[0],node[1])) 
                node = node[2] 
                cost = cost + 1
            print("Cost of BFS is " + str(cost))
            print("Number of nodes visited " + str(num_of_nodes_visitied))
            for i in reversed(path):
                output.append(i)
            print("Path for BFS (x, y):")
            return output

            # path.append((node[0],node[1])) 
            # node = fringe.get() 
            # return path  
        # print(Map[x][y])
        if (Map[y][x] == 1 or Map[y][x] == 4): 
            continue 

        Map[y][x] = 4 
        for i in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]: 
            if (i[0] >= 0 and i[1] >= 0 and i[0] < 25 and i[1] < 25):
                fringe.append((i[0],i[1],node))
    return "The given points are unsolvable!"
    

def DFS(start, map):
    output = []
    output = recursive_DFS(start, map)
    final_output = []
    cost  = 0

    for i in reversed(output):
        final_output.append((i[1], i[0])) 
        cost = cost + 1

    print("Cost of DFS is " + str(cost))
    print("Path for DFS (x, y):")
    return final_output

def recursive_DFS(start, map): 
    y = start[0]
    x = start[1]

    if map[y][x] == 3: 
        return [(x, y)]
    if (map[y][x] == 1 or map[y][x] == 4): 
        return [] 
    map[y][x] = 4

    for i in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]: 
        if (i[0] >= 0 and i[1] >= 0 and i[0] < 25 and i[1] < 25):
            next_level = recursive_DFS([i[0], i[1]], map)
            if (len(next_level) > 0):
                next_level.append((x, y))
                return next_level
     
    return []

def Astar(start,end): 
    y = start[1]
    x = start[0]
    end_x = end[0]
    end_y = end[1]
    Map = maze_mapping([y,x], [end_y,end_x])
    num_of_nodes_visitied = 0

    fringe = deque( [(y,x,None)])

    while (len(fringe)>0): 
        # print(list(fringe.queue))
        node = fringe.popleft()
        num_of_nodes_visitied = num_of_nodes_visitied + 1 
        # print(node)
        y = node[1] 
        x = node[0] 
        if Map[y][x] == 3:  
            path = [] 
            output = []
            cost = 0
            while(node != None): 
                if cost % 2 != 0:
                    path.append((node[1],node[0])) 
                else:
                    path.append((node[0],node[1])) 
                node = node[2] 
                cost = cost + 1
            print("Cost of A* is " + str(cost))
            print("Number of nodes visited " + str(num_of_nodes_visitied))
            for i in reversed(path):
                output.append(i)
            print("Path for A* (x, y):")
            return output

            # path.append((node[0],node[1])) 
            # node = fringe.get() 
            # return path  
        # print(Map[x][y])
        if (Map[y][x] == 1 or Map[y][x] == 4): 
            continue 

        Map[y][x] = 4 
        for i in [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]: 
            if (i[0] >= 0 and i[1] >= 0 and i[0] < 25 and i[1] < 25):
                fringe.append((i[0],i[1],node))
    return "The given points are unsolvable!"


def maze_mapping(start, end): 
    # 0 = path
    # 1 = wall
    # 2 = starting point
    # 3 = ending point
    # 4 = visited nodes

    map = [
        [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0], 
        [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1],
        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
        [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
        [0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0],
        [1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0],
        [1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    if (map[start[0]][start[1]] == 1):
        return "Map error"
    else:
        map[start[0]][start[1]] = 2

    if (map[end[0]][end[1]] == 1):
        return "Map error"
    else:
        map[end[0]][end[1]] = 3

    return map

def main():

    print(BFS([2,13], [23,5]))
    DFS_map = maze_mapping([13,2],[23,5])
    print(DFS([2,13],DFS_map))
    print(Astar([2,13], [23,5]))


if __name__ == '__main__':
    main()