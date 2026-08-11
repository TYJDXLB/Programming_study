#描述包的信息
__version__ = "1.0.0"       #包的版本
__author__ = "黑马程序员"    #包的作者

#手动导入模块   如果不手动导入,下面的__all__指定的模块会报警告
#原因:由于Pylance对__all__的解析规则的限制,他不会扫描同目录下的模块,因此会报文件不存在警告
from.import my_module1
from.import my_module2

#指定包的导入方式
__all__ = ["my_module1", "my_module2"]
