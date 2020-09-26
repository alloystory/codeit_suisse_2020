import sys

def compare(genome1, genome2):
    num_diff = 0
    num_first_diff = 0

    zipped_instructions = zip(genome1.split("-"), genome2.split("-"))
    for instruction in zipped_instructions:
        instr1, instr2 = instruction
        for i in range(len(instr1)):
            if instr1[i] != instr2[i]:
                num_diff += 1
                if i == 0:
                    num_first_diff += 1
    
    if num_first_diff > 1:
        return (num_diff, True)
    return (num_diff, False)

def dfs(adj_list, node, visited):
    copied_visited = set([x for x in visited])
    copied_visited.add(node)
    paths = []

    if len(adj_list[node]) == 0:
        return paths
    else:
        for neighbour in adj_list[node]:
            if neighbour in copied_visited:
                continue
            path = [node] + dfs(adj_list, neighbour, copied_visited)
            paths.append(order)

    return order

def dfs(adj_list, node):
    paths = []
    def inner(adj_list, node, visit_order):
        copied_visit_order = [x for x in visit_order]
        copied_visit_order.append(node)
        
        if len(adj_list[node]) == 0:
            paths.append(copied_visit_order)
        else:
            for neighbour in adj_list[node]:
                if neighbour in copied_visit_order:
                    continue
                inner(adj_list, neighbour[0], copied_visit_order)

    inner(adj_list, node, [])
    return paths    

def solve(data):
    infected = data["infected"]
    origin = data["origin"]
    clusters = data["cluster"]

    # node_names = dict()
    # node_names[infected["name"]] = 0
    # node_names[origin["name"]] = 1
    # for i, cluster in enumerate(clusters):
    #     node_names[cluster["name"]] = i + 2

    adj_list = dict()
    adj_list[infected["name"]] = []
    adj_list[origin["name"]] = []
    for cluster in clusters:
        adj_list[cluster["name"]] = []

    # Infected -> Origin
    dist, is_non_silent = compare(infected["genome"], origin["genome"])
    adj_list[infected["name"]].append((origin["name"], dist, is_non_silent))

    for cluster in clusters:
        # Infected -> Cluster
        dist, is_non_silent = compare(infected["genome"], cluster["genome"])
        adj_list[infected["name"]].append((cluster["name"], dist, is_non_silent))
        
        # Cluster -> Origin
        dist, is_non_silent = compare(cluster["genome"], origin["genome"])
        if dist > 0:
            adj_list[cluster["name"]].append((origin["name"], dist, is_non_silent))

    for i in range(len(clusters)):
        for j in range(i, len(clusters)):
            # Cluster -> Cluster
            dist, is_non_silent = compare(clusters[i]["genome"], clusters[j]["genome"])
            if dist > 0:
                adj_list[clusters[i]["name"]].append((clusters[j]["name"], dist, is_non_silent))
                adj_list[clusters[j]["name"]].append((clusters[i]["name"], dist, is_non_silent))

    print(adj_list)
    print(dfs(adj_list, infected["name"]))
    return {"hello":"hello"}
