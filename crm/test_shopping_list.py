import unittest     #引入测试的库
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
#python -m unittest 文件名  终端输入来调用测试