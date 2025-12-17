def swap_min_max(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for j in range(m):
        min_row = 0
        max_row = 0

        for i in range(n):
            if matrix[i][j] < matrix[min_row][j]:
                min_row = i
            if matrix[i][j] > matrix[max_row][j]:
                max_row = i

        matrix[min_row][j], matrix[max_row][j] = matrix[max_row][j], matrix[min_row][j]


# основна програма

n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))

matrix = []

print("Введіть елементи матриці (по", m, "чисел у кожному рядку):")
for i in range(n):
    row = list(map(int, input(f"Рядок {i + 1}: ").split()))
    matrix.append(row)

print("\nПочатковий масив:")
for row in matrix:
    print(*row)

swap_min_max(matrix)

print("\nМасив після перестановки мінімального та максимального елементів у кожному стовпці:")
for row in matrix:
    print(*row) 
