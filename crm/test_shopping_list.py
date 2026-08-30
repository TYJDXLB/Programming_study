import unittest     #引入测试的库  进行测试的时候，为将测试代码和正常代码分开，因此创建一个以test_开头的文件，并引入unittest测试库
from shopping_list import ShoppingList  #加载要测试的脚本

class TestShoppingList(unittest.TestCase):  #定义一个用于测试的类，继承至unittest父类下的TestCase小类
    def setUp(self):    #创建一个通用的对象实例
        self.shopping_list = ShoppingList({"牙刷":5,"沐浴露":15,"电池":7})

    def test_get_item_count(self):
        # shopping_list = ShoppingList({"牙刷":5,"沐浴露":15,"电池":7})
        self.assertEqual(self.shopping_list.get_item_count(),3) #assertEqual方法可以比较两个参数的值是否一致
    
    def test_get_total_price(self):
        # shopping_list = ShoppingList({"牙刷":5,"沐浴露":15,"电池":7})
        self.assertEqual(self.shopping_list.get_total_price(),27)

#python -m unittest test_shopping_list
#python -m unittest 文件名  终端输入来调用测试(会检测所有继承unittest.TestCase的类，并测试所有以test_开头的方法)

# assert语句，assert后面跟上认为应该为true的表达式，如果表达式不为true则会出现断言错误：AssertionError。之后程序终止

'''
unittest.TestCase类常见的测试方法
assertEqual(A, B)     ==>  Assert A == B
assertTrue(A)         ==>  Assert A is True  最广泛本质上可以代替所有方法
assertIn(A, B)        ==>  Assert A in B
assertNotEqual(A, B)  ==>  Assert A != B
assertFalse(A)        ==>  Assert A is False
assertNotIn(A, B)     ==>  Assert A not in B
'''

