'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     # Your code here
#     temp = []
#     doubles = []
#     for i in arr:
#         if i not in temp:
#             temp.append(i)
#         elif i in temp:
#             temp.pop(temp.index(i))
#             doubles.append(i)
    
#     return temp[0]


# a better solution, now its O(n) 
# because it's 2 sequential for loops 
# and we're not searching an array for 
# an item (which isnt great) but a dict

def single_number(arr):
    # Your code here
    counts = {}
    for i in arr:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    
    for k, v in counts.items():
        if v == 1:
            return k



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")