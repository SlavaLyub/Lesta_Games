from collections import deque


class CircularBufferList:
    """
    Плюсы:
        Простая реализация, легко понять работу с индексами.
        Подходит для сценариев с фиксированным размером,
        не требуется выделение памяти динамически.
    Минусы:
        Необходимо вручную управлять
        индексами и проверками на переполнение.
        Присутствуют дополнительные операции
        при обновлении индексов и проверке заполненности.
        При большом размере управление индексами и операции копирования
        могут быть медленнее по сравнению со стандартными структурами данных.
    """
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.start = 0
        self.end = 0
        self.is_full = False

    def append(self, value):
        self.buffer[self.end] = value
        self.end = (self.end + 1) % self.size
        if self.is_full:
            self.start = (self.start + 1) % self.size
        self.is_full = self.end == self.start

    def pop(self):
        if not self.is_full and self.start == self.end:
            raise IndexError("Буфер пуст!")
        value = self.buffer[self.start]
        self.start = (self.start + 1) % self.size
        self.is_full = False
        return value

    def __repr__(self):
        if self.is_full:
            return f"Заполнен: {self.buffer}"
        elif self.start <= self.end:
            return f"Буфер: {self.buffer[self.start:self.end]}"
        else:
            return f"Буфер: {self.buffer[self.start:]} + {self.buffer[:self.end]}"


class CircularBufferDeque:
    """
    Плюсы:
        Простота реализации благодаря использованию встроенной
        структуры данных deque, которая автоматически управляет буфером.
        Оптимизирован для добавления и удаления элементов с обоих концов,
        что делает операции вставки и удаления O(1).
        Автоматическое управление размером буфера,
        переполнение обрабатывается без необходимости ручного управления
        индексами.
    Минусы:
        Меньшая гибкость в управлении, так как максимальный размер фиксируется
        при создании и нельзя динамически изменять размер буфера.
        Меньший контроль над внутренними процессами
        (например, управление индексами),
        что может быть важно.
    """
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def append(self, value):
        self.buffer.append(value)

    def pop(self):
        if not self.buffer:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()

    def __repr__(self):
        return f"Buffer: {list(self.buffer)}"
