def  bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

a=[5,6,2,8,9,1,3,71]

print(a)
print(f"After sorting : ")
print(bubble_sort(a))

