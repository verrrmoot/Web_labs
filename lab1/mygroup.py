groupmates = [
    {
        "name": "Кареева",
        "surname": "Вера",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 3]
    },
    {
        "name": "Струкова",
        "surname": "Алиса",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Михайлов",
        "surname": "Михаил",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Агарков",
        "surname": "Максим",
        "exams": ["АГиЛА", "ИС", "Философия"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Соцков",
        "surname": "Игнат",
        "exams": ["ИнЯз", "ТПР", "КТП"],
        "marks": [3, 3, 3]
    },
]


# .ljust(15) - добавляет нужное количество пробелов
def filter_students(students, middle):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(20), u"Средний балл".ljust(15))
    for student in students:
        sum = 0
        for mark in student["marks"]:
            sum += mark
        average = sum / len(student["marks"])
        if round(average, 2) > middle:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35),
                  str(student["marks"]).ljust(20), str(round(average, 2)).ljust(15))


mid = float(input("средний балл: "))

filter_students(groupmates, mid)
