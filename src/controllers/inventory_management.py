from flask import jsonify
import sys

def edit_ops(str1, str2):
    dp_table = []
    for _ in range(len(str1) + 1):
        row = []
        for _ in range(len(str2) + 1):
            row.append([0, ""])
        dp_table.append(row)

    for j in range(len(str2) + 1):
        dp_table[0][j][0] = j
        if j > 0:
            dp_table[0][j][1] += "".join(["+" + c for c in str2[:j]])

    for i in range(1, len(str1) + 1):
        dp_table[i][0][0] = i
        if i > 0:
            dp_table[i][0][1] += "".join(["-" + c for c in str1[:i]])

        for j in range(1, len(str2) + 1):
            insertion = dp_table[i][j - 1][0] + 1
            insertion_ops = dp_table[i][j - 1][1] + "+{}".format(str2[j - 1])

            deletion = dp_table[i - 1][j][0] + 1
            deletion_ops = dp_table[i - 1][j][1] + "-{}".format(str1[i - 1])

            substitution = dp_table[i - 1][j - 1][0] + int(str1[i - 1].lower() != str2[j - 1].lower())
            substitution_ops = dp_table[i - 1][j - 1][1] + "{}".format(str2[j - 1])

            min_cost = insertion
            min_ops = insertion_ops
            for op in zip([deletion, substitution], [deletion_ops, substitution_ops]):
                if op[0] < min_cost:
                    min_cost = op[0]
                    min_ops = op[1]
            dp_table[i][j][0] = min_cost
            dp_table[i][j][1] = min_ops
    return dp_table[len(str1)][len(str2)]

def solve(data):
    results = []
    for entry in data:
        query = entry["searchItemName"]
        items = entry["items"]
        scores = [edit_ops(query, item) for item in items]
        scores = sorted(scores, key = lambda x: (x[0], x[1]))

        results.append({
            "searchItemName": query,
            "searchResult": [score[1] for score in scores[:10]]
        })

    return jsonify(results)
