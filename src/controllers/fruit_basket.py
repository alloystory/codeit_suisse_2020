from flask import jsonify
import json

def solve(data):
    data = json.loads(data)
    weights = (50, 50, 0)
    counts = [count for _, count in data.items()]

    guess = 0
    for i in range(3):
        guess += counts[i] * weights[i]

    return jsonify(guess)