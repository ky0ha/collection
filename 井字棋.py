# 创建棋盘
lis = [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]]

# 设置先手
player = 1
# 设置输赢判断的列表
row = [0, 0, 0] # 行
column = [0, 0, 0]  # 列
diag = [0, 0]
# 设置表示游戏是否结束的变量
is_end = False

while True:
    # 要落子的位置
    i, j = map(int, input().split())

    # 落子
    lis[i][j] = player

    # 更新棋盘
    print()
    for x in lis:
        print(*x, sep=' ')
    print("\n########################\n")
    
    # 根据落子位置对输赢判断列表进行更新
    row[i] += 1 if player==1 else -1    # 第 i 行
    column[j] += 1 if player==1 else -1 # 第 j 列
    if i==j:
        diag[0] += 1 if player==1 else -1   # 正对角线，坐标为 (0, 0), (1, 1), (2, 2)
    if (i==0 and j==2) or (i==1 and j==1) or (i==2 and j==0):
        diag[1] += 1 if player==1 else -1   # 反对角线，坐标为 (0, 2), (1, 1), (2, 0)
    
    # 切换玩家，写在这里是因为对输赢列表进行更新的时候，需要判对于先手要 += 1 对于后手要 += -1
    # 如果因为提前切换先后手，则会导致此处先手变为 += -1
    if player==1:
        player = 2
    else:
        player = 1
    
    # 遍历输赢判断列表，查看是否分出胜负
    for i in row+column+diag:
        if i==3:
            print("玩家1获胜！")
            is_end = True
            break
        if i==-3:
            print("玩家2获胜！")
            is_end = True

    # 如果游戏结束，则结束 while 循环
    if is_end:
        break