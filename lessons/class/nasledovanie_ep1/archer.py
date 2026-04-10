from unit import Unit


class Archer(Unit):
    __count_arrows: int

    def __init__(self, hp: int, damage: int, tipe_name: str, count_arrows: int) -> None:
        super().__init__(hp, damage, tipe_name)
        self.__count_arrows = count_arrows

    def print_info(self) -> None:
        print(self._tipe_name)
        print(f"Здоровье: {self._hp}")
        print(f"Урон: {self._damage}")
        print(f"Выносливость: {self.__count_arrows}")