class MatrixProcessor:
    def __init__(self, matrix: list[list[int]]) -> None:
        self.__matrix = [list(row) for row in matrix]
        self.__rows = len(self.__matrix)
        self.__cols = len(self.__matrix[0]) if self.__rows > 0 else 0
        if (
            self.__rows == 0
            or any(len(row) != self.__cols for row in self.__matrix)
            or self.__rows != self.__cols
        ):
            raise ValueError("Матрица должна быть квадратной!")

    def get_max_in_bottom_right_triangle(self) -> int:
        max_value = self.__matrix[0][self.__cols - 1]
        for row_idx in range(self.__rows):
            for col_idx in range(self.__cols):
                if row_idx + col_idx >= self.__rows - 1:
                    if self.__matrix[row_idx][col_idx] > max_value:
                        max_value = self.__matrix[row_idx][col_idx]

        return max_value

    def move_max_positive_to_top_left(self) -> list[list[int]]:
        max_value = None
        max_row = -1
        max_col = -1

        for row_idx in range(self.__rows):
            for col_idx in range(self.__cols):
                value = self.__matrix[row_idx][col_idx]

                if value > 0:
                    if max_value is None or value > max_value:
                        max_value = value
                        max_row = row_idx
                        max_col = col_idx

        if max_value is None:
            raise ValueError("В матрице нет положительных элементов!")

        self.__matrix[0], self.__matrix[max_row] = (
            self.__matrix[max_row],
            self.__matrix[0],
        )

        for row in self.__matrix:
            row[0], row[max_col] = row[max_col], row[0]

        return [list(row) for row in self.__matrix]


class ArrayProcessor:
    def __init__(self, array: list[int]) -> None:
        if not array:
            raise ValueError("Массив не должен быть пустым!")

        self.__array = list(array)

    def get_min_by_absolute_value(self) -> int:
        min_value = self.__array[0]

        for value in self.__array:
            if abs(value) < abs(min_value):
                min_value = value

        return min_value

    def sum_after_last_zero(self) -> int:
        if 0 not in self.__array:
            raise ValueError("В массиве должен быть хотя бы один ноль!")

        last_zero = len(self.__array) - 1 - self.__array[::-1].index(0)

        return sum(self.__array[last_zero + 1:])

    def rearrange_even_indexed_first(self) -> list[int]:
        even_indexed = self.__array[0::2]
        odd_indexed = self.__array[1::2]

        return even_indexed + odd_indexed


if __name__ == "__main__":
    matrix_data = [
        [-5, 2, 0],
        [8, 3, -1],
        [-1, 4, 9]
    ]

    m_proc = MatrixProcessor(matrix_data)

    print(
        "Максимальный элемент нижнего правого треугольника:",
        m_proc.get_max_in_bottom_right_triangle(),
    )

    print(
        "Матрица после перестановки строк и столбцов:",
        m_proc.move_max_positive_to_top_left(),
    )

    array_data = [2, -3, 0, 4, -5, 6, 0, -1, 8]

    a_proc = ArrayProcessor(array_data)

    print(
        "Минимальный по модулю элемент:",
        a_proc.get_min_by_absolute_value(),
    )

    print(
        "Сумма после последнего нуля:",
        a_proc.sum_after_last_zero(),
    )

    print(
        "Преобразованный массив:",
        a_proc.rearrange_even_indexed_first(),
    )