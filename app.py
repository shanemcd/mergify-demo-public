"""Simple demo application."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def farewell(name: str) -> str:
    return f"Goodbye, {name}!"


def count(n: int) -> str:
    return ", ".join(str(i) for i in range(1, n + 1))


if __name__ == "__main__":
    print(greet("world"))
    print(farewell("world"))
    print(count(5))
