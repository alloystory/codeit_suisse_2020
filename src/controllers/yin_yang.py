from flask import jsonify

memoize = dict()
def solver(n, k, E):
    if k == 0:
        return 0
    else:
        num_yang = 0
        possible_orderings = set()
        for x in range(n):
            if E[x] == "Y" or E[n - x - 1] == "Y":
                num_yang += 1
            if E[x] == "Y":
                possible_orderings.add(E[:x] + E[(x + 1):])
            elif E[n - x - 1] == "Y":
                possible_orderings.add(E[:(n - x - 1)] + E[(n - x):])
        probability = num_yang / n

        prob_possible_ordering = 0
        for order in possible_orderings:
            if order in memoize:
                prob = memoize[order]
            else:
                prob = solver(n - 1, k - 1, order)
                memoize[order] = prob
            prob_possible_ordering += (prob / len(possible_orderings))

        return probability + prob_possible_ordering

def solve(data):
    n = data["number_of_elements"]
    k = data["number_of_operations"]
    E = data["elements"]

    print("Data:", (n, k, E))

    return jsonify({
        "result": solver(n, k, E)
    })