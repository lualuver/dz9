class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__energy = 100
        self.__weapon = "Без оружия"

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print(f"{self.name} атакует!")
        else:
            print("Недостаточно энергии для атаки")

    def take_damage(self, damage):
        if not isinstance(damage, int):
            raise InvalidGameValError(f"{damage} Не допустимое значение урона ожидается типом int")
        else:
            self.__health -= damage
            if self.__health <= 0:
                print(f"Персонаж {self.name} погиб")
            else:
                print(f"{self.name} получил {damage} урона, осталось {self.__health} здоровья")

    def equip_weapon(self, weapon):
        if not isinstance(weapon, str):
            raise InvalidGameValError(f"{weapon} это не оружие! Ожидается тип str")
        else:
            self.__weapon = weapon
            print(f"{self.name} экипировал оружие: {self.__weapon}")

    def get_status(self):
        return (f"Здоровье: {self.__health}, "
                f"Энергия: {self.__energy}, "
                f"Оружие: {self.__weapon}")

class InvalidGameValError(Exception):
    def __init__(self, error):
        super().__init__(error)

try:
    character = Character("Пип")
    character.attack()
    print(character.get_status())
    character.take_damage(20)
    character.take_damage(10)
    print(character.get_status())
    character.equip_weapon("Лопата")
    character.equip_weapon(10)
    print(character.get_status())
except InvalidGameValError as p:
    print(f"Произошла ошибка: {p}")
