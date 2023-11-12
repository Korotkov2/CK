import json

def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    sum_dict = 0
    for i in data:
        a = i['score']
        b = i['weight']
        sum_dict += a * b
    return round(sum_dict, 3)

print(task())
