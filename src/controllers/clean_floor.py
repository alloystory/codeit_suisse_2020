from flask import jsonify

def all_clean(arr):
    return all(map(lambda x: x == 0, arr))

def calculate(arr):
    print("Data:", arr)
    ans = 0
    n = len(arr)
    if arr[0] > 0:
        value = arr[0]
        ans += value * 2
        if arr[0] == arr[1]:
            arr[1] = 0
        else:
            arr[1] -= abs(arr[1] - arr[0])
        if arr[1] < 0:
            arr[1] = abs(arr[1]) % 2 == 0

    for i in range(1, n-1):
        ans += 1
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] -= 1
        value = arr[i]
        ans += value * 2
        if arr[i] == arr[i+1]:
            arr[i+1] = 0
        else:
            arr[i+1] -= abs(arr[i+1] - arr[i])
        if arr[i+1] < 0:
            arr[i+1] = abs(arr[i+1]) % 2 == 0

    if arr[-1] > 0:
        if arr[-1] % 2 == 0:
            ans += arr[-1] * 2
        else:
            ans += arr[-1] * 2 - 1
    return ans
        
def solve(data):
    results = {}
    for k, v in data["tests"].items():
        results[k] = calculate(v["floor"])

    return jsonify({
        "answers": results
    })