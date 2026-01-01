from __future__ import annotations

def hello(name: str = "world") -> str:
    name = name.strip() or "world"
    return f"Hello, {name}!"

def main() -> None:
    print(hello())
