import json
import requests
from pathlib import Path

if __name__ == "__main__":
    url = "http://localhost:3000/salad-spree"

    with Path("./data.json").open("r") as f:
        data = json.load(f)
    with Path("./result.json").open("r") as f:
        res = json.load(f)

    for i in range(len(data)):
        response = requests.post(url, json = data[i]).json()
        print("===============")
        print("Data:", i + 1)
        if res[i] != response:
            print("Error:")
            print("Actual:", json.dumps(response, indent = 4))
            print("Expected:", json.dumps(res[i], indent = 4))
        else:
            print("No Error")
        print("===============")