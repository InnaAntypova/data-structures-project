class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.queue = []
        self.tail = None  # конец очереди
        self.head = None  # начало очереди

    def __str__(self):
        """ Метод выводит пользователю данные очереди"""
        return '\n'.join(self.queue)
        #return f"Queue: {'/n'.join(self.queue)}"

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if len(self.queue) == 0:
            self.head = node
            self.tail = node
            self.queue.append(data)
        else:
            self.tail.next_node = node
            self.tail = node
            self.queue.append(data)


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

