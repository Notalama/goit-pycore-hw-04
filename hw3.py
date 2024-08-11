import sys
import pathlib
from colorama import init, Fore, Style

def visualize_directory(path):
    """
    Візуалізує структуру директорії, виводячи імена файлів та піддиректорій з кольоровим виділенням.

    Args:
        path: Шлях до директорії.
    """

    try:
        path = pathlib.Path(path)
        if not path.is_dir():
            raise NotADirectoryError(f"'{path}' не є директорією.")

        def _visualize_recursive(current_path, depth=0):
            """
            Рекурсивно обходить директорію та виводить вміст.

            Args:
                current_path: Поточний шлях (об'єкт Path).
                depth: Рівень вкладеності (для відступів).
            """

            for item in current_path.iterdir():
                if item.is_dir():
                    print(f"{Fore.BLUE}{'  ' * depth}📁 {item.name}{Style.RESET_ALL}")
                    _visualize_recursive(item, depth + 1)
                else:
                    print(f"{Fore.GREEN}{'  ' * depth}📜 {item.name}{Style.RESET_ALL}")

        _visualize_recursive(path)

    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    init()  # Ініціалізація colorama

    if len(sys.argv) != 2:
        print("Використання: python script.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = sys.argv[1]
    visualize_directory(directory_path)
