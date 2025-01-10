# ?
def min_students_to_remove(n: int, heights: list) -> int:
    if n <= 1:
        return 0

    # Step 1: Calculate LIS for each student
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if heights[i] > heights[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    # Step 2: Calculate LDS for each student
    lds = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if heights[i] > heights[j]:
                lds[i] = max(lds[i], lds[j] + 1)

    # Step 3: Calculate the maximum choir formation length
    max_choir_length = 0
    for i in range(n):
        # Subtract 1 because the peak student is counted twice in lis and lds
        max_choir_length = max(max_choir_length, lis[i] + lds[i] - 1)

    # Step 4: Calculate the minimum number of students to remove
    return n - max_choir_length

# Example usage
n = 8
heights = [186, 186, 150, 200, 160, 130, 197, 200]
print(min_students_to_remove(n, heights))  # Output: 4