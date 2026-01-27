import time
import sys
import gc
import copy

# Increase recursion depth for Merge Sort
sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1

def load_data():
    nums = []
    try:
        with open('dataset.txt', 'r') as f:
            for line in f:
                content = line.strip()
                if not content: continue
                if ']' in content:
                    content = content.split(']')[-1].strip()
                if content.isdigit():
                    nums.append(int(content))
        return nums
    except FileNotFoundError:
        print("Error: dataset.txt not found.")
        return []

def menu():
    master_data = load_data()
    if not master_data:
        return

    while True:
        print(f"\n=== Sorting Menu ({len(master_data)} items) ===")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Merge Sort")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        if choice == '4': break
            
        if choice == '1':
            algo, name = bubble_sort, "Bubble Sort"
        elif choice == '2':
            algo, name = insertion_sort, "Insertion Sort"
        elif choice == '3':
            algo, name = merge_sort, "Merge Sort"
        else:
            continue

        # Create a fresh copy to ensure we aren't sorting an already sorted list
        working_data = copy.deepcopy(master_data)

        print(f"Measuring {name}...")

        # --- THE PRECISION ZONE ---
        gc.collect() 
        gc.disable() 
        
        # Use nanoseconds for extreme precision
        t_start = time.perf_counter_ns() 
        algo(working_data)
        t_stop = time.perf_counter_ns()
        
        gc.enable()
        # --------------------------

        # Convert nanoseconds to seconds for display
        duration_s = (t_stop - t_start) / 1_000_000_000
        
        # Display sorted result automatically
        print("\n--- Sorted Results ---")
        print(*working_data, sep="\n")
        print("----------------------")
        
        print(f"\nAlgorithm: {name}")
        print(f"Time Spent: {duration_s:.10f} seconds")
        print(f"Time in Nanoseconds: {t_stop - t_start} ns")

if __name__ == "__main__":
    menu()
