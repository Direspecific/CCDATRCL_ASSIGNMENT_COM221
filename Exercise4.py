def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
            
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

def countingsort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    count = [0] * range_size

    for num in arr:
        count[num - min_val] += 1

    sorted_arr = []
    steps = 0

    for i in range(range_size):
        for j in range(count[i]):
            sorted_arr.append(i + min_val)
            steps += 1

    return sorted_arr, steps
    
def insertionSort(array):
    steps = 0

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            steps += 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return steps
        
# Bubble sort in Python
def bubbleSort(array):
  global num_of_swaps
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        num_of_swaps += 1

        
student_number = 2022103595

# Convert the student number to a list of integers
number_list = [int(digit) for digit in str(student_number)]

# Use counting sort to sort the list in ascending order
countingsort(number_list)

# Convert the sorted list back to a string
sorted_student_number = ''.join(map(str, number_list))




# Print the sorted student number
print("Sorted Student Number in Ascending Order:", sorted_student_number)

# Your birthday should be in mm-dd-yyyy format
birthday = "06-02-2003"

# Define the list of dates
dates = ["12-25-2023", birthday, "01-01-2023"]

# Define a function to convert the date string into a sortable format
def date_key(date_str):
    parts = date_str.split("-")
    return (int(parts[2]), int(parts[0]), int(parts[1]))

# Sort the dates in ascending order using the custom sorting key
sorted_dates = sorted(dates, key=date_key)

# Print the sorted dates
for date in sorted_dates:
    print(date)
    

my_list = [3,2,5,1]
num_of_swaps = 0
bubbleSort(my_list)
print("Sorted list: ", my_list)
print("Total Swaps: ", num_of_swaps)


# Given list
my_list = [6, 2, 5, 7, 4, 1, 8, 9, 3]
# Call insertion_sort to sort the list and count steps
number_of_steps = insertionSort(my_list)
print("Number of steps:", number_of_steps)

# Given list
my_list = [7, 5, 4, 3, 2, 5, 1, 8]

# Calculate steps for Merge Sort
sorted_list_merge, merge_sort_steps = mergeSort(my_list.copy())

# Calculate steps for Counting Sort (Assuming a range from 1 to 10)
sorted_list_counting, counting_sort_steps = countingsort(my_list.copy())

if merge_sort_steps < counting_sort_steps:
    print("Merge Sort is faster")
elif merge_sort_steps > counting_sort_steps:
    print("Counting Sort is faster")
else:
    print("Both algorithms have the same number of steps")

print("Merge Sort steps:", merge_sort_steps)
print("Counting Sort steps:", counting_sort_steps)
