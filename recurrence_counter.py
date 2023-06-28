from functools import wraps

def profiler(func):
    class Counter:
        '''
        计数器类
        '''
        def __init__(self):
            self.count = 0    # 计数器
            self.stuck_deep = 0    # 当前计数器位于递归函数的递归深度，或者说是栈的深度

        def increase(self):
            '''
            自增
            '''
            self.count += 1

        def init(self):
            '''
            初始化
            '''
            self.__init__()

    counter = Counter()
    @wraps(func)    # 返回的装饰器函数 f 继承被装饰函数 func 的属性，包括 __doc__，__name__等
    def f(*args):
        counter.stuck_deep += 1    # 入栈
        counter.increase()    # 计数器自增
        value = func(*args)    # 调用函数并存储返回值
        counter.stuck_deep -= 1    # 出栈
        if counter.stuck_deep==0:    # 如果栈为空，则证明递归过程结束，进行初始化
            f.calls = counter.count    # 为了满足题目要求，将计数器内容给函数的属性 calls
            counter.init()    # 初始化计数器
        return value
    return f

@profiler
def ack(m, n):
    '''
    this is the function's __doc__ part
    '''
    while(m!=0):
        if(n==0):
            n=1
        else:
            n=ack(m, n-1)
        m -= 1
    return n+1

ack(3, 4)

print(ack.calls)    # 5094

ack(3, 2)

print(ack.__doc__)    # this is the function's __doc__ part
print(ack.calls)        # 258