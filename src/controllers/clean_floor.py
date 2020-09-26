from flask import jsonify

def all_clean(arr):
    return all(map(lambda x: x == 0, arr))

def calculate(arr):
    print("Data:", arr)
    i = 0
    num_moves = 0
    while i < (len(arr) - 1):
        i += 1
        num_moves += 1
        arr[i] = not arr[i]

        if arr[i - 1] == 1:
            arr[i - 1] = 0
            num_moves += 1
            if all_clean(arr):
                break
            num_moves += 1
        elif all_clean(arr):
            break
    return num_moves
        
def solve(data):
    results = {}
    for k, v in data["tests"].items():
        results[k] = calculate(v["floor"])

    return jsonify({
        "answers": results
    })