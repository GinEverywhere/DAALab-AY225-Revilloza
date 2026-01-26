import time
from time import perf_counter

def bubble_sort(arr):
    n = len(arr)
    # Start the timer using perf_counter
    start_time = perf_counter()
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # End the timer
    end_time = perf_counter()
    print(f"Sorted array: {arr}")
    print(f"Sorting time: {end_time - start_time} seconds")

# Example usage: 
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)