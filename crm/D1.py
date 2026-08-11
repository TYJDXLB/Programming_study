# print("你好世界！")
# print('He said "Good!!"')   #外引号和内部的引号不要混用
# print("He said \"Let\'s go!\'") #可在引号前加斜杠表明前面只是单纯的引号
# print("Say \nHi!")  #\n表示换行
# print("""古月方源
# 古月方正
# 白凝冰
# 黑楼兰
# 太白云生""")

# 账号 = "156324"     #可用汉语进行变量命名不过不推荐
# 密码 = "123456"
# print(账号 + 密码 + "\npython不用定义变量类型\n可以用汉语做变量名\n不用结尾太爽了！！！")
# print(6-4/2*5)  # + - * / 乘方：**
# import math     #导入数学函数库
# a = math.log2(8)
# print(a)
"""
三引号可以用作多行注释
你看到了吗
直接注释掉了
选中按 Ctrl+/ 可快速注释（取消）
"""

# a = "string"[2] #相当于把2号给提出来了
# print(a)
# print(len(a))
# b = type(a)     #type函数可以判断变量类型
# print(b)
# #python交互模式：win+R输入cmd，在其中输入python，即可进入交互模式。

# user_age = input("请输入年龄：") #input 返回值为字符串
# print("年龄为：" + user_age)
# a_user_age = int(user_age)    #把类型改为整数
# print(a_user_age + 100)
#BMI = 体重 / （身高 ** 2）
# user_weight = float(input("请输入体重（KG）："))
# user_high = float(input("请输入身高（M）："))
# BMI = str(user_weight / (user_high ** 2))
# print("BMI为：" + BMI)

# if_happy = None
# a = input("你今天开心吗？Y/N:")
# if a=="Y":
#     if_happy = True
# elif a=="N":
#     if_happy = False

# if if_happy==True:
#     print("happy!!")
# else:
#     print("sad.")

"""
BMI = 体重 / （身高 ** 2）
偏瘦：BMI <= 18.5
正常：18.5 < BMI <= 25
偏胖：25 < BMI <= 30
肥胖：BMI >= 30
"""
# user_weight = float(input("请输入体重（KG）："))
# user_high = float(input("请输入身高（M）："))
# BMI = user_weight / (user_high ** 2)
# BMI_str = str(BMI)
# print("BMI为：" + BMI_str)
# if BMI <= 18.5:
#     print("偏瘦")
# elif 18.5 < BMI <= 25:
#     print("正常")
# elif 25 < BMI <= 30:
#     print("偏胖")
# else:
#     print("肥胖")

# a_list = ["古月方源"]
# a_list.append("白凝冰") #添加
# a_list.append(True)
# a_list.remove(a_list[2])    #移除
# print(a_list)
# print(len(a_list))
# a_list[0] = "古月方正"
# print(a_list)

# price = [799,239,998,1024]    #列表
# max_price = max(price)
# min_price = min(price)
# sorted_price = sorted(price)
# print(max_price)
# print(min_price)
# print(sorted_price)
# name_dict = {"暮光闪闪":"120001","苹果杰克":"120002","小蝶":"120003"}    #字典，储存键值对
# name_dict["瑞瑞"] = "120004"    #添加一个键值对
# print(name_dict)
# print("碧琪" in name_dict)  #判断某一键值是否在字典内
# del name_dict["苹果杰克"]   #删除一个键值对
# print(name_dict)
# print(name_dict.keys())     #返回所有键
# print(name_dict.values())   #返回所有值
# print(name_dict.items())    #返回所有键值对

# example_turple = ("UUZ","yaomeng")  #类似列表的不可变结构：元组；列表不可用作字典的键，而元组可以
# contact = {("嘉豪",20):"10086",("嘉豪",28):"10087",("嘉豪",42):"10088"}
# print(contact[("嘉豪",28)])

# 中V成员查询系统
# China_V = ["洛天依","乐正绫","言和","战音lorra","徵羽摩柯","墨清弦","乐正龙牙","心华","星尘"]
# 中V = {"洛天依":"能够敏锐地感受到他人感情，有点内向的少女。对过去曾经在人类世界创造了历史的传说中的VOCALOID™前辈们非常憧憬，也梦想着自己有朝一日能够成为用歌声为别人传递感动与幸福的歌姬，这样的她在某日突然获得了召唤，并且带着某个重要的任务，作为新的VOCALOID™来到了人类的世界。",
#       "乐正绫":"活力十足的16岁女高中生，乐器制造商和音乐大企业--乐正集团的大小姐。个性直来直去，不拘小节，一天有3/4的时间都在跑来跑去，那个精神头让男生也自叹不如。"}
# 中V["言和"] = "外表帅气、内心温柔的少女，声音和外形都比较中性，穿男装女装都没有压力。"
# 中V["战音lorra"] = "沉静寡言的16岁少女，带着某个神秘的使命从魔法次元来到人类世界。由于次元乱流的影响，出口错位，正好砸进了乐正绫家里。第一次来到人类世界的战音Lorra，对周围的一切还十分陌生。唯独在音乐上，有着超乎常人的感受和清冽的声线。"
# 中V["徵羽摩柯"] = "智商168的天才混血儿少年，平常总是一副人畜无害的笑容，但其实是个非常深度的宅，出没于各大宅论坛，MAD编辑达人，视频站 UP主，在部分人眼里是神一般的存在……"
# 中V["墨清弦"] = "17岁的高中生。学院中的超人气大姐姐，总是带着稳重感的冷美人，散发出神秘感和让人不容易靠近的气氛…………只是外表如此。实际上因为体质关系，平常的大部分时间处于轻微的低血压状态，因此反应往往会慢半拍。"
# 中V["乐正龙牙"] = "绫的哥哥，乐正集团的未来总裁，思路敏捷，受到期待的有为青年。性格洒脱，不拘小节，处事稳健却不失决断力，气场超强，但唯一的问题是，很讨厌麻烦的事情。怕麻烦的龙牙，唯有对妹妹绫有少许保护过度的倾向，当遇到跟绫相关的事情的时候，总会变得非常神经质…………俗称“妹控”。"
# 中V["心华"] = "心华是一个爱唱歌的16岁高中少女，有着蓝紫色的头发，瞳色为粉紫色。带着孩子气与些许大人般可爱气息的歌声和优美的台湾腔"
# 中V["星尘"] = "这是一个诞生于冰冷宇宙里的姑娘，宇宙的高次位面虽然充满了能量和秩序，却不曾拥有感情。在纯净的以太之海中诞生，以太构成了她的身躯。星尘因为感受到了我们的感情才苏醒。由于对爱这种感觉的迷惑和莫名的憧憬，才使得她来到了我们的世界。"
# print("===VOCALOID角色查询系统===")
# user_want = input("请输入要查询的角色：")
# if user_want in 中V:
#     print("您查询的角色" + user_want + "介绍如下：")
#     print(中V[user_want])
# else:
#     print("抱歉！未查询到该角色。\n当前共收录角色" + str(len(中V)) + "条。分别为以下角色：")
#     print(中V.keys())

# total = 0
# for i in range(1,101):
#     total += i  #等价于：total = total + i
# print(total)
# #已知循环次数的时候用for，一直循环用while
# total_2 = 0
# i = 0
# while i < 101:
#     total_2 = total_2 + i
#     i += 1
# print(total_2)

#对于用户所输入的数字求平均值，直到用户输入q结束。
# total = 0
# i = 0
# num = None
# while num != "q":
#     num = input()
#     if num != "q":
#         total += float(num)
#     else:
#         print(total/i)
#     i += 1

# gpa_dict = {"A":3.6,"B":2.8,"C":4.8}
# for name,gpa in gpa_dict.items():
#     print("{0}酱你好吖，你的GPA为：{1}".format(name,gpa))   #.format用来在引号内安插变量
# name = "haha"
# gpa = 4.99
# print(f"太强了{name}酱绩点高达：{gpa}")     #引号前加f可直接花括号内附变量名

# 函数封装,BMI检测函数
# print("===我是检测BMI的小工具===")
# def BMI_fuc(user_weight,user_high):
#     BMI = user_weight / (user_high ** 2)
#     BMI_ = None
#     if BMI <= 18.5:
#         BMI_ = "偏瘦"
#     elif 18.5 < BMI <= 25:
#         BMI_ = "正常"
#     elif 25 < BMI <= 30:
#         BMI_ = "偏胖"
#     else:
#         BMI_ = "肥胖"
#     print(f"您的BMI值为：{BMI};分类是：{BMI_}")
#     return BMI
# weight = float(input("您的身高为(M)："))
# high = float(input("您的体重为(KG)："))
# BMI_fuc(weight,high)

#引入模块
# import xxx                引入某个模块，调用的时候要用 模块名.方法
# from xx import xx         引入某个模块的某个方法，调用的时候不用加模块名
# from xx import*           引入某个模块的全部方法，调用的时候不用加模块名

# #定义类
# class CuteCat:
#     def __init__(self,cat_name,cat_age,cat_color):  #self参数不需要输入,定义对象
#         self.name = cat_name
#         self.age = cat_age
#         self.color = cat_color
    
#     def speak(self):
#         print("miao" * self.age)
    
#     def think(self,content):
#         print(f"小猫{self.name}在思考：{content}")

# cat1 = CuteCat("JOJO",2,"Yellow")    #创建对象
# print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
# cat1.speak()
# cat1.think("现在去抓沙发还是去撕纸箱")


#定义一个学生类，属性包含：姓名，学号，语数英成绩；能够设置学生的某科成绩；能打印出该学生所有科目成绩
# class Student:
#     def __init__(self,name,id):     #定义学生属性
#         self.name = name
#         self.id = id
#         self.grades = {"语文":0,"数学":0,"英语":0}
    
#     def set_grade(self,course,grade):   #设置各科成绩
#         if course in self.grades:
#             self.grades[course] = grade
    
#     def print_grade(self):
#         print(f"学生{self.name}（学号：{self.id}）的成绩为：")
#         for course in self.grades:
#             print(f"{course}:{self.grades[course]}分")

# Bob = Student("Bob",114514) #创建对象
# print(Bob.name)
# Bob.set_grade("数学",140)
# Bob.set_grade("语文",100)
# Bob.set_grade("英语",110)
# print(Bob.grades)
# Bob.print_grade()


#类继承练习：人力系统
# class Employee:     #员工父类
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
    
#     def print_info(self):
#         print(f"员工信息：\n姓名：{self.name}ID：{self.id}")
# #全职员工子类
# class FullTime(Employee):
#     def __init__(self, name, id, monthly_salary):
#         super().__init__(name, id)     #用super().来继承父类__init__里面的属性
#         self.monthly_salary = monthly_salary
    
#     def calculate_monthly_pay(self):
#         print(f"员工：{self.name}（ID：{self.id}）月薪为：{self.monthly_salary}")
#         return self.monthly_salary
# #兼职员工子类
# class PartTime(Employee):   
#     def __init__(self, name, id, daily_salary, work_days):
#         super().__init__(name, id)     #用super().来继承父类__init__里面的属性
#         self.daily_salary = daily_salary
#         self.work_days = work_days
    
#     def calculate_monthly_pay(self):
#         monthly_salary = self.daily_salary * self.work_days
#         print(f"员工：{self.name}（ID：{self.id}）月薪为：{monthly_salary}")
#         return monthly_salary

# quanzhi = FullTime("AA",10001,5000)
# jianzhi = PartTime("BB",10002,150,28)
# quanzhi.calculate_monthly_pay()
# jianzhi.calculate_monthly_pay()
# print(quanzhi.calculate_monthly_pay())

"""
open("文件地址(相对地址和绝对地址均可)","模式",encoding="UTF-8"（编码类型）)
模式：r是只读，w是只写(用w写的话，如果文件不存在可以创建它，如果原文件已存在则会清空原文件再写入)，a是附加，
    r+可读可写（，要先读后写不然会覆盖源文件），a+可读可写（不会覆盖原文件，但是不能直接读因为进入文本指针默认在尾部读不了，可以调用seek(0)从头读起）
"""
# f = open("data.txt","r",encoding="utf-8")  
# content = f.read()
# print(content)
# f.close()   #记得关闭文件

# with open("data.txt","r",encoding="utf-8") as f:    #用with语句无需关闭文件
#     print(f.readline()) #打印一行

#     content = f.read()
#     print(content)  #全部打印

#     print(f.readlines())    #返回一个列表，列表里的每个元素都是其中一行。
#     lines = f.readlines()    #可跟着for循环使用
#     for i in lines:
#         print(i)


# with open("./poem.txt","w",encoding="utf-8") as f:  #创建文件的时候相对地址要加上./
#     f.write("我欲乘风飞去，\n又恐琼楼玉宇，\n高处不胜寒，\n")

# with open("poem.txt","a+",encoding="utf-8") as f:   #打开文件的时候相对地址不要加上./
#     f.write("起舞弄清影，\n何似在人间。")
#     f.seek(0)   #回到首个字符
#     print(f.read())


#捕捉异常
# try:
#     user_weight = float(input("请输入您的体重(KG)："))
#     user_height = float(input("请输入您的身高(M)："))
#     user_BMI = user_weight / user_height ** 2
# except ValueError:  #数据错误
#     print("输入不为合理数字，请重新运行程序，并输入正确数字。")
# except ZeroDivisionError:   #除零错误
#     print("身高不可为零，请重新运行程序，并输入正确数字。")
# except: #不写错误类型的话，所有的错误均返回该结果
#     print("发生未知错误，请重新运行该程序")
# else:   #没发生任何错误时返回该结果
#     print("您的BMI值为：" + str(user_BMI))
# finally:    #无论是否发生错误均执行语句
#     print("程序结束运行。")


# #普通函数
# def calculator_square(num):
#     return num * num

# def calculator_cube(num):
#     return num * num * num

# def calculator_plus_10(num):
#     return num + 10

# #高阶函数就是普通函数作为其参数而存在
# def gaojie(num,calculator):
#     result = calculator(num)
#     print(f"""
#     |数字参数|{num}|
#     |计算结果|{result}|""")

# gaojie(2,calculator_square)  #普通函数后不要加（），否则就是函数的返回值
#匿名函数:lambda(关键字) num1,num2(函数参数) : num1+num2(返回值表达式)
# gaojie(2,lambda num:num*2)

#匿名函数可以直接调用外边加括号，
# print((lambda num1,num2:num1+num2)(1,5))