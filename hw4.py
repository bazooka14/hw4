def number_input():
    number = input("Введите номер документа:\n")
    return number


def search(dirs, docs, number):
    res = "Такого номер нет в базе."
    for directory in dirs.values():
        if number in directory:
            res = search_name(docs, number)
            break
    return res


def search_name(docs, number):
    for document in docs:
        if document["number"] == number:
            return "Результат:\n" + "Владелец документа: " + document["name"]


def user_input(dirs, docs):
    while True:
        command = input("\nВведите команду:\n")
        if command == "p":
            print(search(dirs, docs, number_input()))
        elif command == "q":
            print("\nВыход.")
            break
        else:
            print("\nТакой команды не существует, повторите попытку.\n")


documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


user_input(directories, documents)
