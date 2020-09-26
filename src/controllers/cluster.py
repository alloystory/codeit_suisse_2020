from flask import jsonify

def solve(data):
    adj_list = dict()
    coor_ones = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "*":
                continue
            elif data[i][j] == "1":
                coor_ones.append(str((i, j)))

            if str((i, j)) not in adj_list:
                adj_list[str((i, j))] = []

            for x in range(max(0, i - 1), min(i + 2, len(data))):
                for y in range(max(0, j - 1), min(j + 2, len(data[i]))):
                    if data[x][y] == "*" or (x, y) == (i, j):
                        continue
                    adj_list[str((i, j))].append(str((x, y)))

    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor in visited:
                continue
            dfs(neighbor)
    
    num_components = 0
    for coor in coor_ones:
        if coor not in visited:
            num_components += 1
            dfs(coor)

    return jsonify({
        "answer": num_components
    })