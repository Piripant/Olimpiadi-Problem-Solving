# Fatto da Davide Barbini

import operator

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node[0] not in path:
                newpaths = find_all_paths(graph, node[0], end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def processPaths(graph, costs, paths, budget=1, minlen=0, maxlen=1000):
    outpaths = []

    # Per ogni percorso nei percorsi
    for path in paths:
        # Ripristina la distanza e il budget
        distance = 0
        path_bud = budget
        request_break = False

        # Per ogni nodo nel percorso
        for i in range(1, len(path)): # Inizia dal secondo nodo del percorso
            prev_node_neigh = graph[path[i-1]] # Il nodo precedente in graph
            node = path[i] # Il nome del nodo corrente

            if node in costs: # Se il nodo ha un costo
                path_bud -= costs[node]
                if path_bud <= 0:
                    request_break = True
                    break

            for neig_node in prev_node_neigh:
                # Trova il nodo nei vicini del nodo precedente
                if neig_node[0] == node:
                    distance += neig_node[1]

                    if distance >= maxlen:
                        print('Nope!')
                        request_break = True
                        break

        # Se non c'è nessuna richiesta di saltare questo percorso (è troppo lungo) e non è troppo corto
        if not request_break and distance >= minlen:
            outpaths.append(path + ['bud'] + [path_bud] + ['dist'] + [distance])

    sortpath = sorted(outpaths, key=operator.itemgetter(-1), reverse=True) # itemgetter(-2) to order by budgets
    return sortpath

# usage: add_node(nodes_dictionary, start_point, end_point, distance, oneway?)
def add_node(nodes={}, name="", conn="", dist=1, oneway=False): # Sintax: add_node(nodes, "n1", "n2", 2)
    if name not in nodes:
        nodes[name] = []
    if conn not in nodes:
        nodes[conn] = []

    nodes[name].append([conn, dist])
    if not oneway:
        nodes[conn].append([name, dist])

def add_cost(costs={}, node="", cost=0):
    costs[node] = cost

costs = {}
nodes = {}

# Utilizzo per nodi a senso unico: add_node(dizionario_nodes, 'punto_di_partenza', 'punto_di_arrivo', distanza, True)
# Utilizzo per nodi a senso non-unico: add_node(dizionario_nodes, 'punto_di_partenza', 'punto_di_arrivo', distanza, False)

add_node(nodes, "n1", "n8", 13)
add_node(nodes, "n1", "n5", 12)

# Utilizzo: allpaths = find_all_paths(nodes, partenza, arrivo)
allpaths = find_all_paths(nodes, "n3", "n8")

# Utilizzo: processPaths(dizionario_nodes, dizionario_costs, varibile_paths, budget, lunghezza_minima, lunghezza_massima)
sortpaths = processPaths(nodes, costs, allpaths, budget=1, minlen=50, maxlen=9000)

print(sortpaths)

for path in sortpaths:
    print(path)
