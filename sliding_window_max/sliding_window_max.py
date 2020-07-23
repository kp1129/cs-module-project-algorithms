'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # iterate over the array
    # grab slices of length k at a time,
    # moving up by one

    # compare elements in each slice to each other
    # grab the max value element
    # save it in a separate list

    # return the list of max values

    max_values = []

    sliding = True
    start = 0

    while sliding:
        end = start + k
        my_slice = nums[start: end]
        my_max = max(my_slice)
        max_values.append(my_max)
        if end + 1 <= len(nums):
            start += 1
        else:
            sliding = False    

    return max_values


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
