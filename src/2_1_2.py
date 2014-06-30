'''
Follow up for "Remove Duplicates": What if duplicates are allowed at most twice?
For example, Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3]
'''

def remove_duplicate(A):
    if len(A) == 0:
        return 0

    cnt = 1
    A_out = []
    A_out.append(A[0])

    for idx, item in enumerate(A[1:]):
        if item == A[idx]:
            cnt += 1
        else:
            cnt = 0
        #print A_out, cnt
        if cnt <= 2:
            A_out.append(item)

    return A_out

if __name__ == '__main__':
    A = [1, 1, 1, 2, 2, 3]
    print remove_duplicate(A)