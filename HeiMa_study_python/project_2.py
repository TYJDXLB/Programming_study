"""
-------------------------------------------------------------------------------------------------------------------------------------------
以下为面向对象学习
"""
# #定义类     类名的命名规则遵循大驼峰命名法,每个单词的首字母大写,单词之间没有分隔符 eg:UserAccount
# class Car:
#     pass
# #创建对象
# c1 = Car()
# #动态的为对象添加属性(不推荐)   由于pylance是静态检查工具,动态添加会报错,不影响输出.可关闭检查类型解决
# c1.brand = "BMW"
# c1.color = "red"
# c1.name = "X5"
# c1.price = 500000
# print(c1)           #<__main__.Car object at 0x0000011BCFE76900(内存地址)>
# print(c1.__dict__)  #{'brand': 'BMW', 'color': 'red', 'name': 'X5', 'price': 500000}   __dict__会把对象中的所有属性一字典的形式输出出来 


"""
class 类名:
    def __init__(self,参数列表): #self:方法的第一个参数,表示当前创建的实例对象
    self.属性名 = 参数值         #__init__:初始化方法,对象创建后自动调用,主要用于设置对象的初始化状态(设置对象属性)
    self.属性名 = 参数值
#创建对象
对象名 = 类名(参数列表)
"""
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型对象已经初始化完毕,对象属性已添加!!!")

# #创建对象
# c2 = Car("天依蓝", "BMW", "X5", 500000) #Car类型对象已经初始化完毕,对象属性已添加!!!   初始化的时候会自动调用__init__方法
# print(c2.__dict__)  #{'color': '天依蓝', 'brand': 'BMW', 'name': 'X5', 'price': 500000}



#python特殊方法(魔法方法)：以双下划线开头或结尾的方法，用于定义类的特殊行为.例如__init__
#魔法方法不需要手动调用,Python会在合适的时机自动调用
"""
__init__: 初始化方法
__str__: 字符串的表示方法
__eq__: 比较两个对象是否相等(equal)
__lt__,__le__,__gt__,__ge__: 支持比较两个对象的大小
(小于('l'ess 't'han), 小于等于('l'ess than or 'e'qual), 大于('g'reater 't'han), 大于等于('g'reater than or 'e'qual)) 
"""
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型对象已经初始化完毕,对象属性已添加!!!")
    
#     #魔法方法
#     def __str__(self):  #使用该方法时,在调用print时就会输出字符而不输出内存地址了
#         return f"{self.color} {self.brand} {self.name} {self.price}"
    
#     def __eq__(self, other):    #判断两对象是否相等的方法
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
    
#     def __lt__(self, other):    #比较两个对象的大小,这里用价格来进行比较
#         return self.price < other.price

# #测试
# c1 = Car("白色", "BYD", "汉", 180000)
# print(c1)

# c2 = Car("白色", "BYD", "汉", 180000)
# print(c1)

# print(c1 == c2)
# print(c1 < c2)


# #属性:   实例属性:属于每个具体对象的属性,每个对象都是独立的(各个对象特有的数据),不能定义在__init__中,通过"类名.属性"操作
#         #类属性:属于类本身的属性.所有实例共享的(所有对象共享的数据或配置),定义在__init__中,通过"实例对象.属性"操作
# #通过实例查找属性时,会先查找实例属性,当实例属性不存在时,再查找类属性
# class Car:
#     #类属性
#     wheel = 4       #轮胎数量
#     tax_rate = 0.1  #购置税税率

#     def __init__(self, c_color, c_brand, c_name, c_price):
#         #实例属性
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         self.wheel = 2  #如果实例属性中有类属性,先访问实例属性中的变量

#     def runnig(self):
#         print(f"{self.brand} {self.name} 正在行驶中......")

#     def total_cost(self, discount, rate=0.1):
#         total_cost = self.price * discount + rate * self.price
#         return total_cost

# #测试
# c1 = Car("白色", "BYD", "汉", 180000)
# print(c1.price)
# print(c1.wheel)
# print(Car.wheel)

# # c2 = Car("白色", "BYD", "汉", 180000)
# # print(c1)

#练习:教务管理系统的开发
"""
要求:采用面向对象的编程思想,完成教务管理系统的开发.
教务管理系统可以管理在校学生的成绩信息,通过控制台菜单与用户实现交互,具体功能如下:
    1.添加学生信息: 根据输入的学生姓名,语文成绩,数学成绩,英语成绩,记录在系统当中
        1.1输入学生姓名,语文成绩,数学成绩,英语成绩
        1.2检查学生姓名是否存在,如果不存在,再添加(存在则不添加)
        1.3验证成绩范围
        1.4创建学生对象并添加到系统
    2.修改学生成绩: 根据输入的学生姓名,修改对应的学生成绩
        2.1输入要修改的成绩姓名
        2.2根据姓名找到该学生,显示该生当前成绩
        2.3输入新的语文,数学,英语成绩
        2.4更新学生成绩数据
    3.删除学生成绩: 根据输入的学生姓名,删除对应的学生成绩
    4.查询指定的学生成绩: 根据输入的学生姓名,查找对应的学生成绩,并输出
    5.展示全部学生成绩: 展示出系统中所有的学生成绩
"""
# #学生类
# class Students:
#     """
#     定义一个学生类储存学生信息:姓名,语文,数学,英语成绩
#     """
#     def __init__(self, name, chinese, math, english):
#         """
#         初始化实例的方法,用于添加学生信息
#         """
#         self.name = name
#         self.chinese = chinese
#         self.math = math
#         self.english = english
#         print(f"学生【{self.name}】信息已添加至系统!!!")

#     def __str__(self):
#         """
#         输出学生信息,且为字符串形式
#         """
#         return f"学生【{self.name}】| 语文: {self.chinese} | 数学: {self.math} | 英语: {self.english} | 总分: {self.chinese + self.math + self.english}"

#     def updata_score(self, chinese=None, math=None, english=None):
#         """
#         根据学生姓名修改成绩的方法
#         """
#         if chinese is not None:
#             self.chinese = chinese
#         if math is not None:
#             self.math = math
#         if english is not None:
#             self.english = english


# #教务管理系统类
# class EduManagement:
#     """
#     教务管理系统的类,用于储存学生信息
#     """
#     system_version = "1.0"
#     system_name = "教务管理系统"

#     def __init__(self):
#         self.student_list = []

#     #添加学生信息
#     def add_student(self):
#         name = input("请输入学生的姓名: ")
#         for s in self.student_list: #判断学生是否存在
#             if s.name == name:
#                 print("该学生已经存在,添加失败!!!")
#                 return  #直接返回不运行后续代码
#         chinese = int(input("请输入学生语文成绩: "))
#         math = int(input("请输入学生数学成绩: "))
#         english = int(input("请输入学生英语成绩: "))
#         #判断积分是否在0-100之间
#         if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#             stu = Students(name, chinese, math, english)    #创建一个学生实例
#             self.student_list.append(stu)   #将其加入到学生列表
#             print("学生信息添加成功!")
#         else:
#             print("各科成绩必须在0-100之间!!!")

#     #修改学生成绩
#     def updata_student(self):
#         name = input("请输入要修改的学生的姓名: ")
#         for s in self.student_list: #判断学生是否存在
#             if s.name == name:
#                 print(f"当前成绩: {s}")
#                 chinese = int(input("请输入学生修改后的语文成绩: "))
#                 math = int(input("请输入学生修改后的数学成绩: "))
#                 english = int(input("请输入学生修改后的英语成绩: "))
#                 #判断积分是否在0-100之间
#                 if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#                     s.updata_score(chinese, math, english)
#                     print("成绩修改成功!")
#                     print(f"修改后成绩为: {s}")
#                     return
#                 else:
#                     print("各科成绩必须在0-100之间!!!")
#                     return
#         print("未找到该学生,修改失败!!!")

#     #删除学生成绩
#     def delate_student(self):
#         name = input("请输入要删除的学生的姓名: ")
#         for s in self.student_list: #判断学生是否存在
#             if s.name == name:
#                 self.student_list.remove(s) #移除列表中的该学生
#                 print("学生信息删除成功!")
#                 return
#         print("未找到该学生,删除失败!!!")

#     #查询指定学生成绩
#     def query_student(self):
#         name = input("请输入要查询的学生的姓名: ")
#         for s in self.student_list: #判断学生是否存在
#             if s.name == name:
#                 print(f"学生信息: {s}")
#                 return
#         print("未找到该学生,查询失败!!!")


#     #展示全部学生成绩
#     def list_student(self):
#         if not self.student_list:   #如果系统中没有学生
#             print("系统中暂无学生信息!")
#             return
#         for s in self.student_list:
#             print(s)

#     #运行系统的方法
#     def run(self):
#         print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")
#         while True:
#             print()
#             print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
#             print("# 1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统 #")
#             print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
#             num = input("请选择所需要的操作(1-6):")
#             match num:
#                 case "1":   #添加
#                     self.add_student()
#                 case "2":   #修改
#                     self.updata_student()
#                 case "3":   #删除
#                     self.delate_student()
#                 case "4":   #查询指定
#                     self.query_student()
#                 case "5":   #查询所有
#                     self.list_student()
#                 case "6":   #退出
#                     print("欢迎下次使用!")
#                     break
#                 case _:
#                     print("请输入正确的编号!!!")




# #tests
# if __name__ == "__main__":
#     edu_management = EduManagement()    #新建一个管理系统的实例
#     edu_management.run()                #调用其中的方法

"""
异常捕捉:
try:
    可能出现异常的代码
expect [异常类型 as 变量名]
    出现异常时的预案
[finally:
    无论是否异常,都会执行的代码]
"""

# try:
#     print("=======================")
#     print(1/0)
#     print("========================")
# except NameError as e:  #拿到错误信息
#     print("ERROR,错误信息为:", e)
# except Exception as e:  #捕捉所有的异常
#     print("ERROR!")
# except:                 #也可以直接捕捉所有异常
#     print("ERROR!")
# finally:
#     print("运行结束!!!")