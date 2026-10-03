from knapsack import knapsack
from lcs import lcs_length
from partitions import count_partitions
from floyd_warshall import floyd_warshall, print_matrix, INF


print("=== 1. Задача о рюкзаке ===")
weights = [1, 3, 4, 5]
values  = [1, 4, 5, 7]
capacity = 7
print(f"Веса:        {weights}")
print(f"Стоимости:   {values}")
print(f"Вместимость: {capacity}")
print(f"Максимум:    {knapsack(weights, values, capacity)}")

print("\n=== 2. LCS ===")
for a, b in [("ABCBDAB", "BDCABA"), ("AGGTAB", "GXTXAYB"), ("abc", "abc"), ("abc", "xyz")]:
    print(f"  LCS('{a}', '{b}') = {lcs_length(a, b)}")

print("\n=== 3. Разбиения числа ===")
for n in range(1, 11):
    print(f"  p({n}) = {count_partitions(n)}")

print("\n=== 4. Флойд-Уоршелл ===")
graph = [
    [0,   3,   INF, 7],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1],
    [2,   INF, INF, 0],
]
print("Исходная матрица:")
print_matrix(graph)
print("\nМатрица кратчайших путей:")
print_matrix(floyd_warshall(graph))