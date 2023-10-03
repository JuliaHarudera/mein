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

def count_unique_elements(imput_list):
    unique_elements = set(imput_list)
    return len(unique_elements)
imput_list = [11,11,12,12,11,21, 2, 3 ,4 ,5 ,6 ,7]
unique_elements = count_unique_elements(imput_list)
print("Количество уникальных символов", unique_elements)