def bubble_sort(abc):
    n = len(abc)
    for i in range(n):
        for j in range(0, n-i-1):
            if abc[j] > abc[j+1]:
                abc[j], abc[j+1] = abc[j+1], abc[j]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted list:", my_list)
