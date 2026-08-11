# #定义__all__表示from my_module import * 中可以调用的方法有哪些,没定义默认为全部
# __all__ = ["log_separator3", "log_separator4", "PI"]
#常量(不会发生变化的数据; 常数名称全部为大写)
PI = 3.14
NAME = "涛哥*黑马"

#函数
def log_separator1():
    print("_ " * 30)

def log_separator2():
    print("+ " * 30)

#__name__: python中的内置变量,表示的当前模块的名字
#如果直接运行当前模块,__name__的值为"__main__" ; 如果模块被导入时,__name__的值时模块名
# print(__name__) #__main__
#测试代码写在一个if语句中判断是否作为模块被调用
if __name__ == "__main__":  #如果直接运行
    log_separator1()
    print("测试中!!!")
    log_separator2()
# else:
#     log_separator3()
#     print("正在作为模块使用")