"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import pytest

from src.linked_list import Node, LinkedList


def test_insert_beginning():
    link_list = LinkedList()

    link_list.insert_beginning({'key_1': 'data1'})
    link_list.insert_beginning({'key_2': 'data2'})
    link_list.insert_beginning({'key_3': 'data3'})

    assert str(link_list) == " {'key_3': 'data3'} -> {'key_2': 'data2'} -> {'key_1': 'data1'} -> None"


def test_insert_at_end():
    link_list = LinkedList()

    link_list.insert_at_end({'key_1': 'data1'})
    link_list.insert_at_end({'key_2': 'data2'})
    link_list.insert_at_end({'key_3': 'data3'})

    assert str(link_list) == " {'key_1': 'data1'} -> {'key_2': 'data2'} -> {'key_3': 'data3'} -> None"


@pytest.fixture
def get_node():
    link_list = LinkedList()

    link_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    link_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
    link_list.insert_at_end({'id': 3, 'username': 'mosh_s'})
    link_list.insert_beginning({'id': 0, 'username': 'serebro'})
    link_list.insert_at_end('username')
    link_list.insert_at_end([1, 2, 3])
    return link_list


def test_to_list(get_node):
    assert LinkedList.to_list(get_node) == [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'},
                                            {'id': 2, 'username': 'mik.roz'}, {'id': 3, 'username': 'mosh_s'},
                                            'username', [1, 2, 3]]


def test_get_data_by_id(get_node):
    assert LinkedList.get_data_by_id(get_node, 1) == {'id': 1, 'username': 'lazzy508509'}
