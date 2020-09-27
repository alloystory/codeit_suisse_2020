from flask import jsonify

def all_clean(arr):
    return all(map(lambda x: x == 0, arr))

def calculate(arr):
    print("Data:", arr)
    num_moves = 0
    if arr[0] > 0:
        num_moves += arr[0] * 2
        if arr[0] == arr[1]:
            arr[1] = 0
        else:
            arr[1] -= abs(arr[1] - arr[0])
        if arr[1] < 0:
            arr[1] = abs(arr[1]) % 2 == 0

    for i in range(1, len(arr)-1):
        num_moves += 1
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] -= 1
        value = arr[i]
        num_moves += value * 2
        if arr[i] == arr[i+1]:
            arr[i+1] = 0
        else:
            arr[i+1] -= abs(arr[i+1] - arr[i])
        if arr[i+1] < 0:
            arr[i+1] = abs(arr[i+1]) % 2 == 0

    if arr[-1] > 0:
        if arr[-1] % 2 == 0:
            num_moves += arr[-1] * 2
        else:
            num_moves += arr[-1] * 2 - 1
    return num_moves
        
def solve(data):
    results = {}
    for k, v in data["tests"].items():
        results[k] = calculate(v["floor"])

    return jsonify({
        "answers": results
    })