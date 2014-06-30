'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''
def find_in_A(A, x):
    low  = 0
    high = len(A) - 1
    
    # FIXME: 写的真是一团糟，完全不知道算法在干什么，思路不清晰
    while low != high:
        mid  = (low + high) >> 1
        print mid, low, high
        if A[mid] == x:
            return mid
        elif A[low] <= A[mid]:
            if A[mid] > x and x > A[low]:
                high = mid
            else:
                low = mid + 1
        else:
            if A[mid] < x and x < A[high]:
                low = mid + 1
            else:
                high = mid
    return -1

if __name__ == '__main__':
    A = [4, 5, 6, 7, 0, 1, 2]
    #A = range(1, 10)
    x_list = [4, 2, 7, 0, -1]
    for x in x_list:
        #print x, find_in_A(A, x)
        find_in_A(A, x)