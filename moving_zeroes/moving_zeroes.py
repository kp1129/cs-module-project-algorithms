'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     for i in arr:
#         if i == 0:
#             arr.pop(arr.index(0))
#             arr.append(0)
#     return arr

#  the problem with the above solution is the 
# cost of an intermediate pop, which is O(n)
# in the worst case due to all of the shifts
# that occur


# a better solution: swaps with pointers
def moving_zeroes(arr):
    # initialize a left and right pointers
    left = 0
    right = len(arr) -1

    # as long as left and right don't cross each other
    while left <= right:
    # if left points at zero and right points at non zero
        if arr[left] == 0 and arr[right] != 0:
            # swap
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            # increment left and decrement right
            left += 1
            right -= 1
        else:
        # if left points at non zero, increment left
            if arr[left] != 0:
                left += 1
        # if right points at zero, decrement right
            if arr[right] == 0:
                right -= 1

    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")