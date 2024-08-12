def aStarAlgo(start_node,stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    while len(open_set)>0:
        n = None
        for v in open_set:
            if n is None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        if n==stop_node or n is None or graph_nodes[n] is None :
            break
        else:
            for m,weight in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m] = g[n]+weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(n)
                            open_set.add(m)
            open_set.remove(n)
            closed_set.add(n)
    if n is None:
        print('Path Does not Exsit')
        return None
    if n == stop_node:
        path = []
        while parents[n]!=n:
            path.append(n)
            n = parents[n]
        path.append(start_node)
        path.reverse()
        print('path found',path)
        return path
    print('Path Does Not Exist')
    return None 
def get_neighbours(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None
def heuristic(n):
    h_dist = {
        'A' :11,
        'B':6,
        'C':99,
        'D':1,
        'E':7,
        'G':0
        }
    return h_dist[n]
graph_nodes = {
    'A':[('B',2),('E',3)],
    'B':[('A',2),('C',1),('G',9)],
    'C':[('B',1)],
    'D':[('E',6),('G',1)],
    'E':[('A',3),('D',6)],
    'G':[('B',9),('D',1)]
    }
print('Following is the A* Algorithm')
aStarAlgo('A','G')
