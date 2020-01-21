def bubble_sort(lst):
    """冒泡排序"""
    for i in range(len(lst)): # 遍历数组
        for j in range(len(lst)-i-1): # 后i个元素已经排好了
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst


def bubble_sort_advanced(lst):
    """改进后的冒泡排序"""
    flag = True
    while flag:
        for i in range(len(lst)):
            changed = False
            for j in range(len(lst)-i-1):
                if lst[j] > lst[j+1]:
                    lst[j],lst[j+1] = lst[j+1],lst[j]
                    changed = True
            if not changed: flag = False
    return lst
                

if __name__ == "__main__":
    lst = [3,5,4,2,1]
    print(bubble_sort(lst))
    print(bubble_sort_advanced(lst))