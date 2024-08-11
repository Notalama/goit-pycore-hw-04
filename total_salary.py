def total_salary(path):
    """
    Обчислює загальну та середню суму заробітної плати з текстового файлу.

    Args:
        path: Шлях до файлу, що містить дані про зарплати.

    Returns:
        Кортеж (total_salary, average_salary), де:
            total_salary: Загальна сума зарплат.
            average_salary: Середня заробітна плата.

    Raises:
        FileNotFoundError: Якщо файл не знайдено.
    """

    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total += salary
                count += 1
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{path}' не знайдено.")

    if count == 0:
        return 0, 0  # Або можна згенерувати виняток, якщо файл порожній

    average = total / count
    return total, average

total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")