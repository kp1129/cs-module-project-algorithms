'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    # Your code here
 
    # plan
    # first, understand what im being asked to do, 
    # because this is like the third time
    # i have to rewrite this

    # create a results  list

    # for i in range(0, len(arr)):
    # create a list that doesn't contain
    # the element at that index
    # multiply all the elements

    # append the answer to the results list

    # return results

    products = []
    for i in range(0, len(arr)):
        my_list = list(arr)
        my_list.pop(i)
        counter = 1
        for each in my_list:
            counter *= each
        products.append(counter)

    return products

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [1, 7, 3, 4]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
