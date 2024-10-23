import os
from typing import Any

from fastapi.templating import Jinja2Templates


def get_env(name: str, _type: Any=str) -> Any:
    """
    Функция возвращает значение переменной окружения с именем name
    Если значение не найдено, то выбрасывает исключение KeyError
    :param name: имя переменной окружения
    :return: значение переменной окружения
    """
    try:
        return _type(os.environ[name])
        
    except KeyError:
        raise KeyError(f"{name} is not set in the environment")


SERVER_HOST = get_env("SERVER_HOST")
SERVER_PORT = get_env("SERVER_PORT", int)


html_templates = Jinja2Templates(directory='pywebsite/app/templates')