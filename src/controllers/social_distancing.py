import operator as op
from flask import jsonify
from itertools import permutations
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom 

def find_seating(seats, people, spaces):
    min_seats = people + (people - 1) * spaces
    if seats < min_seats:
        return 0

    n = people + 1
    r = seats - min_seats
    return ncr(n + r - 1, r)

def solve(data):
    tests = data["tests"]
    results = {}
    for key, test in tests.items():
        results[key] = find_seating(**test)

    return jsonify({
        "answers": results
    })