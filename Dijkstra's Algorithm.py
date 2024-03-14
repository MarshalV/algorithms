# Алгоритм Дейкстры (Dijkstra's Algorithm): Поиск кратчайшего пути в графе с неотрицательными весами рёбер.

"""Алгоритм Дейкстры применяется для нахождения кратчайших путей от одной из вершин (называемой исходной вершиной) до всех остальных вершин в графе с неотрицательными весами рёбер. 
Этот алгоритм обычно используется в сетях связи, транспортных сетях, GPS-навигации, маршрутизации пакетов в компьютерных сетях и во многих других приложениях,
где необходимо найти оптимальный путь с учетом весов рёбер (расстояний, времени и т. д.).

Основные особенности алгоритма Дейкстры:

 - Неотрицательные веса рёбер: Алгоритм Дейкстры работает только с графами, в которых все веса рёбер неотрицательные.
Это означает, что для нахождения кратчайших путей он не подходит для графов с отрицательными весами.

 - Жадный подход: Алгоритм Дейкстры использует жадный подход, выбирая на каждом шаге вершину с наименьшим известным расстоянием до неё.
Этот подход гарантирует, что найденные кратчайшие пути будут оптимальными.

 - Минимальная стоимость: Алгоритм Дейкстры находит кратчайшие пути, минимизируя суммарный вес пути от исходной вершины до каждой другой вершины.
"""



import heapq  # Импорт модуля heapq для использования приоритетной очереди

def dijkstra(graph, start):# Определение функции dijkstra с аргументами graph (граф в виде словаря) и start (вершина, с которой начинается поиск кратчайших путей)
    
    distances = {node: float('infinity') for node in graph}# Создание словаря distances для хранения расстояний от стартовой вершины до всех других вершин, начальные расстояния устанавливаются как бесконечность
    distances[start] = 0 # Устанавливаем расстояние до стартовой вершины равным 0

    queue = [(0, start)] # Создаем приоритетную очередь, в которую помещаем кортежи (расстояние до вершины, вершина), начиная с кортежа (0, start)
    
    while queue: # Пока в очереди есть элементы
        
        current_distance, current_node = heapq.heappop(queue) # Извлекаем из очереди кортеж с наименьшим расстоянием до вершины и саму вершину
        
        if current_distance > distances[current_node]: # Если текущее расстояние до вершины больше, чем сохраненное в словаре distances, значит, мы уже нашли более короткий путь к этой вершине, пропускаем ее
            continue
        
        for neighbor, weight in graph[current_node].items(): # Проходим по всем соседям текущей вершины и их весам (расстояниям до них)
            
            distance = current_distance + weight # Вычисляем длину пути до соседа через текущую вершину
            
            if distance < distances[neighbor]: # Если новое расстояние меньше, чем сохраненное в словаре distances, обновляем расстояние до соседа и добавляем его в очередь
                
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor)) # Добавляем новое расстояние и соседа в приоритетную очередь
                
    return distances # Возвращаем словарь расстояний от стартовой вершины до всех остальных вершин
    

# Пример графа в виде словаря с весами ребер
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Вызов функции dijkstra для поиска кратчайших путей от вершины 'A'
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Вывод результатов
print("Кратчайшие пути от вершины", start_node)
for node, distance in shortest_paths.items():
    print("До вершины", node, "расстояние:", distance)