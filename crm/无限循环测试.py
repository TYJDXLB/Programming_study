import random # 引入随机数模块

adj = [ #有 边(能过去)的路径定义为1，无边的定义为0
    [0, 1, 0, 0],  # 节点0，只能去往节点1
    [0, 0, 1, 1],  # 节点1，能去往节点2，3
    [1, 0, 0, 1],  # 节点2，能去往节点0，3
    [1, 0, 0, 0]   # 节点3，只能去往节点0
]

def play_animation(aniId): # 播放动画函数，用显示随机数字代替
    print(aniId, end='')

if __name__ == "__main__":  # 如果当前函数为主函数
    pos = 0 # 当前节点数
    while True: # 循环播放
        x = random.randint(0, 3)
        while 0 == adj[pos][x]: # 判断是否为0，为0则无边，就再随机一个x直到为1为止(即有边可以到下一个节点)
            x = random.randint(0, 3)
        play_animation(x)
        pos = x # 更新当前位置，去往x节点，下一轮从x出发