# Задача 1.1

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
print(my_favorite_songs[0:13])
print(my_favorite_songs[64:78])
print(my_favorite_songs[16:23])
print(my_favorite_songs[-26:-15])

# Задача 1.2

import random
from datetime import timedelta


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
def calculate_total_time_a(songs):
    total_time_a = sum(song[1] for song in songs)
    return total_time_a

random_songs_a = random.sample(my_favorite_songs, 3)
total_time_a = calculate_total_time_a(random_songs_a)
formatted_time_a = str(timedelta(minutes=total_time_a))

print("Пункт A:")
print(f"Три случайные песни звучат {formatted_time_a} минут.")

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
def calculate_total_time_b(songs):
    total_time_b = sum(my_favorite_songs_dict[song] for song in songs)
    return total_time_b

random_songs_b = random.sample(list(my_favorite_songs_dict.keys()), 3)
total_time_b = calculate_total_time_b(random_songs_b)
formatted_time_b = str(timedelta(minutes=total_time_b))


print(f"Три случайные песни звучат {formatted_time_b} минут.")


combined_songs = [song[0] for song in my_favorite_songs] + list(my_favorite_songs_dict.keys())
random_songs_c = random.sample(combined_songs, 3)


print("Случайные песни:")
for song in random_songs_c:
    print(song)


def format_time(minutes, seconds):
    time = timedelta(minutes=minutes, seconds=seconds)
    return str(time)


for song in my_favorite_songs:
    name, duration = song
    minutes = int(duration)
    seconds = int((duration - minutes) * 60)
    formatted_duration = format_time(minutes, seconds)
    print(f"{name}: {formatted_duration}")


# Задача 1.3

month_number = int(input("Введите номер месяца: "))

months = {
    1: "январь",
    2: "февраль",
    3: "март",
    4: "апрель",
    5: "май",
    6: "июнь",
    7: "июль",
    8: "август",
    9: "сентябрь",
    10: "октябрь",
    11: "ноябрь",
    12: "декабрь"
}

days_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

if month_number in months:
    month_name = months[month_number]
    days = days_month[month_number]
    print(f"Вы ввели {month_name}. {days} дней")
else:
    print("Такого месяца нет!")


# Задача 1.4

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}
store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}


for title, number in titles.items():
    total_quantity = 0
    total_cost = 0

    if number in store:
        items = store[number]
        for item in items:
            quantity = item['quantity']
            price = item['price']
            total_quantity += quantity
            total_cost += quantity * price

        print(f"{title} - {total_quantity} шт, стоимость {total_cost} руб")
    else:
        print(f"Товар {title} отсутствует на складе")    


# Задача 2.1

def minimum(arr):
    if len(arr) == 0:
        return None

    min_size = arr[0]
    for num in arr:
        if num < min_size:
            min_size = num
    return min_size


def maximum(arr):
    if len(arr) == 0:
        return None

    max_size = arr[0]
    for num in arr:
        if num > max_size:
            max_size = num
    return max_size

arr1 = [4, 6, 2, 1, 9, 63, -134, 566]
print(arr1, "Минимум:", minimum(arr1), "Максимум:", maximum(arr1))

arr2 = [-52, 56, 30, 29, -54, 0, -110]
print(arr2, "Минимум:", minimum(arr2), "Максимум:", maximum(arr2))

arr3 = [42, 54, 65, 87, 0]
print(arr3, "Минимум:", minimum(arr3), "Максимум:", maximum(arr3))

arr4 = [5]
print(arr4, "Минимум:", minimum(arr4), "Максимум:", maximum(arr4))

# Задача 2.2

def quarter_of(month):

    month_names = {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'апрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь',
        11: 'ноябрь',
        12: 'декабрь'
    }


    if month >= 1 and month <= 3:
        month_name_a = month_names[month]
        return f"месяц {month} ({month_name_a}) является частью 1 квартала."
    elif month >= 4 and month <= 6:
        month_name_a = month_names[month]
        return f"месяц {month} ({month_name_a}) является частью 2 квартала."
    elif month >= 7 and month <= 9:
        month_name_a = month_names[month]
        return f"месяц {month} ({month_name_a}) является частью 3 квартала."
    elif month >= 10 and month <= 12:
        month_name_a = month_names[month]
        return f"месяц {month} ({month_name_a}) является частью 4 квартала."
    else:
        return "Вы ввели номер квартала по номеру месяца которого нет."


month = int(input('Введите номер квартала по номеру месяца: '))
print(quarter_of(month))


# Задача 2.3

def switch_it_up(number):
    switch = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    return switch.get(number, 'Вы ввели неверное число')
number = int(input('Введите цифру от 0 до 9: '))
print(switch_it_up(number))



# Задача 2.4

def remove_exclamation_marks(s):
    return s.replace("!", "")

def remove_last_em(s):
    if s.endswith("!"):
        return s[:-1]
    else:
        return s

def remove_word_with_one_em(s):
    words = s.split()
    filtered_words = [word for word in words if word.count("!") != 1]
    return " ".join(filtered_words)

print(remove_exclamation_marks("Hi! Hello!"))
print(remove_exclamation_marks(""))
print(remove_exclamation_marks("Oh, no!!!"))


print(remove_last_em("Hi!"))
print(remove_last_em("Hi!!!"))
print(remove_last_em("!Hi"))


print(remove_word_with_one_em("Hi!"))
print(remove_word_with_one_em("Hi! Hi!"))
print(remove_word_with_one_em("Hi! Hi! Hi!"))
print(remove_word_with_one_em("Hi Hi! Hi!"))
print(remove_word_with_one_em("Hi! !Hi Hi!"))
print(remove_word_with_one_em("Hi! Hi!! Hi!"))
print(remove_word_with_one_em("Hi! !Hi! Hi!"))
