from flask import jsonify
# from itertools import permutations 

def score(genome):
    scores = []
    if len(genome) == 0:
        return 0
    
    if genome[:3] == "AAA":
        scores.append(-10 + score(genome[3:]))
    elif genome[:2] == "CC":
        scores.append(25 + score(genome[2:]))
    elif genome[:4] == "ACGT":
        scores.append(15 + score(genome[4:]))
    else:
        scores.append(score(genome[1:]))
    return max(scores)

# def permutate(a, c, g, t):
#     if a <= 0 and c <= 0 and g <= 0 and t <= 0:
#         return []
#     else:
#         permutations = []
#         if c > 2:
#             permutations = permutations + ["CC" + x for x in permutate(a, c - 2, g, t)]
#         elif a > 1 and c > 1 and g > 1 and t > 1:
#             permutations = permutations + ["ACGT" + x for x in permutate(a - 1, c - 1, g - 1, t - 1)]
#         else:
#             permutations = permutations + ["A" + x for x in permutate(a - 1, c, g, t)] + ["C" + x for x in permutate(a, c - 1, g, t)] + \
#                     ["G" + x for x in permutate(a, c, g - 1, t)] + ["T" + x for x in permutate(a, c, g, t - 1)]
#         return permutations

def permutate(count):
    groups = []
    a, c, g, t = count    
    if c == min((a,c,g,t)):
        while a >= 1 and c >= 1 and g >= 1 and t >= 1:
            groups.append("ACGT")
            a -= 1
            c -= 1
            g -= 1
            t -= 1

        while c >= 2:
            groups.append("CC")
            c -= 2
    else:
        while c >= 2:
            groups.append("CC")
            c -= 2

        while a >= 1 and c >= 1 and g >= 1 and t >= 1:
            groups.append("ACGT")
            a -= 1
            c -= 1
            g -= 1
            t -= 1

    while a > 0 and c > 0:
        groups.append("AC")
        a -= 1
        c -= 1

    while a > 0 and g > 0:
        groups.append("AG")
        a -= 1
        g -= 1

    while a > 0 and t > 0:
        groups.append("AT")
        a -= 1
        t -= 1

    for i in range(a, 0, -1):
        groups.insert(i, "A")

    for i in range(c, 0, -1):
        groups.insert(i, "C")

    for i in range(t, 0, -1):
        groups.insert(i, "T")

    for i in range(g, 0, -1):
        groups.insert(i, "G")

    return "".join(groups)

def count(gene):
    a, c, g, t = 0, 0, 0, 0
    for char in gene:
        if char == "A":
            a +=1
        elif char == "C":
            c += 1
        elif char == "G":
            g += 1
        elif char == "T":
            t += 1
    return a, c, g, t

def solve(data):
    tasks = data["list"]
    result = {
        "runId": data["runId"],
        "list": []
    }

    for task in tasks:
        gene = task["geneSequence"]
        

        # best_perm = gene
        # best_score = 0
        # for perm in permutations(gene):
        #     perm = "".join(perm)
        #     dri_score = score(perm)
        #     if dri_score > best_score:
        #         best_score = dri_score
        #         best_perm = perm
        print(score(permutate(count(gene))))
        result["list"].append({
            "id": task["id"],
            "geneSequence": permutate(count(gene))
        })

    return jsonify(result)