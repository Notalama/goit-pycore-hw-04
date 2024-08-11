def get_cats_info(path):
    """
    Читає інформацію про котів з файлу та повертає список словників.

    Args:
        path: Шлях до файлу з даними про котів.

    Returns:
        Список словників, де кожен словник містить інформацію про одного кота.
    """

    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")

    return cats_info
cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
