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
