# ИД — целое уникальное число
# Название — строка (макс 25 символов)
# Жанр — строка (макс 15 символов)
# Режиссёр — строка (макс 20 символов)
# Год выпуска — целое число
# Длительность (мин) — целое число
# Рейтинг — дробное число
# Цена — целое число
# Количество копий — целое число


# 1. поиск фильмов
# по диапазону годов выпуска
# по жанру
# 2. сортировка фильмов
# по длительности
# по рейтингу (по убыванию)
# 3. подсчитать среднюю длительность фильмов
# Задание 4. Фильмы
# Описание сущности
# Сущность:
# Поля:
# Действия пользователя в программе:
# 4. вывести топ-3 фильма по рейтингу
# 5. увеличить цену фильмов, выпущенных до 2000 года
# 6. пометить фильмы длительностью более 150 минут как «эпик»
# 7. сгруппировать фильмы по жанрам и вывести результат
# 8. удалить фильмы с рейтингом ниже 5.0

import os
from dataclasses import dataclass

@dataclass
class film():
    ID: int
    name: str
    genre: str
    director:str
    release: int
    duration: int
    rating: float
    price: int
    copy: int


def input_film_data():
    admin_answer = "yes"
    films = []
    while admin_answer == "yes":
        print("Введите данные фильма")
        name = input("Название: ")
        genre = input("Жанр: ")
        director = (input("Режиссер: "))
        release = int(input("Год релиза: "))
        duration = int(input("Длительность: "))
        rating = float(input("Рейтинг: "))
        price = int(input("цена: "))
        copy = int(input("кол-во копий: "))

        films.append(film(0, name, genre, director,release, duration,rating, price, copy ))

        os.system('cls')
        admin_answer = (input("Хотите добавить еще фильм?(yes/no)"))

    return films




def find_film_release(films):

    print("Введите диапозон годов выпуска фильма, что хотите найти")
    user_find1 = int(input("1ый год: "))
    user_find2 = int(input("2ой год: "))

    j = 0
    os.system('cls')
    print("РЕЗУЛЬТАТЫ ПОИСКА\n-----------------")
    for i in range(user_find1,user_find2+1):
        for item in films:
            if item.release == i:
                j +=1
                print(j,".",item.name)
                
    if j == 0:
        print("По вашему запросу ничего не нашлось.")


def find_film_genre(films):

    print("Введите жанр фильма, что хотите найти")
    user_find1 = (input("жанр: "))

    j = 0
    os.system('cls')
    print("РЕЗУЛЬТАТЫ ПОИСКА\n-----------------")
    for item in films:
        if item.genre == user_find1:
            j +=1
            print(j,".", item.name)
            
    if j == 0:
        print("По вашему запросу ничего не нашлось.")


def sorting_movies_duration(films):
    durations = []
    os.system('cls')
    print("ФИЛЬМЫ\n-----------------")
    for item in films:
        durations.append(item.duration)
    for i in range(1,len(durations)+1):
        max_duration = max(durations)
        for item in films:
            if item.duration == max_duration:
                print(f"{i}. Название: {item.name} \nДлительность(мин): {item.duration}")

        index = durations.index(max_duration)
        durations.pop(index)


def sorting_movies_rating(films):
    ratings = []
    os.system('cls')
    print("ФИЛЬМЫ\n-----------------")
    for item in films:
        ratings.append(item.rating)
    for i in range(1,len(ratings)+1):
        max_rating = max(ratings)
        for item in films:
            if item.rating == max_rating:
                print(f"{i}. Название: {item.name} \nРейтинг: {item.rating}")

        index = ratings.index(max_rating)
        ratings.pop(index)



def main_screen():

    print("Выберите дейтвие\n----------------")
    print("1. Поиск фильма")
    print("2. Все фильмы")
    print("3. Средняя длительность")
    print("4. ТОП 3 фильма")
    print("5. Жанры фильмов")
    print("6. Админ")

    what_user_want = int(input("Действие: "))
    
    return what_user_want


films = input_film_data()
what_user_want = main_screen()


if what_user_want == 1:
    print("Поиск по году выпуска или по жанру")
    print("1. Диапозон годов ")
    print("2. Жанр ")
    what_user_want = int(input("Действие: "))
    if what_user_want == 1:
        find_film_release(films)
    if what_user_want == 2:
        find_film_genre(films)

if what_user_want == 2:
    print("Вывести фильмы по длительности или рейтингу?")
    print("1. Длительности")
    print("2. Рейтингу")
    what_user_want = int(input("Действие: "))
    if what_user_want == 1:
        sorting_movies_duration(films)
    if what_user_want == 2:
        sorting_movies_rating(films)

def average_film_duratin(films):
    if len(films) == 0:
        print("Нет фильмов для расчета средней длительности.")

        return

    os.system('cls')
    print("Средняя длительность фильмов\n" + "-" * 40)

    total_duration = 0
    for movie in films:
        total_duration += movie.duration

    average = total_duration / len(films)

    print(f"Кол-во фильмов:{len(films)}")
    print(f"Суммарная длительность:{total_duration} минут")
    print(f"Средняя длительность:{average:2f} минут")

    print("\nВсе фильмы:")
    for movie in films:
        print(f" - {movie.name}: {movie.duration} минут")

    input("\nНажмите Enter для возврата в меню...")

if what_user_want == 3:
    average_film_duratin(films)

def top_3_by_raiting(films):
    if len(felms) == 0:
        print("Нет фильмов для отображения.")

        return

    os.system('cls')
    print("Топ 3 фильма по рейтингу\n" + "=" * 40)

    sorted_films = sorted(films, key=lambda film: film.rating, reverse=True)
    coun = min(3, len(sorted_films))

    print(f"Рейтинг основан на оценке от 0.0 до 10.0\n")

    for i in range(coun):
        film = sorted_films[i]
        print(f"{i+1}. {film.name}")
        print(f"Рейтинг:{film.rating}")
        print(f"Жанр:{film.genre}")
        print(f"Год:{film.release}")
        print(f"Длительность:{film.duration} мин")

    if len(films) < 3:
        print(f"Всего доступно фильмов {len(films)}")
        print("=" * 40)

    print("\nВсе фильмы с рейтингами:")
    for film in sorted_films:
        print(f" - {film.name}: {film.rating}")

    input("\nНажмите Enter для возврата в меню...")

if what_user_want == 4:
    top_3_by_raiting(films)

def increase_price_for_old_films(films):

    if len(films) == 0:
        print("Нет фильмов для обработки.")

        return

    os.system('cls')
    print("Увеличение цены для фильмов до 2000 года\n" + "=" * 50)

    print("Введите процент увеличения цены(пример: 10б 25б 40):")
    try:
        percent = float(input("Процент: "))
    except ValueError:
        print("Ошибка!Введите число.")
        input("\nНажмите Enter для возврата в меню...")
        return

    old_price_films = []
    total_increase = 0

    for film in films:
        if film.release < 2000:
            old_price = film.price
            increase_amount = old_price * (percent / 100)
            film.price = int(old_price + increase_amount)
            total_increase += increase_amount
            old_price_films.apppend({
                'film': film,
                'old_price': old_price,
                'increase': increase_amount
                })
    
    if old_price_films:
        print(f"\nЦены увеличены на {percent}% для {len(old_price_films)} фильмов: ")
        print("-" * 50)

        for i, item in enumerate(old_price_films, 1):
            film = item['film']
            print(f"{i}. {film.name}({film.release} г.)")
            print(f"Было: {item['old_price']} рублей - Стало:{film.price} рублей")
            print(f"Увеличение: + {int(item['increase'])} рублей.")
            print()
        
        print(f"Общая сумма увеличения: + {int(total_increase)} рублей.")
    else:
        print("\nНет фильмов, выпущенных до 2000 года.")

    print("\n" + "=" * 50)
    print("ВСЕ ФИЛЬМЫ С ЦЕНАМИ:")
    for film in films:
        year_status = "(до 2000 года.)" if film.release < 2000 else "(после 2000 года.)"
        print(f" - {film.name}({film.release} г.) {year_status}: {film.price} рублей.")

    print("\n" + "=" * 50)
    input("\nНажмите Enter для возврата в меню...")

if what_user_want == 5:
    increase_price_for_old_films(films)





