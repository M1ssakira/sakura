# sakura
因为一些知识不常用，导致每次需要用的时候都要重新理解，所以开一个仓库来进行知识点和代码的备忘。
finis.
test

装饰器
---
装饰本质上是语法糖，利用闭包这种可以携带外部引用的机制实现的  
装饰原本函数，并且通过原本函数名进行调用,函数本身也是对象。  
作用是做一些与logic无关的工作，看起来就是简化代码了，而且可以复用，  
本质上是语法糖，就是方便了点。打log或者 算运行时间这样。  
```
'''
def decrator(func):
    def fooo(number):
        def wrapper(args):
            print ('<**>',number,type(number))
            ---> print  number is a foo func obj,
            所以这个语法糖是解析成了29行的样子
            for x in range(number):
                print ('befor call func  args-->',args)
                func(args)
                print ('after call func  args-->',args)
        return wrapper
    return fooo
'''

def decrator(number):
    def fooo(func):
        def wrapper(args):
            print ('<**>',number,type(number))
            for x in range(number):
                print ('befor call func  args-->',args)
                func(args)
                print ('after call func  args-->',args)
        return wrapper
    return fooo

@decrator(3)
def foo(name):
    print ('i am lilith',name)
# foo = decrator(args)(foo)
# foo = decrator(foo)
# 带参数的装饰器，需要在普通的decrator上再套一层闭包，跟line29一样。而不是注释
# 中的那种，这点要注意
foo('rubik')
```