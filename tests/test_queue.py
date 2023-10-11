"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import pytest

from src.queue import Queue, Node


def test_node():
    n1 = Node(3, None)
    n2 = Node('data', n1)
    assert n1.data == 3
    assert n2.data == 'data'


def test_queue():
    queue = Queue()
    queue.enqueue('one')
    queue.enqueue('two')
    queue.enqueue('three')

    assert queue.head.data == 'one'
    assert queue.head.next_node.data == 'two'
    assert queue.tail.data == 'three'
    assert queue.tail.next_node is None


def test_str():
    queue = Queue()
    assert str(Queue()) == ""

    queue.enqueue('one')
    queue.enqueue('two')
    queue.enqueue('three')

    assert str(queue) == "one\ntwo\nthree"


def test_dequeue():
    queue = Queue()
    queue.enqueue('one')
    queue.enqueue('two')
    queue.enqueue('three')

    assert queue.dequeue() == 'one'
    assert queue.dequeue() == 'two'
    assert queue.dequeue() == 'three'
    assert queue.dequeue() is None
