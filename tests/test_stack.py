"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack


def test_node():
    n1 = Node(5, None)
    n2 = Node('a', n1)
    assert n1.data == 5
    assert n2.data == 'a'


def test_steck():
    stack = Stack()
    stack.push('one')
    stack.push('two')
    stack.push('three')

    assert stack.top.data == 'three'
    assert stack.top.next_node.data == 'two'
    assert stack.top.next_node.next_node.data == 'one'
    assert stack.top.next_node.next_node.next_node is None


def test_pop():
    stack = Stack()
    stack.push('one')
    stack.push('two')
    data = stack.pop()
    assert stack.top.data == 'one'
    data = stack.pop()
    assert data == 'one'
    assert stack.top is None
