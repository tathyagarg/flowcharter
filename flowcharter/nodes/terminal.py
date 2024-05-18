from .parent import Node

class Terminal(Node):
    def __init__(self, height: int, width: int, color: int, text: str):
        super().__init__(height, width, color, text)
