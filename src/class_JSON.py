import json
from abc import ABC, abstractmethod


class Work_JSON(ABC):
    """
    Абстрактный класс для работы с файлом.
    """

    @abstractmethod
    def get_data(self):
        """Метод получения данных из файла"""
        pass

    @abstractmethod
    def addition_data(self, vacancy_dict):
        """Метод добавления данных в файл"""
        pass

    @abstractmethod
    def del_data(self, criterion_key, criterion_value):
        """Метод удаления данных из файла"""
        pass


class work_with_json(Work_JSON):
    """
    Класс для работы с JSON-файлами.
    """

    def __init__(self, filename="vacancies.json"):
        self.__filename = filename

    def get_data(self) -> list[dict]:
        """Получение данных из файла"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data  # список словарей
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def addition_data(self, vacancy_dict: dict):
        """
        Метод добавления новой вакансии без дублирования.
        Проверка по ключу 'name' или другому уникальному ключу.
        """
        data = self.get_data()
        # Предположим, что уникальный ключ — 'name'
        vacancy_name = vacancy_dict.get("name")
        if not any(vac.get("name") == vacancy_name for vac in data):
            data.append(vacancy_dict)
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

    def del_data(self, criterion_key: str, criterion_value: str):
        """
        Удаление вакансии по критерию.
        Например: criterion_key='name', criterion_value='Python Developer'
        """
        data = self.get_data()
        new_data = [vac for vac in data if vac.get(criterion_key) != criterion_value]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(new_data, f, indent=4, ensure_ascii=False)
