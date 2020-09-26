from flask import jsonify

def solve(data):
    weights = (50, 50, 50)
    counts = [count for _, count in data.items()]

    guess = 0
    for i in range(3):
        guess += counts[i] * weights[i]

    return jsonify(guess)