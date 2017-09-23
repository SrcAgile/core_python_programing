
### 3–1

标识符  为什么 Python 中不需要变量名和变量类型声明？

`答:python 是动态类型语言，在赋值时，根据"=" 右边动态确定变量类型，不需要特别的声明，在运行时，才会调用类型使用。变量在第一次被赋值时自动声明,。Python 语言中， 对象的类型和内存占用都是运行时确定的。尽管代码被编译成字节码，Python 仍然是一种解释型语言`

### 3–2

标识符 为什么 Python 中不需要声明函数类型？

`答:函数没有定义返回的数据类型。 Python不需要提定返回值的数据类型；甚至不需要指定是否有返回值。实际上，每个Python函数都返回一个值；如果函数执行过return语句，它将返回指定的值，否则将返回None（Python 的空值`

### 3–3

标识符 为什么应当避免在变量名的开始和和结尾使用双下划线？

`答:__xxxx__ 这样的变量类型在python中有特殊意义，表示 "系统定义名字"  ，这样的做的目的减少自定义变量覆盖系统定义变量，从而导致脚本运行出错`

### 3–4

语句 在 Python 中一行可以书写多个语句吗？
`答：可以，使用";“ 隔开即可`

### 3–5

语句 在 Python 中可以将一个语句分成多行书写吗？
`答：可以,使用”\“ 即可实现分多行书写`

### 3–6

变量赋值
(a)赋值语句 x, y, z = 1, 2, 3 会在 x、y、z 中分别赋什么值？
(b)执行 z, x, y = y, z, x 后，x、y、z 中分别含有什么值？

`答: x,y,z，分别是 1，2，3  在执行b）后 三值互换
x=3,y=2,z=1
`

### 3–7

标识符 下面哪些是 Python 合法的标识符？如果不是，请说明理由！在合法的标
识符中，哪些是关键字？
int32  40XL  $aving$  printf  print
_print  this  self  __name__ 0X40L
bool  true  big-daddy 2hot2touch type
thisIsn'tAVar thisIsAVar R_U_Ready Int  True
if  do  counter-1 access  -

答案
Python标识符字符串规则和其他大部分用C编写的高级语言相似：
第一个字符必须是字母或下划线“_”；剩下的字符可以是字母数字或下划线；大小写敏感。
int32、printf、_print、this、self、__name__、bool、true、type、thisIsAVar、R_U_Ready、Int、True、do、access是Python合法的标识符。
print、if、是Python合法的标识符且是关键字。

40XL、$aving$、0X40L、big-daddy、2hot2touch、thisIsn'tAVar、counter-1、-不是Python合法的标识符。

下面的问题涉及了 makeTextFile.py 和 readTextFile.py 脚本。

### 3–8

Python 代码。将脚本拷贝到您的文件系统中，然后修改它。可以添加注释，修改
提示符（‘>’太单调了）等等，修改这些代码，使它看上去更舒服。
`答：略`

### 3–9

移植 如果你在不同类型的计算机系统中分别安装有Python， 检查一下，
os.linesep 的值是否有不同。 记下操作系统的类型以及 linesep 的值。

`答:导入模板 import os `
```python
>>> import os
>>> print os.uname()
>>> ('Linux', 'meta', '4.4.0-93-generic', '#116-Ubuntu SMP Fri Aug 11 21:17:51 UTC 2017', 'x86_64')

>>> print os.linesep


>>>
```

### 3–10
异常 使用类似readTextFile.py 中异常处理的方法取代 readTextFile.py
makeTextFile.py 中 对 os.path.exists()的调用。反过来， 用os.path.exists() 取 代
readTextFile.py 中的异常处理方法。


### 3–11
字符串格式化 不再抑制 readTextFile.py 中 print 语句生成的 NEWLINE 字符，修改你的
代码，在显示一行之前删除每行末尾的空白。这样，你就可以移除 print 语句末尾的逗号了。
提示： 使用字符串对象的 strip()方法
`答:` [见git仓库](./3.11.py)

```
- 将逗号改为 .strip() ，此时读入的字串后面的换行符作为空白被舍弃，但是仍然输出print的换行符
- 即自动消除行尾\n,但是strip的用法不仅仅如此
```

### 3–12
合并源文件。将两段程序合并成一个，给它起一个你喜欢的名字，比方
readNwriteTextFiles.py。让用户自己选择是创建还是显示一个文本文件。

`答:` [见git仓库](./3.12.py)



### 3–13
添加新功能。将你上一个问题改造好的 readNwriteTextFiles.py 增加一个新功
能：允许用户编辑一个已经存在的文本文件。 你可以使用任何方式，无论是一次编辑一行，还
是一次编辑所有文本。需要提醒一下的是，一次编辑全部文本有一定难度，你可能需要借助 GUI
工具包或一个基于屏幕文本编辑的模块比如 curses模块。要允许用户保存他的修改（保存到
文件）或取消他的修改（不改变原始文件），并且要确保原始文件的安全性（不论程序是否正
常关闭）。


`答：` [见git仓库](./3.13.py)  -->使用了Tkinter  ,platform
