// Console.WriteLine("Hello, World!"); // 输出
// Console.ReadKey(); // ReadKey暂停程序，等待用户输入一个按键（可用作暂停程序）
// // 单行注释
// /* 多行注释 */
// /// 文档注释，用于给类，方法进行注释
// // 变量(先声明，在赋值，最后使用；使用小驼峰命名法命名)：
// int zhengShu = 10;
// float danShu = 10.1f; // 单精度小数，精确到后7位
// double shuangShu = 10.2; // 双精度小数，精确到后15位
// bool buer;
// string str = "字符串用双引号";
// char dan = '&'; // 单个字符，用单引号括住
// // 运算符号 +, -, *, /, %(取模，取余数), ++, --
// Console.WriteLine(10 / 3);
// Console.WriteLine(10f / 3); // 加上f可以带小数
// // ++i：先自增再参与运算；i++：先参与运算再自增
// int c = 10;
// int f = ++c;
// Console.WriteLine(f); // 11
// Console.WriteLine(c); // 11
// int d = 10;
// int g = d++;
// Console.WriteLine(g); // 10 先完成g=d之后d再自增的
// Console.WriteLine(d); // 11
// // 【i++先使用所以为1，然后自增因此i++执行完之后i为2。之后i++先自增为3，执行完之后i为3。故最终为：1+3+3=7】
// int i = 1;
// Console.WriteLine(i++ + ++i + i); // 7 = 1+3+3
// // 关系运算符：<, <=, >, >=, ==, !=
// // 逻辑运算符：&&, ||, !
// Console.WriteLine(5 < 3);
// // 占位符 {0}, {1}, {2}....
// string name = "yk";
// int age = 18;
// char gender = '男';
// Console.WriteLine("我的名字是{1}，年龄是{1}，性别是{2}", name, age, gender);
// // 输入
// string shuRu = Console.ReadLine();
// Console.WriteLine(shuRu);
// // 转义符：\   \n为换行，\t表示tab，\b表示将光标向前移动一格，遇到\n,\r停止，并从此位置输出后面的内容
// Console.WriteLine("123\b45"); // 1245
// Console.WriteLine("123\b\b45"); //145
// // 类型转换 
// // 隐式转换 同类型的数小的可以转换成大的 int-->float, int-->double
// int a = 1;
// float b;
// double c;
// b = a;
// c = a;
// // 显式转换[强制转换类型] 同类型的数小的可以转换成大的 int-->float, int-->double
// float fl = 11.45f;
// int xian = (int)fl;
// // convert转换 可以转换不同类型的变量
// string str = "11";
// int num = Convert.ToInt32(str);
// // 常量 声明完不可改变 用大写字母组成的单词加下划线构成
// const int CHANG_SHU = 10;

/* 将注释补充到下面C#文档中了！！！ */




