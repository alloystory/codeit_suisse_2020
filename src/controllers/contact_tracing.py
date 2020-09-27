import sys
from flask import jsonify

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

def solve(data):
    infected = data["infected"]
    origin = data["origin"]
    clusters = data["cluster"]

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

    def dfs(node):
        visited = set()
        all_paths = []
        def inner(curr_node, path, max_dist):
            visited.add(curr_node)

            if not adj_list[curr_node]:
                path.append(curr_node)
                all_paths.append((max_dist, path))
            else:
                for neighbor in adj_list[curr_node]:
                    copied_path = [x for x in path]
                    is_non_silent = neighbor[2]
                    if is_non_silent:
                        copied_path.append(curr_node + "*")
                    else:
                        copied_path.append(curr_node)

                    if neighbor in visited:
                        continue
                    inner(neighbor[0], copied_path, max(max_dist, neighbor[1]))
        inner(node, [], 0)
        return all_paths

    paths = dfs(infected["name"])

    min_path_weight = sys.maxsize
    min_paths = []
    for path in paths:
        if path[0] < min_path_weight:
            min_paths = []
        if path[0] <= min_path_weight:
            min_path_weight = path[0]
            min_paths.append(" -> ".join(path[1]))
    return jsonify(min_paths)
