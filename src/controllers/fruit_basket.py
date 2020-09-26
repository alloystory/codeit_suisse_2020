from flask import jsonify
import json

def solve(data):
    data = json.loads(data)
    weights = (50, 40, 0)
    print(data)
    counts = [count for _, count in data.items()]

    guess = 0
    for i in range(3):
        guess += counts[i] * weights[i]

    return jsonify(guess)