import sys

def solve(data):
    n = data['number_of_salads']
    S = data['salad_prices_street_map']

    min_cost = sys.maxsize
    for street in S:
        for i in range(len(street) - n + 1):
            window_cost = 0
            is_valid_window = True
            for j in range(n):
                price = street[i + j]
                if price == "X":
                    is_valid_window = False
                    break
                window_cost += int(price)
            
            if is_valid_window:
                min_cost = min(min_cost, window_cost)

    if min_cost == sys.maxsize:
        min_cost = 0
            
    return {
        "result": min_cost
    }