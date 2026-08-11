# print("hello word")
# #练习1：
# print("""
# # # # # # #  #
# # 白日依山尽 #
# # 黄河入海流 #
# # 欲穷千里目 #
# # 更上一层楼 #
# # # # # # #  #
# """)
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #布尔类型本质也是整数类型(int)True - 1 ； False - 0
# print(True + 1)   #2
# print(False - 1)  #-1
# #练习2：
# num1,num2,num3 = 100,200,300
# print("三个数分别是：{0}，{1}，{2}".format(num1,num2,num3))
# #练习3:
# a = 100
# b = 200
# c = 300
# print(f"\t三个数分别为：\na = {a};\nb = {b};\nc = {c}") #\t表示前方加一个tab
# d = c
# c = a
# a = b
# b = d
# print(f"\t互换后三个数分别为：\na = {a};\nb = {b};\nc = {c}")
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #type(数据)语句得到数据类型；isinstance(数据,类型)用于判断是否为指定的类型返回bool值
# 数据 = "Hello World!"
# print(type(数据)) #<class 'str'>
# print(isinstance(数据,str)) #True

# s1 = "黑马"
# s2 = "涛"
# print("该课程为%s程序员，%s老师进行讲解" % (s1,s2)) #%s为占位符
# print(f"该课程为{s1}程序员，{s2}老师进行讲解") #f快速格式化
# print("该课程为{0}程序员，{1}老师进行讲解".format(s1,s2)) #以上结果均为：该课程为黑马程序员，涛老师进行讲解

# #练习4：
# 密码 = "123456"
# 余额 = 10000
# if input("请输入密码：") == 密码:
#     out = float(input("请输入取出金额："))
#     if out < 余额:
#         余额 -= out
#         print(f"您的余额为：{余额}")
#     else:
#         print("余额不足！")
# else:
#     print("密码错误！")
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
#运算符：加+；减-；乘*；除/；整除//（除完取整）；取余%（取除完的余数）；幂指数**
#逻辑运算符：and or not
# #练习5：
# num = int(input())
# if 10 <= num and num <= 20:
#     print(f"10<{num}<20")
# else:
#     print("不在此范围！")

#练习6
# hao = input("请输入账号：")
# mi = input("请输入密码：")
# if hao == "18888" and mi == "123456":
#     print("You Pass!")
# else:
#     print("Loaded faild")

# #练习7：
# year = int(input("请输入年份："))
# if year % 100 == 0: #判断整百年份
#     if year % 400 == 0:
#         print("是闰年")
#     else:
#         print("不是闰年")
# elif year % 4 == 0:
#     print("是闰年")
# else:
#     print("不是闰年")
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# i = 0
# while i < 10:
#     print("循环中------")
#     i += 1
# else:
#     print("循环结束")

# #练习8：
# total = 0   #总数值
# i = 0
# while i < 101:  #循环1-100的数
#     if i % 2 == 0:  #判断是否为偶数
#         total += i
#     i += 1  #递归i
# print(f"1-100之间偶数和为：{total}")

# str = "Hello_Python"
# for i in str:
#     print(i)
# else:
#     print("循环结束，输出字符串")

"""
range语句：
range(end)-->获取一个从0开始，到end结束（不含end）的数字序列
range(start,end)-->获取一个从start开始，到end结束（不含end）的数字序列
range(start,end,step)-->获取一个从start开始，到end结束（不含end）的数字序列，步长为step
"""
# #练习9：
# total = 0
# for i in range(1,101,2):   #遍历1-100
#     total += i
# print(f"1-100奇数和为：{total}")
# total_1 = 0
# for i in range(100,501):
#     if i % 3 == 0:  #如果是3的倍数
#         total_1 += i
# print(f"100-500之间的3的倍数和为：{total_1}")

# #练习10:
# long = int(input("输入长度："))
# wide = int(input("输入宽度："))
# for i in range(wide):
#     for i in range(long):
#         print("*" , end=" ") #由于print语句末尾为自动换行加个end=""，即可自定义以什么结尾
#     print() #换行用的

# #练习11：
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} X {i} = {j*i}",end="\t")
#     print()

#练习12:
"""
while True:语句表示一直循环，想跳出用break关键字跳出即可(用break时，while的else语句不会被执行)
continue语句，表示跳出本次循环，继续执行下次循环
"""
# while True:
#     hao = input("请输入帐号：")
#     mi = input("请输入密码：")

#     if hao == "" or mi == "":
#         print("账号或密码不可为空！")
#         continue #跳出本次循环

#     if hao == "admin" and mi == "666888":
#         print("登入成功，进入B站首页")
#         break   #跳出循环
#     elif hao == "zhangsan" and mi == "123456":
#         print("登入成功，进入B站首页")
#         break
#     elif hao == "taoge" and mi == "888666":
#         print("登入成功，进入B站首页")
#         break
#     else:
#         print("用户名或密码错误，请重新输入!")

# #练习13:
# import random   #引入模块

# random_number = random.randint(1,100)   #random.randint(a,b)生成a-b之间的随机数为int类型
# while True:
#     player_number = int(input("请输入您所猜数字："))
#     if player_number < random_number:
#         print("小了")
#     elif player_number > random_number:
#         print("大了")
#     else:
#         print("刚刚好！")
#         break   #跳出循环
# print(f"随机数为{random_number}")
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #列表操作list
# #定义
# list = [56,90,88,"Hello","world"]
# print(type(list))   #list
# #访问列表元素
# #获取
# print(list[2])  #88 正向索引从0开始
# print(list[-2]) #Hello 反向索引从-1开始
# #修改
# list[1] = "num1"
# print(list[1])  #num1
# #删除
# del list[1]
# print(list)     #[90,88,"Hello","world"]
# #遍历
# for i in list:
#     print(i)

# #切片操作   s[开始索引:结束索引:步长](不包含结束索引,默认开头为0，步长为1)
# s = ["a","b","c","d","e","f","g"]
# print(s[0:4:2]) #["a","c"]
# print(s[:4:])   #["a","b","c","d"]
# print(s[:4])   #["a","b","c","d"]   第二个冒号可省略，第一个不可省略否则含义变为第几个索引
# print(type(s[0:4:2]))   #list
# print(s[0:-2:2])    #["a","c","e"]  反向索引也适用

# #列表里的方法
# s = [22,55,11,33,44,99,66,77,33]
# #append()   在列表尾追加元素
# s.append(100)
# print(s)    #[22, 55, 11, 33, 44, 99, 66, 77, 33, 100]
# #insert()   在指定索引前插入元素
# s.insert(4,88)
# print(s)    #[22, 55, 11, 33, 88, 44, 99, 66, 77, 33, 100]
# #remove()   #移除列表中第一个匹配到的元素
# s.remove(33)
# print(s)    #[22, 55, 11, 88, 44, 99, 66, 77, 33, 100]
# #pop()      删除列表中指定索引位置的元素并返回（如未指定则默认删除最后一个）
# s.pop(1)
# print(s)    #[22, 11, 88, 44, 99, 66, 77, 33, 100]
# s.pop()
# print(s)    #[22, 11, 88, 44, 99, 66, 77, 33]
# #sort()     排序
# s.sort()
# print(s)    #[11, 22, 33, 44, 66, 77, 88, 99]
# #reverse()  翻转列表元素
# s.reverse()
# print(s)    #[99, 88, 77, 66, 44, 33, 22, 11]

# #练习14：
# num_list = []   #定义一个空列表
# total = 0   #定义数字和
# for i in range(10):
#     num = int(input(f"请输入第{i+1}个数字:"))  #输入数字
#     num_list.append(num)    #添加到列表尾部
#     total += num
# num_list.sort()     #排序
# print("最小值:",num_list[0])  #输出最小值（因为排序过了，所以第一个是最小的）
# print("最大值:",num_list[-1])  #输出最大值
# print("总数:",total)    #输出总数
# print("平均数:",total/10) #输出平均值
# print(min(num_list) + max(num_list))    #最大值max()，最小值min()
# print("平均数2:",sum(num_list)/len(num_list))   #sum()求和;len()长度


# #练习15：
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# num_list = []   #创建一个新列表用于存储数据

# #1.通过解包（将列表这一类容器解开成一个个独立的元素）【*列表】操作简化合并步骤
# #组包：将多个值合并到一个容器
# num_list3 = [*num_list1,*num_list2]
# print(num_list3)

# #2.直接通过+进行列表合并
# num_list4 = num_list1 + num_list2
# print(num_list4)

# #3.循环遍历列表2的值然后添加到列表1中，以实现两列表相加
# for i in num_list2:
#     num_list1.append(i)
# print(num_list1)


# #将合并后的列表中的元素添加到新列表中，如有重复则不添加
# for i in num_list1:
#     if i not in num_list:
#         num_list.append(i)
# print(num_list)


# #练习16：
# #1.1
# num_list1 = []
# for i in range(1,21):
#     num_list1.append(i ** 2)
# print(num_list1)
# #1.2 列表推导式1 ---> 按照一定规则快速生成一个列表 ---> 语法格式[要插入的值 for i in 序列/列表]
# num_list1_1 = [i ** 2 for i in range(1,21)]
# print(num_list1_1)

# num_list2 = [19,23,54,64,87,20,109,232,123,43,26,55,72]
# #2.1
# num_list3 = []
# for i in num_list2:
#     if i % 2 ==0:
#         num_list3.append(i ** 2)
# print(num_list3)
# #2.2 列表推导式2 ---> 语法格式[要插入的值 for i in 序列/列表 if 条件]
# num_list3_1 = [i ** 2 for i in num_list2 if i % 2 == 0]
# print(num_list3_1)

# #练习17:
# list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
# list2 = ['X','Z','T','Y','D','E','F','G']
# list3 = ['W','A','S','D']

# new_list = [*list1,*list2,*list3]   #合并列表
# list = []
# for i in new_list:      #去重
#     if i not in list:
#         list.append(i)
# list.sort()
# print(list)

# #练习18:
# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# new_list = [i ** 2 for i in list1 if i % 3 == 0 or i % 5 == 0]
# print(new_list)

# #练习19:
# list1 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
# new_list = [i for i in list1 if i > 0]
# print(new_list)
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #字符串常用方法
# s = "Hello-Python-Hello-World"
# #find()     查找指定字符串第一次出现的索引
# index = s.find("-")
# print(index)    #5
# #count()    统计子字符串在指定字符串中出现的次数
# c = s.count("o")
# print(c)        #4
# #upper()    将字符串转为大写
# su = s.upper()
# print(su)       #HELLO-PYTHON-HELLO-WORLD
# #lower()    将字符串转为小写
# sl = s.lower()
# print(sl)       #hello-python-hello-world
# #split()    将字符串按指定的字符串切割
# slist = s.split("-")
# print(slist)    #['Hello', 'Python', 'Hello', 'World']
# print(type(slist))#输出为列表类型   <class 'list'>
# #replace()  将字符串中指定子字符串替换为新内容
# sr = s.replace("-","_")
# print(sr)       #Hello_Python_Hello_World
# #startswith()/endswith()    判断字符串是否以指定的字符串开头或结尾，返回bool值
# print(s.startswith("Hello"))    #True
# print(s.endswith("Python"))     #False
# #strip()    去除字符串两端的空格（括号里面空着）或相同字符
# s1 = "aaaHello-Python-Hello-Worldaa"
# ss = s1.strip("a")
# print(ss)   #Hello-Python-Hello-World
# #原始字符串是不变的，因为字符串是不可变的，以上诸多方法只是生成了新的字符串并储存
# print(s)    #Hello-Python-Hello-World


# #练习20:
# # 1.1
# mail = input("请输入邮箱地址：")
# num_1 = mail.count("@")
# num_2 = mail.count(".")
# if num_1 == 1 and num_2 >= 1:
#     print("sign Right!")
# else:
#     print("Wrong!")

# # 1.2   通过in运算符判断--->存在则返回True，不存在返回False
# mail = input("请输入邮箱地址：")
# if mail.count("@") == 1 and "." in mail:
#     print("sign Right!")
# else:
#     print("Wrong!")


# #练习21:
# s = input("输入字符判断是否回文：")
# print(f"{s}：是回文" if s == s[::-1] else f"{s}：不是回文")   #切片步长设为-1以实现翻转

# #练习22:
# str_list = []
# for i in range(1,11):
#     s = input(f"请输入第{i}个字符串：")
#     s_1 = s[::-1]    #翻转
#     str_list.append(s_1.upper())    #大写并添加到列表

# print(str_list)
# for i in str_list:  #遍历输出
#     print(i)
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #由于列表（特点：元素可重复，有序，可以修改）如果要记录一些信息且这些信息不可被修改则可用元组（tuple）
# #元组（可以重复，有序，不可修改）一旦被定义只可以被查询不可以被修改
# #元组tuple定义
# t1 = (80,95,78,50,76,80,85,20)
# print(type(t1))     #<class 'tuple'>
# print(t1)
# #索引访问
# print(t1[1])
# print(t1[-1])
# #切片
# print(t1[0:5:1])
# print(t1[::-1])     #切片反向
# #count()    统计元素的个数
# print(t1.count(80)) #2
# #index()    获取元素的索引（第一个元素）
# print(t1.index(80)) #0
# #如果要定义单元数元组则需在元素后加逗号
# t2 = (100)
# t3 = (100,)
# print(type(t2))     #<class 'int'>
# print(type(t3))     #<class 'tuple'>

# #组包（Packing）:将多个值合并到一个容器（元组，列表）中。
# #解包（Unpacking）：将容器（元组，列表）解开成独立元素，分别赋值给多个变量
# #组包
# t1 = (5,7,9,10,2,23,12)
# t2 = 5,7,9,10,2,23,12   #不加外围的括号也可以
# print(t1)   #(5, 7, 9, 10, 2, 23, 12)
# print(t2)   #(5, 7, 9, 10, 2, 23, 12)
# #解包
# #基础解包
# a,b,c,d,e,f,g = t1  #将元组里的元素赋值到7个变量中
# print(a,b,c,d,e,f,g)
# #扩展解包（*表示收集剩余的所有元素，封装成一个列表）
# first,second,*other,last = t1
# print(first,second) #5 7
# print(other)        #[9, 10, 2, 23]
# print(type(other))  #<class 'list'>
# print(last)         #12

# #练习23:
# a = 10
# b = 20
# # t1 = (b,a)  #组包
# # a,b = t1    #解包
# a,b = b,a   #合并二者
# print(a,b)

# a1 = 100
# b1 = 200
# c1 = 300
# # t2 = (c1,a1,b1)
# # a1,b1,c1 = t2
# a1,b1,c1 = c1,a1,b1
# print(a1,b1,c1)

# #练习24:
# students = (
#     ("s001","方源",85,92,78),
#     ("s002","方正",92,88,95),
#     ("s003","白凝冰",78,85,82),
#     ("s004","黑楼兰",88,79,91),
#     ("s005","吴帅",95,96,89),
#     ("s006","气海",76,82,77),
#     ("s007","气绝",89,91,94),
#     ("s008","紫薇",75,69,82),
#     ("s009","龙公",86,89,98),
#     ("s010","楚度",66,59,72),
# )
# #1.1
# #计算每人总分，平均分
# zongfen = []
# yu = []
# shu = []
# ying = []
# for i in students:
#     zong = i[-1] + i[-2] + i[-3]    #计算总分
#     zongfen.append(zong)    #把总分添加到列表中
#     yu.append(i[-3])
#     shu.append(i[-2])
#     ying.append(i[-1])
# print("所有人总分为：",zongfen)  #输出所有人总分    所有人总分为： [255, 275, 245, 258, 280, 235, 274, 226, 273, 197]
# print("语文平均分为：",sum(yu)/10)   #输出语文平均分    语文平均分为： 83.0
# print("数学平均分为：",sum(shu)/10)   #输出数学平均分   数学平均分为： 83.0
# print("英语平均分为：",sum(ying)/10)   #输出英语平均分  英语平均分为： 85.8

# print(f"语文最高分为：{max(yu)}")   #语文最高分为：95
# print(f"数学最高分为：{max(shu)}")  #数学最高分为：96
# print(f"英语最高分为：{max(ying)}") #英语最高分为：98

# #找到平均分大于90的学生
# youxiu = []
# for i in zongfen:
#     if i > 270:
#         youxiu.append(students[zongfen.index(i)][1])
# print("优秀的学生有：",youxiu)  #优秀的学生有： ['古月方正', '吴帅', '气绝魔仙', '龙公']

# #1.2
# print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
# #1.2.1
# for i in students:
#     total = i[-1] + i[-2] + i[-3]
#     avg = total/3
#     print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{total}\t{avg:.1f}")#浮点数要保留n位小数时，可以在变量后加“:.nf”
# #1.2.2  通过元组的解包
# for id,name,chinese,math,english in students:   #相当于解包了
#     total = chinese + math + english
#     avg = total / 3
#     print(f"{id}\t{name}\t{chinese}\t{math}\t{english}\t{total}\t{avg:.1f}")#浮点数要保留n位小数时，可以在变量后加“:.nf”

# chinese_scores = [i[2] for i in students]   #将语文成绩封装成一个列表
# math_scores = [i[3] for i in students]
# english_scores = [i[4] for i in students]
# print(f"语文平均分：{sum(chinese_scores)/10}；最高分：{max(chinese_scores)}；最低分：{min(chinese_scores)}")
# print(f"语文平均分：{sum(math_scores)/10}；最高分：{max(math_scores)}；最低分：{min(math_scores)}")
# print(f"语文平均分：{sum(english_scores)/10}；最高分：{max(english_scores)}；最低分：{min(english_scores)}")

# print("优秀学生（平均分>90）名单如下：")
# for id,name,chinese,math,english in students:   #用解包的形式多数据时更方便区分
#     total = chinese + math + english
#     avg = total / 3
#     if avg > 90:    #优秀学生
#         print(f"学号：{id}，姓名：{name}，平均分：{avg:.1f}")
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #集合set:是一种无序的(数据没有索引)，不可重复的，可修改的数据容器。
# #定义集合
# s1 = {0,5,4,32,2,7,5,4}
# print(s1)           #{0, 32, 2, 4, 5, 7} 
# print(type(s1))     #<class 'set'> 
# #定义空集合：（不可用{}直接定义，否则是字典）
# s2 = set()
# s3 = {}
# print(type(s2))     #<class 'set'>
# print(s2)           #set()
# print(type(s3))     #<class 'dict'>

# #方法
# s1 = {"a","b","c","d","e"}
# print(s1)   #{'e', 'd', 'c', 'b', 'a'}  反映了集合的无序性
# #add()添加元素到集合中
# s1.add("f")
# print(s1)   #{'f', 'e', 'd', 'c', 'b', 'a'}
# #remove()移除指定的元素
# s1.remove("a")
# print(s1)   #{'f', 'e', 'd', 'c', 'b'}
# #pop()随机删除集合中的元素并返回
# pop = s1.pop()   #返回移除的值
# print(pop)  #f
# print(s1)   #{'e', 'd', 'c', 'b'}
# #clear()清空集合
# s1.clear()
# print(s1)   #set()
# #difference()求两集合的差集（包含在第一个集合中但不包含在第二个集合中）
# s2 = {1,2,3,4,5,6}
# s3 = {4,5,6,7,8,9}
# print(s2.difference(s3))    #{1, 2, 3}
# #通过运算符-求差集：
# print(s2 - s3)              #{1, 2, 3}
# #union()求两集合的并集
# print(s2.union(s3))         #{1, 2, 3, 4, 5, 6, 7, 8, 9}
# #通过运算符|求并集：
# print(s2|s3)                #{1, 2, 3, 4, 5, 6, 7, 8, 9}
# #intersection()求两集合的交集
# print(s2.intersection(s3))  #{4, 5, 6}
# #通过运算符&求交集：
# print(s2 & s3)  #{4, 5, 6}

# #集合推导式 ---> 快速构建一个集合   语法：{要往集合中添加的数据 for s in set1 if 条件}
# s4 = {s for s in s2 if s not in s3}  #s2与s3的差集
# print(s4)       #{1, 2, 3}

# #练习25:
# #选足球课：
# soccer_set = {"王林","曾牛","徐立国","遁天","天运子","韩立","历飞雨","乌丑","紫灵"}
# #选篮球课：
# basketball_set = {"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","历飞雨","云露"}
# #选法语课：
# french_set = {"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","历飞雨","韩立","曾牛"}
# #选艺术课：
# art_set = {"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

# print("同时选择法语和艺术的学生有：",french_set.intersection(art_set))  #同时选择法语和艺术的学生有： {'虎咆', '韩立', '姜老道', '天运子'}
# s1 = soccer_set & basketball_set & french_set & art_set
# print("同时选择四门课程的学生有：",s1) #同时选择四门课程的学生有： {'韩立', '天运子'}
# print("选择足球但未选篮球的学生有：",soccer_set.difference(basketball_set)) #选择足球但未选篮球的学生有： {'徐立国', '遁天', '紫灵', '乌丑'}
# #将集合解包成元素放入列表中
# student_list = [*soccer_set, *basketball_set, *french_set, *art_set]
# #合并集合，利用集合的去重性质去除重复的元素，拿到学生名单
# student_set = soccer_set.union(basketball_set).union(french_set).union(art_set)
# #判断某个学生的名字在列表中出现了几次，就是选了几门课
# for i in student_set:
#     num = student_list.count(i)     
#     print(f"{i}\t选了{num}门课程")
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #字典：使用键值对(key:value)来储存数据，每一个键都对应一个值，可通过键(key)快速找到对应值(value)
# #特点：键值对(key:value)存储，键(key)不能重复(如果重复后面的值会覆盖前面的值)，可修改。
# #其中value可以是任何类型数据，而key不能为可变类型（如：不为列表list，集合set，字典dict）
# #定义字典
# dict1 = {"A":670, "B":608, "C":580, "D":688,}
# print(dict1)        #{'A': 670, 'B': 608, 'C': 580, 'D': 688} 
# print(type(dict1))  #<class 'dict'>
# #访问
# print(dict1["A"])   #670
# dict1["A"] = 688
# print(dict1["A"])   #688

# #方法
# dict1 = {"a":100, "b":110, "c":120}
# #键值对的个数:
# print(len(dict1))       #3
# #添加
# dict1["d"] = 130        #往指定字典中添加键值对
# print(dict1)            #{'a': 100, 'b': 110, 'c': 120, 'd': 130}
# #删除
# print(dict1.pop("d"))   #130    删除字典中指定的key值，并返回其value
# del dict1["a"]          #删除字典中指定键值对
# print(dict1)            #{'b': 110, 'c': 120}
# #修改
# dict1["b"] = 140
# print(dict1)            #{'b': 140, 'c': 120}
# #查询
# print(dict1.get("b"))   #140    根据key获取value
# print(dict1.keys())     #dict_keys(['b', 'c'])  获取所有的key
# print(dict1.values())   #dict_values([140, 120])  获取所有的value
# print(dict1.items())    #dict_items([('b', 140), ('c', 120)])  获取所有的kry-value键值对
# #遍历
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")
# for key,value in dict1.items():
#     print(f"{key}:{value}")


# #练习26：
# import time #加入时间模块
# import ast  #将字符串解析成抽象语法树模块（相当于把字符串解析成python语句，并分析结构）\
# #判断一下有无文档   用try-except捕捉错误:因为如果没有文档直接运行代码会报FileNotFoundError错误
# try:
#     #打开储存文档，读取其中储存的文件
#     with open("./shopping(练习26).txt", "r", encoding = "UTF-8") as f:
#         #新建字典用于储存商品信息
#         dict_shopping = ast.literal_eval(f.read())
#         #ast.literal_eval()解析字符串解析成的语句，如果在白名单内即可执行
#         #不用eval()是因为该语句是无条件执行解析的语句，不进行检测可能执行恶意代码
# except FileNotFoundError:   #出错了就直接新建一个字典用于储存信息
#     dict_shopping = {}

# #循环重复交互菜单
# while True:
#     #交互菜单       按住alt+shift可以进行多行同时编辑
#     num = input("""
#     ########## 购物车系统 ##########
#     #         1.添加购物车         #
#     #         2.修改购物车         #
#     #         3.删除购物车         #
#     #         4.查询购物车         #
#     #         5.退出购物车         #
#     ################################
#     请选择要执行的操作(1-5)：
#     """)
#     match num:      #分情况讨论的语句
#         case "1":   #添加
#             name = input("请输入商品名称：")
#             if name in dict_shopping.keys():
#                 print("商品已存在！")
#                 time.sleep(1)   #等待1秒
#             else:
#                 dict_shopping[name] = [input("请输入商品价格："),input("请输入商品数量：")]
#                 print("已添加至购物车！")
#                 time.sleep(1)   #等待1秒                       
#         case "2":    #修改
#             name = input("请输入要修改的商品名称：")
#             if name in dict_shopping.keys():
#                 dict_shopping[name] = [input("请输入要修改的商品价格："),input("请输入要修改的商品数量：")]
#                 print(f"已修改{name}！")
#                 time.sleep(1)   #等待1秒
#             else:
#                 print("未找到该商品！")
#                 time.sleep(1)   #等待1秒
#         case "3":    #删除
#             name = input("请输入要删除的商品名称：")
#             if name in dict_shopping.keys():
#                 del dict_shopping[name]
#                 print(f"已删除{name}！")
#                 time.sleep(1)   #等待1秒
#             else:
#                 print("未找到该商品！")
#                 time.sleep(1)   #等待1秒
#         case "4":    #查询
#             for name,[value,num] in dict_shopping.items():
#                 print(f"商品名称：{name}，商品价格：{value}，商品数量：{num}。")
#                 time.sleep(1)   #等待1秒
#         case "5":    #退出
#             print("欢迎下次使用！")
#             time.sleep(1)   #等待1秒
#             break
#         case _:   #表示其他情况
#             print("wrong！请输入正确的编号！")
#             time.sleep(1)   #等待1秒        
# #再次打开储存文档
# with open("./shopping(练习26).txt", "w", encoding = "UTF-8") as f:
#     #将商品信息储存到文档中
#     f.write(str(dict_shopping))
# print("已储存至文档shopping！")

"""     数据容器总结与对比
特性        字符串(str)   列表(list)   元组(tuple)   集合(set)   字典(dict)
有序性         有序          有序         有序        无序          有序
重复元素       允许          允许         允许       不允许       key不允许
可变性        不可变         可变         不可变      可变          可变
索引访问       支持          支持          支持       不支持        不支持
切片操作       支持          支持          支持       不支持        不支持
使用场景     文本处理    有序可重复集合  固定数据记录  去重数据集合    键值对
"""

# #练习27:
# import ast      #将字符串解析成抽象语法树模块（相当于把字符串解析成python语句，并分析结构）
# #判断一下有无文档   用try-except捕捉错误:因为如果没有文档直接运行代码会报FileNotFoundError错误
# try:
#     #打开储存的文件
#     with open("./students(练习27).txt", "r", encoding = "UTF-8") as f:
#         #定义字典用于储存学生信息   {"name":[chinese,math,english]}
#         dict_students = ast.literal_eval(f.read())
# except FileNotFoundError:   #如果没有文档
#     dict_students = {}      #新建一个空字典用于储存学生数据

# while True:
#     #菜单
#     print("""
#     # # # # # # # # # # # # # # # # # # # # # # # # # # #【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     # 1.添加学生信息   2.修改学生信息   3.删除学生信息   4.查询学生信息   5.列出所有学生   6.统计班级成绩   7.退出系统  #
#     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     """)
#     num = input("请输入需要执行的操作(1-7):")
#     match num:
#         case "1":   #添加
#             name = input("请输入要录入学生姓名:")
#             if name in dict_students.keys():
#                 print("该学生已存在!!!")
#             else:
#                 try:    #保证用户输入的成绩是浮点数
#                     dict_students[name] = [float(input("请输入语文成绩:")), float(input("请输入数学成绩:")), float(input("请输入英语成绩:"))]
#                     print(f"添加学生【{name}】成功!")
#                 except ValueError:
#                     print("成绩只能是数字!")
#         case "2":   #修改
#             name = input("请输入要修改的学生姓名:")
#             if name in dict_students.keys():    #如果学生已在字典内
#                 try:    #保证用户输入的成绩是浮点数
#                     dict_students[name] = [float(input("请输入修改后的语文成绩:")), float(input("请输入修改后的数学成绩:")), float(input("请输入修改后的英语成绩:"))]
#                     print("修改成功!")
#                 except ValueError:
#                     print("成绩只能是数字!")
#             else:
#                 print("未找到该学生!")
#         case "3":   #删除
#             name = input("请输入要删除的学生姓名:")
#             if name in dict_students.keys():    #如果学生已在字典内
#                 dict_students.pop(name)
#                 print(f"学生【{name}】已被删除!")
#             else:
#                 print("未找到该学生!")
#         case "4":   #查询
#             name = input("请输入要查询的学生姓名:")
#             if name in dict_students.keys():    #如果学生已在字典内
#                 #dict_students[name]是列表结构,可以按索引读取其中元素,0号为语文,1号为数学,2号为英语
#                 print(f"学生【{name}】成绩如下:语文({dict_students[name][0]}), 数学({dict_students[name][1]}), 英语({dict_students[name][2]})")
#             else:
#                 print("未找到该学生!")
#         case "5":   #列出
#             print("全部学生成绩如下:")
#             print(f"{'姓名':<10}{'语文':<10}{'数学':<10}{'英语':<10}")
#             for name,[chinese,math,english] in dict_students.items():
#                 print(f"{name:<10}{chinese:<10}{math:<10}{english:<10}")
#         case "6":   #统计
#             if not dict_students:   #如果还没有文档
#                 print("暂无学生数据，无法统计!")
#                 continue
#             #创建3个列表分别存放语数英成绩和学生名单
#             list_chinese = []
#             list_math = []
#             list_english = []
#             list_students = []
#             for name,[chinese,math,english] in dict_students.items():
#                 list_students.append(name)
#                 list_chinese.append(chinese)
#                 list_math.append(math)
#                 list_english.append(english)
#             print(f"""
#             语文:
#             最高分:{max(list_chinese)} 【{list_students[list_chinese.index(max(list_chinese))]}】
#             最低分:{min(list_chinese)} 【{list_students[list_chinese.index(min(list_chinese))]}】
#             平均分:{(sum(list_chinese) / len(list_chinese)):.2f}
#             """)
#             print(f"""
#             数学:
#             最高分:{max(list_math)} 【{list_students[list_math.index(max(list_math))]}】
#             最低分:{min(list_math)} 【{list_students[list_math.index(min(list_math))]}】
#             平均分:{(sum(list_math) / len(list_math)):.2f}
#             """)
#             print(f"""
#             英语:
#             最高分:{max(list_english)} 【{list_students[list_english.index(max(list_english))]}】
#             最低分:{min(list_english)} 【{list_students[list_english.index(min(list_english))]}】
#             平均分:{(sum(list_english) / len(list_english)):.2f}
#             """)
#         case "7":   #exit
#             print("欢迎再次使用,bye---")
#             break
#         case _:     #其他
#             print("请输入正确的编号!!!")
# #将结果写入文档
# with open("./students(练习27).txt", "w", encoding = "UTF-8") as f:
#     #将学生信息储存到文档中
#     f.write(str(dict_students))
# print("已储存至文档students!")
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
#函数
"""
def 函数名(参数1,参数2)     函数里定义的参数是形式参数,只在函数内使用(局部变量)
    函数体
    return 返回值

函数值(参数1,参数2)         调用的参数是实际参数

注:函数定义时不会执行,调用的时候才会执行.并且要先定义再调用
"""
# #定义函数
# def func(value):
#     if value == "参数":
#         print("调用成功！")
#     else:
#         print("发生未知错误！！！")
# #调用
# value = "参数"
# func(value)   #调用成功！
# func(111)     #发生未知错误！！！

# #计算圆的面积与周长
# def circle_area_len(r):
#     area = 3.14 * (r ** 2)
#     len = round(2 * 3.14 * r, 1)    #round(数字,保留位数)该函数用于四舍五入数字
#     return area,len
# #调用
# print(circle_area_len(10))      #(314.0, 62.8)
# area, len = circle_area_len(10) #解包
# print(area,len)                 #314.0 62.8

# #计算长方形的面积和周长     ----->多个返回值封装到元组(元组不可修改)中了
# def rectangle_area_len(l,w):
#     """
#     (这是说明文档,鼠标悬浮于函数上自动显示)
#     该函数用于根据长方形的长和宽计算长方形的面积和周长
#     :param l: 长方形的长
#     :param w: 长方形的宽
#     :return: 长方形的面积, 周长
#     """
#     return l * w, (l + w) * 2
# print(rectangle_area_len(5,4))  #(20, 18)
# print(type(rectangle_area_len(5,4)))    #<class 'tuple'>
# help(rectangle_area_len)# Help on function rectangle_area_len in module __main__:                                                                                                     
#                         # rectangle_area_len(l, w)
#                         #     (这是说明文档,鼠标悬浮于函数上自动显示)
#                         #     该函数用于根据长方形的长和宽计算长方形的面积和周长
#                         #     :param l: 长方形的长
#                         #     :param w: 长方形的宽
#                         #     :return: 长方形的面积, 周长

# #函数的嵌套调用
# def fuc1():
#     print("fuc1_befor")     #结果   栈结构，先进后出LIFO(Last In First Out)
#     fuc2()                  #fuc1_befor
#     print("fuc1_after")     #fuc2_befor
# def fuc2():                 #fuc3 
#     print("fuc2_befor")     #fuc2_after
#     fuc3()                  #fuc1_after
#     print("fuc2_after")
# def fuc3():
#     print("fuc3")

# fuc1()
# print("Over!")

# #练习28:
# def triangle_arae(l,h):
#     """
#     该函数根据三角形的底边长(l)和高(h)求三角形的面积
#     """
#     return l * h *0.5

# print(triangle_arae(3,2))   #3.0


# def vowel_num(fuc_str):
#     """
#     输出传入的字符串中元音字母的数量
#     """
#     #先转化为str格式改为大写
#     num = 0 #元音字母数量
#     str_upper = str(fuc_str).upper()
#     for i in str_upper:     #遍历字符串
#         if i in "AEIOU":    #如果有元音字母
#             num += 1
#     return num

# print(vowel_num("asdfGHjkli"))         #2


# def calc_score(score_list):
#     """
#     计算传入的班级学员的高考成绩列表中的最高分, 最低分, 平均分(保留一位小数)
#     :param score_list: 成绩列表
#     :return 最高分, 最低分, 平均分
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list) / len(score_list), 1)
#     return max_s, min_s, avg_s

# math_score = [100, 105, 120, 99]
# m_max, m_min, m_avg = calc_score(math_score)    #解包
# print(f"最高分:{m_max}, 最低分:{m_min}, 平均分:{m_avg}(保留一位小数)")  #最高分:120, 最低分:99, 平均分:106.0(保留一位小数)
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #global关键字:告诉python解释器,在函数中使用全局变量,使得可以在函数内部修改全局变量的值
# num = 100

# def fuc1():
#     num = 1000
#     print("num内部:", num)

# def fuc2():
#     global num  #用global声明全局变量时,要先声明,再使用
#     num = 200
#     print("num内部:", num)

# fuc1()                      #num内部: 1000
# print("num外部:", num)      #num外部: 100
# fuc2()                      #num内部: 200


# #传参方式     参数比较方便认出的用位置传参简单,不好认的用关键词传参
# def reg_stu(name,age,gender,city):
#     print(f"注册成功, 姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
#     return {"name":name, "age":age, "gender":gender, "city":city}
# #位置传参:
# reg_stu("张三", 18, "男", "北京")   #注册成功, 姓名:张三, 年龄:18, 性别:男, 城市:北京
# #关键词传参:
# reg_stu(name = "张三", age = 18, gender = "男", city = "北京")
# #混合传参:
# reg_stu("张三", 18, city = "北京", gender = "男")   #关键词传参要在位置传参之后

# #默认参数(缺省参数,用于在定义函数时为参数提供默认值,调用函数时,可以不传递有默认值的参数)
# def reg_stu1(name,age,gender,city="青岛"):
#     print(f"注册成功, 姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
#     return {"name":name, "age":age, "gender":gender, "city":city}

# stu = reg_stu1("李四", 24, "男")    #注册成功, 姓名:李四, 年龄:24, 性别:男, 城市:青岛
# print(stu)                          #{'name': '李四', 'age': 24, 'gender': '男', 'city': '青岛'}


# #不定长参数(可变参数)   用于函数定义或调用时参数个数不确定的场景
# #位置传参(*args)    args参数会把多个数据封装成一个元组,args是元组类型(注意不会封装关键字参数),可以使用元组的方法
# def fuc1(*args):    #args只是约定俗成的名字,可以是任何变量名(如*data)
#     """
#     使用位置传参传递不定长参数,计算传入数字的最大值,最小值和平均值(结果保留1位小数),并输出args是的类型
#     """
#     min_ = min(args)
#     max_ = max(args)
#     avg_ = round(sum(args) / len(args), 1)
#     return type(args), max_, min_, avg_
# print(fuc1(10,20,30,40,50,60))  #(<class 'tuple'>, 60, 10, 35.0)
#关键字传递(**kwargs)   关键字是以键值对的方式传递参数的,kwargs参数会把多个数据封装成一个字典,kwargs是字典类型
# def fuc2(*args, **kwargs):
#     """
#     计算传入的数据的最小值,最大值,平均值.根据传入的保留小数位数(round),和是否打印(print)形式参数类型
#     """
#     min_ = min(args)
#     max_ = max(args)
#     avg_ = sum(args) / len(args)
#     if kwargs.get("round") is not None:
#         avg_ = round(avg_, kwargs.get("round")) #如果指定保留几位就保留几位
#     else:
#         avg_ = round(avg_, 2)      #默认保留两位
#     if kwargs.get("print"):        #判断是否打印类型
#         print(type(args), type(kwargs))
#     return max_, min_, avg_
# print(fuc2(14, 28, 35, round = 5, print = True))    #<class 'tuple'> <class 'dict'>
# print(fuc2(14, 28, 35)) #(35, 14, 25.67)             #(35, 14, 25.66667)
# #*args适用于处理数量不确定的数据
# #**kwargs适用于处理数量不确定的选项(函数的配置参数,用来定义函数的行为)

# def add(x, y):
#     """
#     使传入的两数字相加
#     """
#     return x + y
# def subtract(x, y):
#     """
#     使传入的两数字相减
#     """
#     return x - y
# def multiply(x, y):
#     """
#     使传入的两数字相乘
#     """
#     return x * y
# def divide(x, y):
#     """
#     使传入的两数字相除
#     """
#     return x / y

# def cacl(x, y, oper):
#     """
#     计算x,y是传入的数字,oper是计算方法(传入函数)
#     """
#     return oper(x, y)

# print(cacl(10, 5, divide))      #2.0 
# print(cacl(78, 18, subtract))   #60

# #匿名函数   只适用于简单函数的编写(适用于函数逻辑简单,并且只在一个地方使用的时候通常作为高阶函数的参数使用)
# #匿名函数:lambda(关键字) num1,num2(函数参数) : num1+num2(返回值表达式)
# add = lambda x,y : x + y
# print(add(1, 2))    #3
# #匿名函数可以直接调用外边加括号
# print((lambda num1,num2:num1+num2)(1,5))    #6

# #练习29:
# data_list = ["C++", "C", "Python", "C#", "PHP", "Java", "Go", "JavaScript", "Rust"]
# print(data_list)    #['C++', 'C', 'Python', 'C#', 'PHP', 'Java', 'Go', 'JavaScript', 'Rust']
# data_list.sort()    #sort()方法列表的排序方法   sort(*,key=None,reverse=False)----->key控制排序方式,默认按字母顺序排序;reverse是排序反转的意思
# #使其按照字母数量由小到大排序
# data_list.sort(key=lambda item : len(item))
# print(data_list)    #['C', 'C#', 'Go', 'C++', 'PHP', 'Java', 'Rust', 'Python', 'JavaScript']
# #使其按照字母数量由大到小排序
# data_list.sort(key=lambda item : len(item), reverse=True)
# print(data_list)    #['JavaScript', 'Python', 'Java', 'Rust', 'C++', 'PHP', 'C#', 'Go', 'C']

# #练习30:
# def N_jiecheng(num):
#     """
#     计算传入参数的阶乘
#     """
#     # zong = 1
#     # for i in range(1, num+1):
#     #     zong *= i
#     # return zong
#     if num == 1:
#         return 1
#     else:
#         return num * N_jiecheng(num - 1)    #可以自我递归调用

# print(N_jiecheng(5))    #120

# #练习31:
# #31.1
# #储存一批商品用列表套字典的形式
# """
# [{"name":商品名1, "price":价格1, "num":数量1, "freight":邮费1}
#  {"name":商品名2, "price":价格2, "num":数量2, "freight":邮费2}]
# 计算公式:商品数量*价格-优惠+运费
# """
# def cacl_shop(shop_list, q=0, jf=0):  #不填默认优惠券和积分为0
#     """
#     商品计算器,计算输入的一批商品的
#     总价计算公式: 商品总价 = 商品数量*价格 - 优惠 + 运费
#     """
#     jf_q = jf // 100        #积分抵扣金额
#     all_price = 0           #定义一下总价
#     for i in shop_list:     #遍历商品订单计算一个商品的金额加上邮费并相加得到总金额
#         all_price += i["price"] * i["num"] + i["freight"]

#     if all_price > 5000:    #如果商品总额大于5000,可用优惠
#         if q >= all_price:  #如果优惠券金额大于等于商品总价,优惠券不可用,只能用积分
#             if jf_q > 1 and jf_q < all_price:      #如果积分达到100以上,且抵扣金额不超过商品总价
#                 last_price = all_price - jf_q
#             elif jf_q > 1 and jf_q >= all_price:   #如果积分达到100以上,且抵扣金额超过商品总价
#                 last_price = 0  #全额抵扣
#             else:   #如果积分未达到100以上,无法使用积分
#                 last_price = all_price
#         else:               #如果优惠券金额小于商品总价,优惠券可用
#             last_price_1 = all_price - q           #用过优惠券后判断可否用积分
#             if jf_q > 1 and jf_q < last_price_1:   #如果积分达到100以上,且抵扣金额不超过券后总价
#                 last_price = last_price_1 - jf_q
#             elif jf_q > 1 and jf_q >= last_price_1:#如果积分达到100以上,且抵扣金额超过券后总价
#                 last_price = 0  #全额抵扣
#             else:   #如果积分未达到100以上,无法使用积分
#                 last_price = last_price_1
#     else:           #如果商品总额小于等于5000,不可用优惠
#         last_price = all_price
#     return last_price
# #调用
# shop_list = [{"name":"手机", "price":2000, "num":1, "freight":100},
#              {"name":"电脑", "price":5000, "num":1, "freight":100},
#              {"name":"平板", "price":1000, "num":1, "freight":100}]
# print(cacl_shop(shop_list,1000,10000))  #7200 = (2000*1 + 5000*1 + 1000*1) + 300 - 1000 - 10000/100
# #31.2
# def cacl_order_cost(*args:tuple[str, float, int], q=0, jf=0, freight=0):   #默认没有积分, 优惠券, 运费
#     """
#     :param args: 商品信息(商品名, 价格, 数量)--->("鼠标", 188, 1)用元组封装
#     :param q: 优惠券
#     :param jf: 积分
#     :param feright: 邮费
#     :return: 订单总金额
#     """
#     #总价计算公式: 商品总价 = 商品数量*价格 - 优惠 + 运费
#     #1. 计算总金额 = 商品数量 * 价格
#     total_price = [goods[1] * goods[2] for goods in args]   #列表推导式,将各个商品价格封装成一个列表
#     total_cost = sum(total_price)   #计算所有商品价格
#     #2. 扣减优惠券
#     if total_cost > 5000 and q <= total_cost:
#         total_cost -= q
#     #3. 扣减积分抵扣
#     if total_cost > 5000 and jf // 100 <= total_cost:
#         total_cost -= jf // 100
#     #4. 添加运费
#     total_cost += freight

#     return total_cost

# #调用
# print(cacl_order_cost(("手机", 2000, 1), ("电脑", 5000, 1), ("平板", 1500, 1))) #8500
# print(cacl_order_cost(("手机", 2000, 1), ("电脑", 5000, 1), ("平板", 1500, 1), q=1000, jf=10000, freight=300)) #7700
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# #类型注解(类似与C#中定义变量时的定义类型)   C#: int a = 111; /  Ptyhon: a: int = 111
# a: int = 111
# score: float = 18.5
# s: str = "Python"
# tr: bool = True
# no: None = None
# names: list[str | int] = ["a", "b", "c"]    #通过|可以再加一个类型,就不会报错了
# phones: set[str] = {"10086", "10000", "10085"}
# dic: dict[str, int] = {"count":2, "total":10}
# goods: tuple[str, int, int] = ("Hello", 100, 1)
# #作用是输入错误的类型会报错(如下),但是报错不代表不能跑
# names.append(11)
# print(names)
#如果不定义类型解释器会自动进行类型推断,无需声明.而定义类型则是强制规定类型
#添加类型注解只是提示并非强制,因为python是动态类型语言

# #函数注解
# def circle_area_len(r: int) -> float:    #参数返回值类型定义和变量一致,返回值类型定义为" -> 类型"
#     return round(3.14 * (r ** 2), 2)
# print(circle_area_len(2))
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
#模块(module) 一个.py文件就是一个模块,模块是python的基本组织单位,在模块中可以定义变量,函数,类,以及可执行的代码
"""
导入模块
import 模块名(一次导入多个模块用逗号隔开) 引入某个模块，调用的时候要用 模块名.方法()
import 模块名 as 别名                   引入某个模块，相当于给模块起个小名 别名.方法()
from 模块名 import 方法名               引入某个模块的某个方法，方法名()
from 模块名 import 方法名 as 别名        引入某个模块的某个方法， 相当于给某个模块的某个方法起个小名 别名()
from 模块名 import *                    引入某个模块的全部方法，调用的时候不用加模块名 方法名()

"""
# #导入模块
# import random as rd

# for i in range(1, 5):   #生成4个1-100的随机数
#     print(rd.randint(1,100))

# #导入模块中的某个功能
# from random import randint as rdt

# for i in range(1, 5):   #生成4个1-100的随机数
#     print(rdt(1,100))

# #导入模块中的所有
# from random import *

# for i in range(1, 5):   #生成4个1-100的随机数
#     print(randint(1,100))

# #导入my_module模块
# import my_module
# #使用模块中的功能
# print(my_module.PI)
# print(my_module.NAME)
# my_module.log_separator4()

# #导入my_module模块中的某个功能
# from my_module import log_separator4, PI, NAME  ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                 #正在作为模块使用
# #使用模块中的功能
# print(PI)
# print(NAME)
# log_separator4()

# from my_module import *
# print(PI)
# log_separator4()

#包(package): 本质就是一个文件夹,该文件中可以包含若干Python模块(.py文件),文件夹下还包含了一个__init__.py文件(用来描述当前包的信息)
#作用:模块文件较多的时候,用来管理多个模块(包的本质也是一个模块)
"""                                     调用方式
import 包名.模块名                       包名.模块名.方法名()
from 包名 import 模块名                  模块名.方法名()
from 包名 import *                       模块名.方法名()
from 包名.模块名 import 方法名            方法名()
from 包名.模块名 import *                 方法名()
"""
#导入包的模块
# import utils_package.my_module1
#调用
# utils_package.my_module1.log_separator1()
# print(utils_package.__author__)

#导入模块中的方法
#from utils_package.my_module1 import log_separator1,log_separator2   #相对路径导入
#绝对路径导入(切记绝对路径不能从和.venv同级的文件夹开始),包要么放在最外层用相对路径导入,要么放内层用绝对路径
from z_study.utils_package.my_module1 import log_separator1,log_separator2  
#调用
log_separator2()

# #注:如果要通过from 包名 import * 的方式导入包下面所有的模块,需要在__init__.py 文件中添加 __all__ = []
# from utils_package import * 
# #调用
# my_module1.log_separator1()
"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
以上均为面向过程学习
"""
