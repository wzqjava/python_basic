#! /usr/lib/local/python3.6
#coding=utf-8

#----  获取类型------
# age = "5"
# print(type(age))

#------\n是换行的意思-------
# name = '王志强'
# age = 30
# print("名字是%s,\n年龄是%s"%(name,age))

#-------------
# temp = raw_input('请输入文字:')
# print(temp)

#-----取整数
num = 9//4
# print(num) #2
temp = 9%2
# print(temp) #余1


#---逻辑运算符-----
a= 10;
b= 20;
temp = a and b;
# print(temp)

temp2 = a or b
# print(temp2)

#----if else------
'''
if (1==2):
    print("has ticket")
elif (2<1):
    print("has ticket  yeh")
else:
    print("has't ticket")
    '''

#----while------
'''

num  = 0
while num<5:
    print("i是%d"%num)
    num+=1

'''
#----计算1 到100的和-----
'''
num = 1
total = 0
while num<101:

    total+=num
    num += 1

print("toatal%d"%total)
'''


#----计算1 到100之间的偶数的 和-----
'''
i = 1
total = 0
while i<101:
    if i%2==0:
        total+=i
    i += 1

print("toatal:%d"%total)
'''


#----嵌套循环, 打印星星-----
'''
i = 1
while i<=5:
    j = 1
    while j<=i:
            print("* ")
            j+=1

    print("\n")
    i+=1

'''
#----for 循环-----
'''
name = "i m python teacher"
for x in name:
    print(x)
'''

#----break demo break:停止循环,只对最近的一层循环起作用-----
'''
name = "QiangGe"
for x in name:
    print("----")
    if(x == "G" ):
        print(x)
        break
'''

#----continue demo,continue 结束本次循环,紧接着执行下次循环,只对最近的一层循环起作用-----
'''
name = "QiangGe"
for x in name:
    print("------")
    if x == "G":
        continue
    print(x)

'''

#----字符串的切片操作
# name = "abcdef"

# print(name[1:3]) #bc
# print(name[2:])         # cdef 取下标2到最后的字符串
# print(name[2:0])       #cdef  取下标2到最后第二个字符,最后一个元素的下标为-1
# print(name[2:-1])       #cde 取下标2到最后第二个字符,最后一个元素的下标为-1
# print(name[:3])       #abc
#print(name[::2])       #ace 步长为2 ;
# print(name[1:5:2])      #bd
# print(name[::-2])      # 反向取
# print(name[5:1:-2])      # fd 反向取
# print name[::-1]+"wzq"      #字符串倒叙输出

# print   name*3  #拼接本字符串N次;

# str = "hello world wzq"
# print(str.partition("world"))   # 根据参数分割成三个字符串


# strTemp = "hello\nwzq"  # 把每行的文字放入列表
# print(strTemp.splitlines())


# 判断是否只有字母和数字
# strTemp = "wzq 123"
# print(strTemp.isalnum())


# 判断是否只包含空格
# str = " "
# print(str.isspace())

# 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
# str = "_"
# li  = ['wzq','zyn','mcx']
# print(str.join(li))     # wzq_zyn_mcx



#   -----------列表的操作-------------
# li1 = ['q',1,'wzq']  #可以存储不同元素;
# li2 = [3,4,5,6]
# print(li)
# print(li[1])

#  while 循环列表
# i = 0
# length = len(li)
# while i<length:
#     print(li[i])
#     i+=1

# li1.append(li2)
# print(li1)  #['q', 1, 'wzq', [3, 4]]


# 把li2 中的元素一个个添加到第一个li1中
# li1.extend(li2)
# print(li1)


#    在当前下标前插入元素
# li2.insert(2,"wzq")
# print(li2)

#   修改元素
# li2[0] = 0
# print(li2)

li=[0,1,2,3,4,3,'w']

#   in  notin  判断是否存在
# print( 1 in li)

# index 获取某个元素的下标,后面两个参数是区间,左闭右开
# print(li.index(3,4,10))

#   计算元素出现的次数;
# print(li.count(3))

# 删除列表的元素
#   删除列表的最后一个元素,并返回删除的元素
# li.pop()

#   根据下标来删某个元素
# del li[3]

#   remove,删除某个元素

# li.remove(3)    # 删除某个元素,如果有多个,只删除第一个;
# print(li)

# sort ,reverse ,

# li.sort()
# li.reverse()
# li.sort(reverse=True)  #    传递倒叙参数;
# print(li)

# 二位列表 随机分配讲师
# import random
# names = ['b', 'c', 'd', 'e', 'f', 'g', 'h']
# office = [[],[],[]]
#
#
# for x in names:
#     index = random.randint(0, 2)
#     office[index].append(x)
#
# for off in office:
#     for a in off:
#         print(a)
#
#     print("-------")




# ---------元组,  元组--------------------

mTuple = ('wzq',30,30)
# print mTuple
# print(mTuple[0])

# mTuple[0] = 'zyn'     #    报错, 不支持修改
# print(mTuple.index(30,0,10))
# print(mTuple.count(30))


# ---------字典--------------------
# 列表修改元素,根据下标, 如果顺序变了, 修改元素就要修改下标,可以用字典,根据key来修改

info = {'name':'wzq','age':30}
# print(info.get(name))   # 获取value的方法
# print((info[age]))      #获取value的第二种方法

# 默认值
# print(info.get('wife','zyn')) #获取不到 返回默认值;

#   增加元素
# info['id'] = 1
# print(info.get("id"))

#   删除元素

# del info
# print(info)

# 清空字典
# info.clear()
# print(info)

# print(len(info))    #获取字典的长度
# print(info.keys())
# print(info.values())
# print(info.items()) #[('age', 30), ('name', 'wzq')]
#
# print(info.has_key('name')) # 是否包含key




#--------循环--------
#   fon in 可以遍历 list tuple 字典,

#
# for key,value in info.items():
#     print("key=%s,value=%s"%(key,value))

# chars  = ['a','b','c']
# for char in enumerate(chars):
#     print char


# --------使用global声明全局变量
# a =1;
# def fn():
#     global a  # 声明一下变量
#     a +=1
#     print(a)
#
# fn();

#   函数返回多个值

# def more(a,b):
#     return a+1,b+1;
# a,b = more(1,2)
# print(a,b)  #(2, 3)

#   带有默认值得函数
# name = "sss"
# def mPrint(name,age=30):    #默认参数一定要位于参数列表的最后面;
#     print("name:"+name)
#     print("age:%d"%age)
#
# mPrint(name='wzq')


#   可变参数
# def fun(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
#     for key,value in kwargs.items():
#         print(key,"=",value)

'''
1
2
(3, 4, 5)
{'p': 8, 'm': 6, 'n': 7}
('p', '=', 8)
('m', '=', 6)
('n', '=', 7)
'''
# fun(1,2,3,4,5,m=6,n=7,p=8)


# c= (3,4,5)
# d={'m':6,'n':7,'p':8}

'''
1
2
(3, 4, 5)
{'p': 8, 'm': 6, 'n': 7}
('p', '=', 8)
('m', '=', 6)
('n', '=', 7)
'''
# fun(1,2,*c,**d) #传入的是元组和字典;


'''
1
2
((3, 4, 5), {'p': 8, 'm': 6, 'n': 7})
{}
'''
# c= (3,4,5)
# d={'m':6,'n':7,'p':8}
# fun(1,2,c,d) #多余的参数都封装到了元组里面;

#可变与不可变形参的区别

def selfAdd(a):
    print 'test',id(a)
    a = a+a;
    print "test--",id(a)
    print("test--",a)

# a =1
# selfAdd(a)
# print(a)    #1 打印的是全局变量a,a不可变

b = [1,2]
# print id(b)
'''
a+=a的情况
4467023672
test 4467023672   id都没变
test-- 4467023672
('test--', [1, 2, 1, 2])
[1, 2, 1, 2]
4467023672

----------
a = a+a的情况
4316712760
test 4316712760
test-- 4316791008   局部生成了新对象; id变了
('test--', [1, 2, 1, 2])
[1, 2]
4316712760


'''
# selfAdd(b)  #[1, 2, 1, 2]
# print(b)
# print id(b)


#------递归,计算n的连乘积

# def fun(num):
#     if(num>1):
#       return num *   fun(num-1)
#     else:
#         return 1
#
# print fun(3)


#   lambda [arg1,[arg2,arg3]] : expression
# sum = lambda arg1,arg2: arg1+arg2
# print(sum(1,3))

# lambda 作为内置函数的参数
'''
stu = [
    {"name":'wzq',"age":30},
    {"name":'zyn',"age":29}

]

stu.sort(key = lambda x:x['age'])
print(stu)
'''

# ---------文件的操作
'''
r 读,从开泰
w 写,覆盖写入
a,追加写入
'''

# f = open('wzq.txt','w')
# f.write('我是wzq')
# f.close()

# f = open('wzq.txt','r')
# content = f.read()
# print(content)


#一次性读取readLines
f = open('wzq.txt','r')
content = f.readlines()
print(type(content))


for  line in content:
    print(line)

f.close()































