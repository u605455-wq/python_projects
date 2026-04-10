class Unit:
    _hp: int
    _damage: int
    _tipe_name: str

    def __init__(self, hp: int, damage: int, tipe_name: str) -> None:
        self._hp = hp
        self._damage = damage
        self._tipe_name = tipe_name
