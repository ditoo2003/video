# for i in [1,2,3,4]:
#     if i > 2:
#         print (i)
#         break
# else:
#     print(i,'我是else')
#

def multi_sum(*args):
    s = 0
    for item in args:
        s += item
    return s


# result=multi_sum(3,4,5)
# # print(result)

# def do_something(name,age,gender='男',*args,**kwds):
#     print('姓名：%s,年龄：%d,性别：%s'%(name,age,gender))
#     print(args)
#     print(kwds)
#
# do_something('xufive', 50, '男', 175, 75, math=99, english=90)
#
# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
#
# print('\n'.join([''.join(['*' if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0 else s(s,z*z+c,c,n-1))(0,0.02*x+0.05j*y,40))<2 else ' ' for x in range(-80,20)]) for y in range(-20,20)]))

# def get_square(n):
#     for i in range(n):
#         yield (pow(i,2))
#
# a=get_square(9)
# print(type(a))
# for i in a:
#     print(i,end='---')

import time

def timer(func):
    def wrapper(*args, **kwds):
        t0 = time.time()
        func(*args, **kwds)
        t1 = time.time()
        print('耗时%0.3f' ,(t1 - t0))
        return wrapper


def do_something(delay):
    print('函数do_something开始')
    time.sleep(delay)
    print('函数do_something结束')

do_something(3)
