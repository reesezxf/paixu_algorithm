"""
@AUthor:Reese
@Date:2018/12/23 21:54
@Description: 冒泡排序 时间复杂度O(n2) 空间复杂度O(n) 稳定 简单
"""

def bubbleSort(input_list):
    """
    函数说明：冒泡排序（升序）
    Parameters: input_list（待排序列表）
    :return: sorted_list -升序排序好的列表
    """
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    for i in range(len(sorted_list)-1):
        bChanged = False
        print("第%d趟排序：" % (i+1))
        for j in range(len(sorted_list)-1):
            if sorted_list[j+1] < sorted_list[j]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                bChanged = True
            print(sorted_list)
        if not bChanged:
            break
    return sorted_list


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print("排序前：", input_list)
    sorted_list = bubbleSort(input_list)
    print("排序后：", sorted_list)