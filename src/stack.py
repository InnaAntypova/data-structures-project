class Node:
    """Класс для узла стека"""

    def __init__(self, data: str, next_node: str):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.stack = []

    def push(self, data: str):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if len(self.stack) == 0:
            self.top = Node(data, None)
            self.stack.append(self.top)
        else:
            next_node = self.stack[-1]
            self.top = Node(data, next_node)
            self.stack.append(self.top)

    def pop(self) -> str:
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.top = None
            return removed.data
        else:
            self.top = self.stack[-1]
            return removed.data




