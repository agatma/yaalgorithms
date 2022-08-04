"""
ПРИНЦИП РАБОТЫ
    Для вычисления значения выражения, записанного в обратной польской нотации,
    нужно считывать выражение слева направо и придерживаться следующих шагов:
    - Обработка входного символа:
    - - Если на вход подан операнд, он помещается на вершину стека.
    - - Если на вход подан знак операции, то эта операция выполняется над требуемым количеством значений,
        взятых из стека в порядке добавления. Результат выполненной операции помещается на вершину стека.
    - Если входной набор символов обработан не полностью, перейти к шагу 1.
    - После полной обработки входного набора символов результат вычисления выражения находится в вершине стека.

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
    Стек (англ. stack - стопка) - одна из простейших структур данных,
    представляющая собой скорее ограничение простого массива, чем его расширение.

    Классический стек поддерживает всего лишь три операции:
    - Добавить элемент в стек;
    - Извлечь элемент из стека;
    - Проверить, пуст ли стек.

    Для объяснения принципа работы стека часто используется аналогия со стаканом с печеньем.
    Представьте, что на дне вашего стакана лежат несколько кусков печенья.
    Вы можете положить наверх ещё один кусок или достать уже находящийся наверху.
    Остальные куски закрыты верхним, и вы про них ничего не знаете.

    Для описания стека часто используется аббревиатура LIFO (Last In, First Out),
    подчёркивающая, что элемент, попавший в стек последним, первым будет из него извлечён.

    Статья - https://brestprog.by/topics/datastructures/.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    Добавление в стек стоит O(1).
    Извлечение из стека стоит O(1).
    Проверить, пуст ли стек стоит O(1).

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Стек, содержащий k элементов, занимает O(k) памяти.

"""

OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x,
    '*': lambda x, y: x * y,
    '/': lambda x, y: y // x
}


class NoItemsException(Exception):
    def __init__(self):
        pass


class Stack:
    def __init__(self):
        self._array = []
        self._size = 0

    @property
    def is_empty(self):
        return self._size == 0

    def push(self, element):
        self._size += 1
        self._array.append(element)

    def pop(self):
        if self.is_empty:
            raise NoItemsException
        self._size -= 1
        return self._array.pop()


stack = Stack()

for value in input().split(' '):
    operation = OPERATIONS.get(value)
    stack.push(operation(stack.pop(), stack.pop()) if operation else int(value))

print(stack.pop())
