# // The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.

# // Assumption

# // Every array element is unique.
# // Array is 0 indexed.
# // Note:

# // If the array is empty, return 0.
# // If array length is 3 or <3, return 0.
 
# // Example

# // Input:
# // Arr: 3 2 1 7 5 4

# // Output:
# // 7

arr = list(map(int, input().split()))
even_arr = []
odd_arr = []
for i in range(len(arr)):
     if i % 2 == 0:
        even_arr.append(arr[i])
     else:
        odd_arr.append(arr[i])
even_arr.sort()
odd_arr.sort(reverse=True)
print(even_arr[1] + (odd_arr[1] ))
