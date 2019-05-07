arr = [i for i in range(1,6)]
#print(arr)

def rotate(arr,k):
    n = len(arr)
    k %= n
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)

def reverse(arr,start,end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


print(arr)

rotate(arr,2)
print(arr)

