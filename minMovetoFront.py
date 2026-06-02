
def minMoves(arr, n):
    
    # Since we traverse array from end, 
    # expected item is initially n
    expectedItem = n

    # Traverse array from end
    for i in range(n - 1, -1, -1):
        
        # If current item is at its
        # correct position, decrement
        # the expectedItem (which also
        # means decrement in minimum
        # number of moves)
        if (arr[i] == expectedItem):
            expectedItem -= 1
    return expectedItem
    
# Driver Code
arr = [4, 3, 4, 2, 1,4,9,8,6]
n = len(arr)
print(minMoves(arr, n))

