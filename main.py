import random
import timeit


# --СОРТУВАННЯ ВСТАВКАМИ--

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a



# --СОРТУВАННЯ ЗЛИТТЯМ--

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)



# --ОБʼЄДНАННЯ k ВІДСОРТОВАНИХ СПИСКІВ--

def merge_k_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged.append(merge(lists[i], lists[i + 1]))
            else:
                merged.append(lists[i])
        lists = merged

    return lists[0]



# --ЕМПІРИЧНЕ ТЕСТУВАННЯ--

def benchmark():
    sizes = [1000, 5000, 10000]

    print("Порівняння алгоритмів сортування:\n")

    for size in sizes:
        data = random.sample(range(size * 10), size)

        t_insert = timeit.timeit(
            stmt="insertion_sort(data)",
            globals={"data": data, "insertion_sort": insertion_sort},
            number=1
        )

        t_merge = timeit.timeit(
            stmt="merge_sort(data)",
            globals={"data": data, "merge_sort": merge_sort},
            number=1
        )

        t_timsort = timeit.timeit(
            stmt="sorted(data)",
            globals={"data": data},
            number=1
        )

        print(f"Розмір масиву: {size}")
        print(f"Insertion sort: {t_insert:.4f} сек")
        print(f"Merge sort:     {t_merge:.4f} сек")
        print(f"Timsort:        {t_timsort:.4f} сек")
        print("-" * 40)



if __name__ == "__main__":
    benchmark()

    #Приклад для необовʼязкового завдання
    lists = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    print("\nОбʼєднання k відсортованих списків:")
    print(merge_k_lists(lists))
