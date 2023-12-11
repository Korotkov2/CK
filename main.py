import doctest

class Glass:
    """
        Документация на класс.
        Класс описывает модель аквариум.
    """

    def __init__(self, height: float, bottom_radius: float):
        """
         Создание и подготовка к работе объекта Аквариум.
         :param height: высота Аквариума
         :param bottom_radius: радиус дня аквариума
         Примеры:
         >>> glass = Glass(50.0, 10.0)  # инициализация экземпляра класса
         """

        if not isinstance(height, float):
            raise TypeError("Высота аквариума должна быть типа float")
        if height <= 0:
            raise ValueError("Высота аквариума должна быть положительным числом")
        self.height = height

        if not isinstance(bottom_radius, float):
            raise TypeError("Радиус дна должен быть float")
        if bottom_radius <= 0:
            raise ValueError("Радиус дна должен быть положительным числом")
        self.bottom_radius = bottom_radius

    def count_volume(self):
        """
                Функция которая позволяет вычислить объем аквариума
                :return: Объем аквариума
                Примеры:
                >>> glass = Glass(30.0, 10.0)
                >>> glass.count_volume()
        """
        ...

    def count_another_height(self, new_bottom_radius: float) ->float:
        """
            Функция, которая позволяет вычислить новую высоту аквариума для заданного радиуса, и такого же объема,
            как имеющийся аквариум
            :return: Объем аквариума
            Примеры:
            >>> glass = Glass(30.0, 10.0)
            >>> glass.count_another_height(15.0)
        """
        if new_bottom_radius <= 0:
            raise ValueError("Радиус аквариума должна быть положительным числом")
        ...

class Box:
    """
        Документация на класс.
        Класс описывает модель коробки.
    """

    def __init__(self, edge: float, sand: float):
        """
         Создание и подготовка к работе объекта коробка.
         :param edge: сторона коробки
         :param sand: количество песка внутри
         Примеры:
         >>> box = Box(50.0,10.0)  # инициализация экземпляра класса
         """

        if not isinstance(edge, float):
            raise TypeError("Сторона коробки должна быть типа float")
        if edge <= 0:
            raise ValueError("Сторона коробки должна быть быть положительным числом")
        self.edge = edge

        if not isinstance(sand, float):
            raise TypeError("Объем песка внутри должно быть типа float")
        if sand <= 0:
            raise ValueError("Объем песка внутри быть быть положительным числом")
        self.sand = sand

    def count_volume(self) -> float:
        """
                Функция которая позволяет вычислить объем коробки
                :return: Объем коробки
                Примеры:
                >>> box = Box(30.0, 10.0)
                >>> box.count_volume()
        """
        ...

    def is_empty_box(self) -> bool:
        """
        Функция которая проверяет является ли коробка пустой
        :return: Является ли коробка пустой
        Примеры:
        >>> box = Box(30.0, 10.0)
        >>> box.is_empty_box()
        """
        ...

class Wardrobe:
    """
        Документация на класс.
        Класс описывает модель шкафа.
    """

    def __init__(self, shelf: int, hanger: int):
        """
         Создание и подготовка к работе объекта Шкаф.
         :param shelf: количество полок
         :param hanger: количество занятых вешалок
         Примеры:
         >>> wardrobe = Wardrobe(10,10)  # инициализация экземпляра класса
         """

        if not isinstance(shelf, int):
            raise TypeError("Количество полок должно быть типа int")
        if shelf <= 0:
            raise ValueError("Количество полок должно быть быть положительным числом")
        self.shelf = shelf

        if not isinstance(hanger, int):
            raise TypeError("количество вешалок  должно быть типа int")
        if hanger <= 0:
            raise ValueError("количество вешалок должно быть быть положительным числом")
        self.hanger = hanger

    def count_volume(self) -> int:
        """
                Функция которая позволяет вычислить количество вешалок
                :return: Количество вешалок
                Примеры:
                >>> wardrobe = Wardrobe(10,10)
                >>> wardrobe.count_volume()
        """
        ...

    def is_empty_wardrobe(self) -> bool:
        """
        Функция которая проверяет есть ли в шкафу вешалки
        :return: Является ли шкаф пустым
        Примеры:
        >>> wardrobe = Wardrobe(10,10)
        >>> wardrobe.is_empty_wardrobe()
        """
        ...




if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
