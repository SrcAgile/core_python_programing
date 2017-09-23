### 4–1

>Python 对象。与所有 Python 对象有关的三个属性是什么？请简单的描述一下。

`答：`

身份：每个对象有自己唯一一个身份标识，这个值可以用内存地址来表示。id（）函数获得

类型：决定了该对象可以保存什么样类型的值。用type（）来查看某个对象的类型

值：对象表示的数据项

### 4-2
> 类型。不可更改（immutable）指的是什么？Python 的哪些类型是可更改的（mutable），哪些不是？

`答：`

不可能改指的是Python的一个数据类型，从更新模型角度划分的，这个对象如果是不可更改，则它的值不可以改变

可更改：列表，字典

不可更改：字符串，元组，数字

### 4–3
> 类型。哪些 Python 类型是照顺序访问的，它们和映射类型的不同是什么？

`答：`

顺序访问：字符串，列表，元组

映射类型是容纳哈希键值对的集合

### 4–4
> type()。内建函数 type()做什么？type()返回的对象是什么？

`答：`

type（）是显示某对象的类型的函数。

返回的对象是叫 type 的对象

### 4–5
> str() 和 repr()。 内建函数 str()与 repr()之间的不同是什么？哪一个等价于反引号(`\`\``)运算符？

`答：`

str（）是让用户看的，repr（）是让程序维护者看的。repr()等价于反引号

### 4–6
> 对象相等。 您认为 type(a) == type(b)和 type(a) is type(b)之间的不同是什么？为什么会选择后者？函数 isinstance()与这有什么关系？

`答：`

前者是两者的对象值相等，后者是对象的类型相等，

后者在运行的时候少一次查询，所以更倾向于后者吧

isinstance()可以用来替代他们前两者


```python
>>>if type(b) is type(a):
```

可以用

```python
>>>if isinstance(a,(int,long,float,complex)):
```
来替代

### 4–7
> 内建函数 dir()。在第二章的几个练习中，我们用内建函数 dir()做了几个实验，它接受一个对象，然后给出相应的属性。请对 types 模块做相同的实验。记下您熟悉的类型，包括您对这些类型的认识，然后记下你还不熟悉的类型。在学习 Python 的过程中，你要逐步将“不熟悉”的类型变得“熟悉”起来。

`答：`

```python
>>>import types                #在2.7版本中，直接输入types会有错误
>>>types
 <module 'types' from 'C:\Python27\lib\types.pyc'>
>>>dir(types)
>>>['BooleanType', 'BufferType', 'BuiltinFunctionType', 'BuiltinMethodType', 'ClassType', 'CodeType', 'ComplexType', 'DictProxyType', 'DictType', 'DictionaryType', 'EllipsisType', 'FileType', 'FloatType', 'FrameType', 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'InstanceType', 'IntType', 'LambdaType', 'ListType', 'LongType', 'MemberDescriptorType', 'MethodType', 'ModuleType', 'NoneType', 'NotImplementedType', 'ObjectType', 'SliceType', 'StringType', 'StringTypes', 'TracebackType', 'TupleType', 'TypeType', 'UnboundMethodType', 'UnicodeType', 'XRangeType', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__']


```

### 4–8
> 列表和元组。列表和元组的相同点是什么？不同点是什么？

`答：`

两者都是容器存储模型，都是顺序访问模型。

不同是前者是可更改的后者不可更改。

### 4–9
> 练习，给定以下赋值：

a = 10
b = 10
c = 100
d = 100
e = 10.0
f = 10.0

请问下面各表达式的输出是什么？为什么？
(a) a is b
(b) c is d
(c) e is f

`答：`


```python
>>> a is b
True                        #小整型Python会缓存，默认指向同一个内存地址
>>> c is d
True                     
>>> e is f
False   
```
