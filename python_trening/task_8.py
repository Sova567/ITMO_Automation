a: int = 5
b: str = 'ygvyv'
c: list = [4, 6]

def task4(s: str, v: int) -> str:
    return " " * (max(0, v - len(s))) + s

print(task4('123', 123))