from flask import jsonify

def all_clean(arr):
    return all(map(lambda x: x == 0, arr))

def calculate(arr):
    num_moves = 0
    for i in range(1, len(arr)):
        num_moves += 1
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] -= 1

        if arr[i - 1] != 0:
            num_moves += arr[i - 1] * 2
            arr[i - 1] = 0
            arr[i] -= arr[i - 1]
            if arr[i] % 2 == 0:
                arr[i] = 0
            else:
                arr[i] = 1
            if all_clean(arr):
                num_moves -= 1
        
        if all_clean(arr):
            break

    return num_moves
        
def solve(data):
    results = {}
    for k, v in data["tests"].items():
        results[k] = calculate(v["floor"])

    return jsonify({
        "answers": results
    })