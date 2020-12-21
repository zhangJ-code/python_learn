"""
    2048 游戏核心算法
"""
# list_merge = [2, 0, 0, 2]
#
#
# # 1. 定义函数　zero_to_end()
# # [2,0,2,0]  -->  [2,2,0,0]
# # [2,0,0,2]  -->  [2,2,0,0]
# # [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

#
# # zero_to_end()
# # print(list_merge)
#
#
# 2. 定义函数　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
def merge():
    """
        合并数据
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# merge()
# print(list_merge)

# 3. 向左移动
# map = [
#     [2, 0, 0, 2],
#     [4, 2, 0, 2],
#     [2, 4, 2, 4],
#     [4, 4, 4, 2],
# ]


def move_left():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        list_merge = line
        merge()  # 操作list_merge,但是等同于操作map

# move_left()
# for item in map:
#     print(item)

# 4. 向右移动 move_right
def move_right():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        # 从右向左获取数据形成新列表
        list_merge = line[::-1]
        merge()  # 因为   line[::-1]所以向左移动等同于向右移动
        # 将处理后的数据再从右向左还给map
        line[::-1] = list_merge
        # line[:] = list_merge[::-1]


#5.转置函数
def convert():
    for c in range(1,len(map)):
        for r in range(c,len(map)):
            map[r][c-1],map[c-1][r]=map[c-1][r],map[r][c-1]
    # for r in range(1,4):
    #     map[r][0],map[0][r]=map[0][r],map[r][0]
        # for c in range(2,4):
            # map[c][1], map[1][c] = map[1][c], map[c][1]
            # for i in range(3,4):

                # map[i][2],map[2][i]=map[2][i],map[i][2]

#.
def move_up():
    convert()
    move_left()
    convert()


def move_down():
    convert()
    move_right()
    convert()

map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [4, 4, 4, 2],
]
move_down()
for item in map:
    print(item)