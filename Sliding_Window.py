def find_subarray_sliding_window(arr, target):
    left, right = 0, 0
    current_sum = arr[0]
    
    while left <= right < len(arr):
        if current_sum == target:
            return arr[left:right+1]
        elif current_sum < target:
            right += 1
            if right < len(arr):
                current_sum += arr[right]
        else:
            current_sum -= arr[left]
            left += 1
    return None
