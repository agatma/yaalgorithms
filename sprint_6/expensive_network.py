"""
ПРИНЦИП РАБОТЫ
    Составляем остовное дерево. Храним самое тяжёлое ребро в куче, используя heapq.

    Функция add_vertex() служит для добавления вершины в остов. При этом проводится проверка исходящих ребер
    данной вершины на отсутствие этих ребер (вершин ребра) в множестве вершин, добавленных в остов.
    В этом случае эти вершины добавляются в массив ребер, исходящих из остовного дерева посредством функции heapq,
    с целью преобразования edges в кучу для использования пирамидальной сортировки min_heap, при этом в данный
    массив добавляем вес ребра с отрицательным значением для нужного нам результата сортировки.
    То есть в начале списка будут лежать не минимальные значения, а максимальные.

    Непосредственно реализована функция для поиска максимального остовного дерева. На вход передаем граф.
    В самом начале определяемся с тем, что будем начинать обходить граф с 1-ой вершины.
    Далее циклом, пока длина множества added не равна значению вершин в графе и массив (куча)  существуют
    (имеет элементы), берем "минимальный" (максимальный) элемент из кучи edges.
    Проверяем, что вершины этого ребра нет во множестве вершин, добавленных в остов и, в таком случае, к значению
    максимального остовного дерева maximum_spanning_tree прибавляем вес максимального ребра, как раз того, что мы
    забарали из кучи. После чего вызваем функцию add_vertex() для добавления данной вершины в остов.
    Когда цикл завершится, необходимо проверить, что длина множества added равно количеству вершин графа.
    В этом случае вернем значение maximum_spanning_tree, что и будет передавать значение максимального остовного дерева.
    В противном случае, если в графе несколько компонент связности, выведем сообщение: 'Oops! I did it again'.

ВРЕМЕННАЯ СЛОЖНОСТЬ
    O(E*logV), где E - количество рёбер в графе, а V - количество вершин.

    В рамках реализации нашего алгоритма мы использовали приоритетную очередь. Это говорит о том, что
    для поиска минимального (максимального элемента) мы затрачиваем О(logV) времени, где V - количество вершин в графе.
    Таким образом если вместе с ребром в подграф добавляется новая вершина, то это ребро добавляется в остов.
    Если ребро соединяет две вершины, уже присутствующее в подмножестве остова, мы отбрасываем его из дальнейшего
    рассмотрения и из кучи в том числе.
    В общем случае временная сложность алгоритма получается O(E*logV), где E - количество ребер графа.

ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
    Хранение кучи - O(n).
    Список смежности - O(E*V), где E - количество вершин, V - количество рёбер.

УСПЕШНАЯ ПОСЫЛКА
    66717360
"""
import heapq


def add_vertex(vertex, graph_edges, added, edges):
    added[vertex] = True

    for edge, weight in graph_edges:
        if not added[edge]:
            heapq.heappush(edges, (-weight, edge))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append((t, w))
    graph[t].append((f, w))


added, edges = [False] * (n+1), []
maximum_spanning_tree = 0

added[0] = True
add_vertex(1, graph[1], added, edges)

while not all(added) and edges:
    weight, vertex = heapq.heappop(edges)
    if not added[vertex]:
        maximum_spanning_tree += abs(weight)
        add_vertex(vertex, graph[vertex], added, edges)

print(maximum_spanning_tree if all(added) else 'Oops! I did it again')
