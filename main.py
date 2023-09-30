# Task 1
# def count_words(text):
#     words = text.split()
#
#     word_count = {}
#
#     for word in words:
#         word = word.strip(".,!?/"'()[]{}')
#         word = word.lower()
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word = word_count[word] = 1
#     return word_count
#
# test = input("Введите текст: ")
# result = count_words(test)
# print("Результат")
# for word , count in result.items():
#     print(f"{word}: {count}")

# Task 2
# translations = {
#     'hello': 'привіт',
#     'goodbye': 'до побачення',
#     'cat': 'кіт',
#     'dog': 'собака'
# }
# def translate_word(word):
#     if word in translations:
#         return translations[word]
#     else:
#         return "такого слова нету"
# while True:
#     input_word = input("Введите слово для перевода (або 'end' для завершенния): ").lower()
#
#     if input_word == "end":
#         break
#     translations = translate_word(input_word)
#     print(f"Перевод:{translations}")

# Task 3
# contacts = {}
# def Add_contact(name , phone_number):
#     contacts[name] = phone_number
#     print(f'contact{name} = с номером {phone_number} добавлен.')
# def delete_contact(name):
#     if name in contacts[name]:
#         del contacts[name]
#         print(f"контакт {name} Удален")
#     else:
#         print(f"Контакт {name} не найденно")
# def get_phone_number(name):
#     if name in contacts:
#         phone_number = contacts[name]
#         print(f"номер телефона{name}: {phone_number}")
#     else:
#         print(f"контакт {name} не найденно ")
#
# while True:
#     print("\nМеню")
#     print("1) Добавить контакт")
#     print("2) Удалить контакт")
#     print("3) Узнать номер телефона за именем")
#     print("4) Выйти ")
#
#     choice = input("выберите опцию")
#     if choice == "1":
#         name = input("введите имя контакта")
#         phone_number = input("Введите номер телефона")
#         Add_contact(name, phone_number)
#     elif choice == "2":
#         name = input("Введите имя контакта который хоитите удалить")
#         delete_contact(name)
#     elif choice == "3":
#         name = input("Введите имя контакта номер которого хоитие получить")
#         get_phone_number(name)
#     elif choice == "4":
#         print("Спасибо что использовали программу ))")
#         break
#     else:
#         print("вы выбрали неверную функцию")
# #
# Task 4
# summa = float(input("Введіть суму для конвертаций"))
# pochatkova_valuta = input("Введите начальныую валюту").lower()
# cilova_valuta = input("Введіть валюту, в яку конвертувати: ").lower()
#
# currencies = {"usd": 36, "eur": 38, "gbp": 33}
#
# if pochatkova_valuta in currencies and cilova_valuta in currencies:
#     kurs_pochatkova = currencies[cilova_valuta]
#     kurs_cilova = currencies[cilova_valuta]
#
#     convertacia = summa * (kurs_cilova / kurs_pochatkova)
#     print(f"{summa} {pochatkova_valuta.upper()} = {convertacia} {cilova_valuta.upper()}")
# else:
#     print("Вы ввели неверный код.Проверте данные")

