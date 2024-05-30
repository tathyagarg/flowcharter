from .parent import Node

class Terminal(Node):
    def __init__(self, color: int, text: str) -> None:
        super().__init__(color, text)

    def draw(self) -> str:
        return f'<path d="h-50 a 50 50 0 0 0 -50 50 a 50 50 0 0 0 50 50 h100 a50 50 0 0 0 50 -50 a50 50 0 0 0 -50 -50" stroke="black" color="{self.color}"/>'

