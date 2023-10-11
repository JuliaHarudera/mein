def parser(numbers: str) -> list:
    return [list(num) for num in numbers.split(",")]


def is_arithmetic_sequence(numbers: list) -> bool:
    n = len(numbers)
    if n < 2:
        return False
    diff = numbers[1] - numbers[0]
    return all(numbers[i] - numbers[i - 1] == diff for i in range(2, n))


def is_geometric_sequence(numbers: list) -> bool:
    n = len(numbers)
    if n < 2:
        return False
    ratio = numbers[1]/numbers[0]
    return all(numbers[i]/numbers[i - 1] == ratio for i in range(2, n))


def next_arithmetic_item(numbers: list) -> int:
    diff = numbers[1] - numbers[0]
    return numbers[-1] + diff


def next_geometric_item(numbers: list) -> int:
    ratio = numbers[1] / numbers[0]
    return int(numbers[-1] * ratio)


def get_next_item(numbers: list):
    if len(numbers) > 2:
        if is_arithmetic_sequence(numbers):
            return next_arithmetic_item(numbers)

        if is_geometric_sequence(numbers):
            return next_geometric_item(numbers)

    return None


if __name__ == '__main__':
    numbers = input('Введите последовательность чисел через запятую: ')
    numbers = parser(numbers)
    next_item = get_next_item(numbers)

    if next_item is not None:
        print("Следующий член последовательности:", next_item)
    else:
        print("Не удалось определить правило для генерации последовательности.")