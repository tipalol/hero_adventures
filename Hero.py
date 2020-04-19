import random


class Hero:

    def __init__(self, name, power, lives, weapon):
        self.weapon = weapon
        self.lives = lives
        self.name = name
        self.power = power

    @staticmethod
    def get_weapon_name(weapon):
        if weapon == 0:
            return 'безоружный'
        if weapon == 1:
            return 'деревянный меч'
        if weapon == 2:
            return 'топор'
        if weapon == 3:
            return 'стальной меч'
        if weapon == 4:
            return 'световой меч'

    def talk(self):
        print("Привет, меня зовут " + self.name)
        print('Моя сила: ' + str(self.power))
        print('У меня осталось ' + str(self.lives) + ' жизней')
        print('Мое оружие: ' + Hero.get_weapon_name(self.weapon))

    # Устраивает бой между двумя бойцами
    # возвращает 1, если выиграл первый и 2, если второй
    def fight(self, other):
        # print('Бой начался!')
        while self.lives > 0 and other.lives > 0:
            other.lives -= self.power + self.weapon*2

            if other.lives < 1:
                break

            self.lives -= other.power + other.weapon*2

        if self.lives < 1:
            # print(other.name + ' побеждает в этом бою')
            return 2
        else:
            # print(self.name + ' побеждает в этом бою')
            return 1

    @staticmethod
    def create_hero():

        names = ['Гена Букин', 'Гарри Поттер', 'Перси', 'Рон Уизли', 'Воландеморт', 'Гоблин']

        new_name = names[random.randint(0, 5)]
        new_power = random.randint(2, 10)
        new_lives = 100
        new_weapon = random.randint(0, 4)

        return Hero(new_name, new_power, new_lives, new_weapon)

    # Сравнение двух бойцов
    def __eq__(self, other):
        if self.name == other.name and self.power == other.power and self.lives == self.lives:
            return True

        return False


