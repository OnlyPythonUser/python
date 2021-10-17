def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  lesser_arr, equal_arr, greater_arr = [], [], []
  for num in arr:
    if num < pivot:
      lesser_arr.append(num)
    elif num > pivot:
      greater_arr.append(num)
    else:
      equal_arr.append(num)
  return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
print(quick_sort([5,7,9,6,3,1,4,8,6,2,1,54,8,6,131]))
