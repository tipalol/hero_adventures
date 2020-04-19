from Hero import Hero
from Data import Data

import random


# Есть кто живой?
def is_alive(heroes_list):
    for element in heroes_list:
        if element.lives > 1:
            return True

    return False


# Сколько живых?
def count_alive(neponaytnaya_fignya):
    count = 0
    for element in neponaytnaya_fignya:
        if element.lives > 0:
            count += 1

    return count


# Устроить битву
def make_battle(kakoyta_list):
    # Первый боец
    fighter1 = kakoyta_list[random.randint(0, len(kakoyta_list) - 1)]
    # Второй
    fighter2 = None

    for fighter in kakoyta_list:
        if fighter != fighter1:
            fighter2 = fighter

    # Устраиваем бой и результат сохраняем в result
    result = fighter1.fight(fighter2)

    # Первый выиграл, второй проиграл
    if result == 1:
        # Находим позицию мертвого бойца
        dead_fighter_index = kakoyta_list.index(fighter2)
        # Найти позицию победителя
        winner_index = kakoyta_list.index(fighter1)

    # Второй выиграл, первый проиграл
    else:
        # Находим позицию мертвого бойца
        dead_fighter_index = kakoyta_list.index(fighter1)
        # Найти позицию победителя
        winner_index = kakoyta_list.index(fighter2)

    # Удаляем мертвого бойца из списка и сохраняем его оружие
    new_weapon = kakoyta_list.pop(dead_fighter_index).weapon
    # Обновляем победителя
    kakoyta_list[winner_index].power += 5
    # Забираем оружие проигравшего, если оно лучше
    if new_weapon > kakoyta_list[winner_index].weapon:
        kakoyta_list[winner_index].weapon = new_weapon

    return kakoyta_list


# Создает новый список героев
def generate_heroes():
    heroes_list = []
    for i in range(1000):
        heroes_list.append(Hero.create_hero())

    return heroes_list


# Печатаем меню
def print_menu():
    print('1 - Мой герой')
    print('2 - Магазин')
    print('3 - Участвовать в боях')
    print('0 - Выход')
    print('Введите нужный пункт меню')


# ------Игровые переменные--------- #
# Наш герой
my_hero = None
# Список героев
heroes = []
# Имя игрока
name = ''
# День
day = 1

print("В первый раз здесь? (да/нет)")
choose = input()

# Новая игра
if choose == 'да':
    print("Привет, герой, как тебя называть?")
    name = input()
    # Создаем своего героя
    my_hero = Hero(name, 10, 100, 1)
    # Создаем общий список героев
    heroes = generate_heroes()
    # Сохраняем нашего героя и всех остальных
    Data.save(my_hero, heroes)

# Загрузка игры
else:
    print("Загружаю..")
    # Загружаем сохранение
    data = Data.load()
    # Достаем героя
    my_hero = data[0]
    # Достаем всех остальных
    heroes = data[1]

print('Шел мой ' + str(day) + ' день на арене')
print('В живых остается ' + str(count_alive(heroes)) + ' гладиаторов')
print('Сегодня должно состояться несколько боев, я тоже участвую')
print_menu()
choose = input()

while choose != '0' and my_hero.lives > 0:
    # Меню героя
    if choose == '1':
        my_hero.talk()

    # Магазин
    elif choose == '2':
        pass

    # Участвовать в боях
    elif choose == '3':
        # Увеличиваем дни на 1
        day += 1
        # Выбираем случайного противника
        enemy = random.randint(0, len(heroes) - 1)
        # Устраиваем с ним бой
        result = my_hero.fight(heroes[enemy])
        print('Деремся с ' + heroes[enemy].name)

        # Если мы выиграли
        if result == 1:
            # Даем себе силу
            my_hero.power += 2
            # Восстанавливаем жизни
            my_hero.lives = 100
            # Если у нашего противника оружие было сильнее - забираем
            if heroes[enemy].weapon > my_hero.weapon:
                my_hero.weapon = heroes[enemy].weapon
                print('Наш герой забрал оружие проигравшего')

            # Удаляем противника из общего списка
            heroes.pop(enemy)
            print('Бой окончен, ' + my_hero.name + ' выходит победителем')

        # Если мы проиграли
        else:
            print('Меня постигла неудача :(')
            my_hero.lives = 0

        # Кол-во боев, проходящих сегодня, кроме нашего
        fights = random.randint(1, 10)
        # Устраиваем бои между другими участниками
        for i in range(fights):
            heroes = make_battle(heroes)


    print('Шел мой ' + str(day) + ' день на арене')
    print('В живых остается ' + str(count_alive(heroes)) + ' гладиаторов')
    print('Сегодня должно состояться несколько боев, я тоже участвую')
    print_menu()
    choose = input()

# Сохраняемся
Data.save(my_hero, heroes)
