# a = dict(a=1, b=2)
# c = {'a':1, "b":2}
# q = {}
# q['a'] = 1
# q['b'] = 2
# w = dict([("a",1),("b",2)])
# r = {x: y for x,y in w.items()}


dic = {
    'a': 1,
    'b': 2,
    'c': 13,
    'd': 4,
    'e': 7
}

def change(d: dict) -> dict:
    return {x: y for x, y in d.items() if y == min(d.values()) or y == max(d.values())}

print(change(dic))

def change_two(d: dict) -> dict:
    # res = {}
    # res.update({x: y for x, y in d.items() if y == max(d.values())})
    # del({x for x, y in d.items() if y == max(d.values())})
    # return res.update({x: y for x, y in d.items() if y == max(d.values())})
    res = sorted([(x,y) for x, y in d.items()] , key=lambda x: x[1])
    res
    list(d.items())



print(change_two(dic))