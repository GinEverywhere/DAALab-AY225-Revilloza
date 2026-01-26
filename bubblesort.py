import time
from time import perf_counter

# Function to perform bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Menu functionality, data loading, and display features to remain intact

def main_menu():
    print("Bubble Sort Program")
    choice = int(input("Please enter your choice: \n1. Run Bubble Sort \n2. Exit\n"))

    while choice != 2:
        if choice == 1:
            arr = [64, 34, 25, 12, 22, 11, 90]  # Example array, replace with actual data loading logic
            start_time = perf_counter()  # Start timing
            bubble_sort(arr)
            end_time = perf_counter()  # End timing
            print(f"Sorted array: {arr}")
            print(f"Bubble sort took {end_time - start_time:.6f} seconds")
        else:
            print("Invalid choice! Please choose again.")
        choice = int(input("Please enter your choice: \n1. Run Bubble Sort \n2. Exit\n"))

if __name__ == '__main__':
    main_menu()