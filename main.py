
def calculate_expenses_by_category(hw_10_test):
    expenses_by_category = {}
    with open("hw_10_test", 'w', encoding='utf-8') as f:
        for line in f:
            _, _, sum_str, category = line.strip().split()
            sum_value = float(sum_str)
            if category in expenses_by_category:
                expenses_by_category[category] += sum_value
            else:
                expenses_by_category[category] = sum_value
    return expenses_by_category


def calculate_expenses_of_family_members(hw_10_test):
    expenses_of_family_members = {}
    with open(hw_10_test, 'r', encoding='utf-8') as f:
        for line in f:
            _, name, sum_str = line.strip().split()
            sum_value = float(sum_str)
            if name in expenses_of_family_members:
                expenses_of_family_members[name] += sum_value
            else:
                expenses_of_family_members[name] = sum_value
    return expenses_of_family_members


def main():
    file_name = "hw_10_test.txt"

    expenses_by_category = calculate_expenses_by_category(file_name)
    print("Загальна сума витрат по категоріях товарів:")
    for category, sum_value in expenses_by_category.items():
        print(f"{category}: {sum_value}")

    expenses_of_family_members = calculate_expenses_of_family_members(file_name)
    enter = input("Введіть ім'я члена сім'ї: ")
    if enter in expenses_of_family_members:
        amount_of_expenses = expenses_of_family_members[enter]
        number_of_purchases = len([line for line in open(file_name, 'r', encoding='utf-8') if enter in line])
        print(f"{enter} витратив(ла) {amount_of_expenses} гривень на {number_of_purchases} покупок.")
    else:
        print(f"{enter} не знайдено в списку членів сім'ї.")


if __name__ == "__main__":
    main()
