def select_sort(arr):
    """选择排序"""
    for i in range(len(arr)):
        lowest_index = i
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                lowest_index = j
        arr[lowest_index], arr[i] = arr[i],arr[lowest_index]
    return arr

if __name__ == "__main__":
    arr=[1,2,5,4,3,9,24,56,7]
    print(select_sort(arr))
