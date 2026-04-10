class AbstractBrush:
    _sign: str
    _name: str

    def __init__(self, sign: str, name: str) -> None:
        self._sign = sign
        self._name = name

    def draw() -> None:
        raise NotImplementedError("не реальзован метод draw")

class StarBrush(AbstractBrush):

    def __init__(self) -> None:
        super().__init__("*", "Звездная кисть")

    def draw(self) -> None:
        print(self._name)
        print(self._sign)
