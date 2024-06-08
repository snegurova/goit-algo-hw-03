"""Module providing a solving hanoi task."""
def hanoi(n, source, auxiliary, target, state):
    """Function providing hanoi algorithm"""
    if n > 0:
        hanoi(n - 1, source, target, auxiliary, state)
        disk = source.pop()
        target.append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        hanoi(n - 1, auxiliary, source, target, state)

def main():
    """Function solving hanoi task"""
    n = int(input("Введіть кількість дисків: "))
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []
    state = {'A': source, 'B': auxiliary, 'C': target}

    print(f"Початковий стан: {state}")
    hanoi(n, source, auxiliary, target, state)
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
