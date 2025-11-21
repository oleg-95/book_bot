import logging
import os

logger = logging.getLogger(__name__)


# Функция, возвращающая строку с текстом страницы и её размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end_simbol = [".", ",", "!", ":", ";", "?"]
    end = start + page_size
    while text[end:][:1] in end_simbol:
        end -= 1
    text = text[start:end]
    text = text[: max(map(text.rfind, end_simbol)) + 1]
    return text, len(text)


# Функция, формирующая словарь книги
def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}

    # Читаем весь текст книги
    with open(path, encoding="utf-8") as f:
        text = f.read()

    start = 0
    page_num = 1
    n = len(text)

    # Пока не дошли до конца текста
    while start < n:
        # Получаем страницу с помощью _get_part_text()
        page_text, size = _get_part_text(text, start, page_size)

        # Удаляем лишние символы слева (пробелы, переносы строк и т.п.)
        cleaned = page_text.lstrip()

        # Сохраняем в словарь
        book[page_num] = cleaned

        # Переходим к следующему фрагменту
        start += size
        page_num += 1

    return book
