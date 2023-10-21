class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)
        node.data = data
        if self.head is None:
            self.head = node
            return
        else:
            node.next_node = self.head
            self.head = node
            return

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        node.data = data
        if self.head is None:
            self.head = node
            return
        else:
            temp_node = self.head
            while temp_node.next_node:
                temp_node = temp_node.next_node

            temp_node.next_node = node
            return

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string

    def to_list(self):
        """ Возвращает список с данными"""
        nodes = []
        node = self.head
        while node:
            nodes.append(node.data)
            node = node.next_node
        return nodes

    def get_data_by_id(self, key_id):
        """ Возвращает первый найденный словарь с ключом 'id' """

        node = self.head

        while node:
            try:
                if node.data['id'] == key_id:
                    return node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
            finally:
                node = node.next_node


