def insert_sort(arr):
    # 第一个数已经排序，从第二位开始
    for i in range(1,len(arr)):
        item_to_insert = arr[i]
        j = i - 1 # 保留前一个元素索引的引用 
        # 如果已排序段的所有项目大于要插入的项目，则将它们向前移动
        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1
        # 插入
        arr[j + 1] = item_to_insert
    return arr

arr = [1,5,3,4,2]
print(insert_sort(arr))
            