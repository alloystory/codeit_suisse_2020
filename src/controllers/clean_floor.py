from flask import jsonify

def all_clean(arr):
    return all(map(lambda x: x == 0, arr))

def calculate(arr):
    print("Data:", arr)
    floor = arr[::-1]
    num_moves = 0
    while floor:
        if len(floor)==1:
            if floor[-1]%2 == 0:
                num_moves+= (2* floor[-1])
            else:
                num_moves+= (2* floor[-1]) +1
            
            break
        num_moves+= floor[-1]*2+1
        if floor[-1] >= floor[-2]:
            if (floor[-1]-floor[-2])%2==0:
                if len(floor) != 2:
                    floor[-2] = 1
                    floor.pop()
                else:
                    floor.pop()
                    floor.pop()
                    num_moves -= 1
                    break
            else:
                floor.pop()
                floor.pop()
                try:
                    floor[-1] -= 1
                    num_moves+=1
                except:
                    break
        else:
            floor[-2]-=floor[-1]
            floor[-2]-=1
            floor.pop()
    return num_moves
        
def solve(data):
    results = {}
    for k, v in data["tests"].items():
        results[k] = calculate(v["floor"])

    return jsonify({
        "answers": results
    })