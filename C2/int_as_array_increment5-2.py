
# Time complexity is O(n), where n is the length of A

def plus_one(A:list[int]) -> list[int]:
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10: # We are not carrying the 1 and we break out and return the updated array.
            break
        A[i] = 0
        A[i-1] += 1
    
    else:
        if A[0] == 10: # We are carrying the 1 over and adding a 0 at the end of the array and update first entry to 1.
                        # We need to also add another digit to the array using append().
            A[0] = 1
            A.append(0)
    
    return A


if __name__ == "__main__":
    assert plus_one([1,2,9]) == [1,3,0]
    assert plus_one([9,9]) == [1,0,0]
    assert plus_one([9,9,9]) == [1,0,0,0]
    assert plus_one([0,1,0]) == [0,1,1]