# Task 1
# def elementu_spicka(imput_list):
#     ynikalnue_slova = set()
#     for elementu in imput_list:
#         if elementu in ynikalnue_slova:
#             return False
#         ynikalnue_slova.add(elementu)
#     return True
# imput_list = [1211,1211, 3321,4345,456, 2455]
# result = elementu_spicka(imput_list)
# if result:
#     print("Все елементы уникальные")
# else:
#     print("error")

# Task 2
# def count_unique_elements(imput_list):
#     unique_elements = set(imput_list)
#     return len(unique_elements)
# imput_list = [11,11,12,12,11,21, 2, 3 ,4 ,5 ,6 ,7]
# unique_elements = count_unique_elements(imput_list)
# print("Количество уникальных символов", unique_elements)

# Task 3
# def count_Unique_words(imput_list):
#     Unique_words = set(imput_list)
#     for meaning in imput_list:
#         if meaning in Unique_words:
#             return False
#         Unique_words.add(meaning)
#     return True
# imput_list = {"bbb": "111",
#               "aaa": "222",
#               "ccc": "333"
#               }
# result = count_Unique_words(imput_list)
# if result:
#     print("Все значения соваря уникальные")
# else:
#     print("не все слова словаря есть уникальынми")

# Task 4
# def find_common_friends(friendships, user1, user2):
#     if user1 in friendships and user2 in friendships:
#         common_friends = friendships[user1].intersection(friendships[user2])
#         return common_friends
#     else:
#         return set()
# friendships = {
#     "user1": {"user2", "user3", "user4"},
#     "user2": {"user1", "user3"},
#     "user3": {"user1", "user2", "user4"},
#     "user4": {"user1", "user3"}
# }
# user1 = "user1"
# user2 = "user2"
# common_friends = find_common_friends(friendships, user1, user2)
# if common_friends:
#     print(f"совместные друзья {user1} і {user2}: {', '.join(common_friends)}")
# else:
#     print(f"У пользователя {user1} і {user2} нет совместных друзей.")


# Task 5
# def long_common_words(str1, str2):
#     words1 = set(str1.split())
#     words2 = set(str2.split())
#     common_words = words1.intersection(words2)
#     long_words = ""
#     for word in words1:
#         if len(word) > len(long_words):
#             long_words = word
#     return long_words
# string1 = "Тут надо ввести стору для сровнения"
# string2 = "Тут тоже надо ввести строку для стовнения"
# result = long_common_words(string1, string2)
# if result:
#     print(f"Самое длиное слово которе совпало: {result}")
# else:
#     print("нету совместных слов")

