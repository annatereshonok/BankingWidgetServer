import functools
import os
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования выполнения функции.

    Параметры:
        filename: путь к файлу для записи логов (необязательный параметр).
    Возвращает:
        декорированная функция.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message: str = f"[INFO] Запуск функции '{func.__name__}' с аргументами: {args}, {kwargs}"

            if filename:
                mode: str = "a" if os.path.exists(filename) else "w"
                with open(filename, mode) as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)

            try:
                result: Any = func(*args, **kwargs)
                success_message: str = f"[INFO] Функция '{func.__name__}' выполнена успешно. Результат: {result}\n"

                if filename:
                    with open(filename, "a") as file:
                        file.write(success_message + "\n")
                else:
                    print(success_message)
                return result
            except Exception as e:
                error_message: str = (
                    f"[ERROR] Ошибка в функции '{func.__name__}': {type(e).__name__}. "
                    f"Входные параметры: {args}, {kwargs}\n"
                )
                if filename:
                    with open(filename, "a") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
