"""
@AUthor:Reese
@Date:2018/12/23 22:15
@Description:直接插入排序 时间复杂度O(n2) 空间复杂度O(1) 稳定 简单
@优化：因为在一个有序序列中查找一个插入位置，以保证有序序列的序列不变，所以可以使用二分查找，减少元素比较次数提高效率。

二分查找是对于有序数组而言的，假设如果数组是升序排序的。那么，二分查找算法就是不断对数组进行对半分割，
每次拿中间元素和目标数字进行比较，如果中间元素小于目标数字，则说明目标数字应该在右侧被分割的数组中，
如果中间元素大于目标数字，则说明目标数字应该在左侧被分割的数组中。
@原文：https://cuijiahua.com/blog/2017/12/algorithm_2.html
"""


def insertSort(input_list):
    """
    函数说明：
    :param input_list:
    :return:
    """
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    for i in range(1, len(sorted_list)):
        temp = sorted_list[i]
        j = i - 1
        while j >= 0 and temp < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = temp
    return sorted_list


def BinarySearch(input_list, end, value):
    left = 0
    right = end - 1
    while left <= right:
        middle = left + (right - left) // 2
        if input_list[middle] >= value:
            right = middle - 1
        else:
            left = middle + 1
    return left if left < end else -1


def BinaryInsertSort(input_list):
    if len(input_list) == 0:
        return []
    result = input_list
    for i in range(1, len(input_list)):
        j = i - 1
        temp = result[i]
        insert_index = BinarySearch(result, i, result[i])
        if insert_index != -1:
            while j >= insert_index:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = temp
    return result


if __name__ == '__main__':
    input_list = [6, 8, 9, 2, 3, 1]
    print("排序前：", input_list)
    # sorted_list = insertSort(input_list)
    sorted_list = BinaryInsertSort(input_list)
    print("排序后：", sorted_list)
