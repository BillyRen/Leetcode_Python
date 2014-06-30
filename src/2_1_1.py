'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, Given input array A = [1,1,2], Your function should return length = 2, and A is now [1,2].
'''

def remove_duplicate_1(A):
    if len(A) == 0:
        return 0
    
    return len(set(A))

def remove_duplicate_2(A):
    if len(A) == 0:
        return 0

    length = 1    
    for i, item in enumerate(A[1:]):
        if A[i] != item:
            length += 1
    
    return length

if __name__ == '__main__':
    As = [1, 1, 2, 2, 3, 3, 4, 5]
    print remove_duplicate_1(A)
    print remove_duplicate_2(A)