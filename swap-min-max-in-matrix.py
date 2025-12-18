def swap_min_max(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for b in range(m):
        min_row = 0
        max_row = 0

        for a in range(n):
            if matrix[a][b] < matrix[min_row][b]:
                min_row = a
            if matrix[a][b] > matrix[max_row][b]:
                max_row = a

        matrix[min_row][b], matrix[max_row][b] = matrix[max_row][b], matrix[min_row][b]


#основна програма

n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))

matrix = []
for x in range(n):
    matrix.append(list(map(int, input(f"Рядок {x + 1}: ").split())))

swap_min_max(matrix)

print("\nМасив після перестановки:")
for row in matrix:
    print(*row)


