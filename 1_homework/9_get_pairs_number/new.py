print('Hello world')

lst = [1,3,6,7]

def progression(x:list) -> bool:
    d = lst[1] - lst[0]
    for i in range(1, len(x)):
        if lst[i] - lst[i-1] != d:
            return False
    return True

print(progression(lst))


s = 'привет мир это я'
def upper(x: str) -> str:
    words = x.split()
    #result = f'{x[0][0].upper()}{s[1:]} {x[1]}'
    res = ''
    for w in words:
        s = f'{w[0].upper()}{w[1:]} '
        res += s
    return res

print(upper(s))