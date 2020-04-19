import pickle


class Data:

    @staticmethod
    def save(hero, heroes_list):
        print("Сохранил")

        # То, что сохраняем
        data = [hero, heroes_list]

        with open("data", 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def load():
        print("Загружаю")

        with open("data", 'rb') as f:
            return pickle.load(f)
