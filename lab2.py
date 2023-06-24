import random
import sys
import time
import matplotlib.pyplot as plt
# Sorting Algorithms
from algorithms import *

# Helper Functions

def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

def measure_memory_usage(func, *args, **kwargs):
    arg_size = sum(sys.getsizeof(arg) for arg in args)
    kwarg_size = sum(sys.getsizeof(value) for value in kwargs.values())
    total_size = arg_size + kwarg_size
    result = func(*args, **kwargs)
    result_size = sys.getsizeof(result)
    memory_usage = total_size + result_size
    return memory_usage

def plot_complexity():
    sizes = [100, 200, 300, 400, 500]  # Розміри масивів
    bubble_sort_times = []
    selection_sort_times = []
    insertion_sort_times = []
    merge_sort_times = []
    quick_sort_times = []
    bubble_sort_memory = []
    selection_sort_memory = []
    insertion_sort_memory = []
    merge_sort_memory = []
    quick_sort_memory = []

    for size in sizes:
        array = generate_random_array(size)

        bubble_sort_time = measure_time(bubble_sort, list(array))
        selection_sort_time = measure_time(selection_sort, list(array))
        insertion_sort_time = measure_time(insertion_sort, list(array))
        merge_sort_time = measure_time(merge_sort, list(array))
        quick_sort_time = measure_time(quick_sort, list(array))

        bubble_sort_memory_usage = measure_memory_usage(bubble_sort, list(array))
        selection_sort_memory_usage = measure_memory_usage(selection_sort, list(array))
        insertion_sort_memory_usage = measure_memory_usage(insertion_sort, list(array))
        merge_sort_memory_usage = measure_memory_usage(merge_sort, list(array))
        quick_sort_memory_usage = measure_memory_usage(quick_sort, list(array))

        bubble_sort_times.append(bubble_sort_time)
        selection_sort_times.append(selection_sort_time)
        insertion_sort_times.append(insertion_sort_time)
        merge_sort_times.append(merge_sort_time)
        quick_sort_times.append(quick_sort_time)

        bubble_sort_memory.append(bubble_sort_memory_usage)
        selection_sort_memory.append(selection_sort_memory_usage)
        insertion_sort_memory.append(insertion_sort_memory_usage)
        merge_sort_memory.append(merge_sort_memory_usage)
        quick_sort_memory.append(quick_sort_memory_usage)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(sizes, bubble_sort_times, label="Bubble Sort")
    plt.plot(sizes, selection_sort_times, label="Selection Sort")
    plt.plot(sizes, insertion_sort_times, label="Insertion Sort")
    plt.plot(sizes, merge_sort_times, label="Merge Sort")
    plt.plot(sizes, quick_sort_times, label="Quick Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Complexity (Time)")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(sizes, bubble_sort_memory, label="Bubble Sort")
    plt.plot(sizes, selection_sort_memory, label="Selection Sort")
    plt.plot(sizes, insertion_sort_memory, label="Insertion Sort")
    plt.plot(sizes, merge_sort_memory, label="Merge Sort")
    plt.plot(sizes, quick_sort_memory, label="Quick Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Memory Usage (bytes)")
    plt.title("Sorting Algorithm Complexity (Memory)")
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    sizes = [100, 200, 300, 400, 500]  # Розміри масивів

    for size in sizes:
        array = generate_random_array(size)

        bubble_sort_time = measure_time(bubble_sort, list(array))
        selection_sort_time = measure_time(selection_sort, list(array))
        insertion_sort_time = measure_time(insertion_sort, list(array))
        merge_sort_time = measure_time(merge_sort, list(array))
        quick_sort_time = measure_time(quick_sort, list(array))

        bubble_sort_memory_usage = measure_memory_usage(bubble_sort, list(array))
        selection_sort_memory_usage = measure_memory_usage(selection_sort, list(array))
        insertion_sort_memory_usage = measure_memory_usage(insertion_sort, list(array))
        merge_sort_memory_usage = measure_memory_usage(merge_sort, list(array))
        quick_sort_memory_usage = measure_memory_usage(quick_sort, list(array))

        print(f"Array size: {size}")
        print(f"Bubble Sort time: {bubble_sort_time} seconds")
        print(f"Selection Sort time: {selection_sort_time} seconds")
        print(f"Insertion Sort time: {insertion_sort_time} seconds")
        print(f"Merge Sort time: {merge_sort_time} seconds")
        print(f"Quick Sort time: {quick_sort_time} seconds")
        print(f"Bubble Sort memory usage: {bubble_sort_memory_usage} bytes")
        print(f"Selection Sort memory usage: {selection_sort_memory_usage} bytes")
        print(f"Insertion Sort memory usage: {insertion_sort_memory_usage} bytes")
        print(f"Merge Sort memory usage: {merge_sort_memory_usage} bytes")
        print(f"Quick Sort memory usage: {quick_sort_memory_usage} bytes")
        print()

    # Візуалізуємо теоретичну складність
    plot_complexity()

if __name__ == "__main__":
    main()

