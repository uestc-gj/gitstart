# -*- coding: utf-8 -*-
'''
数据封装
'''
class Student( object ):
	def __init__(self, name, score):
		self.__name = name
		self._score = score

	def get_grade(self):
		print '%s\'s grade is: %s' % (self.__name, self._score)

'''
继承和多态
'''
class animal( object ):
    def run( self ):
        '''
        This is a function shows animal could run as human beings!
        '''
        print 'Animal is running...'
    def run_twice( animal ):
        animal.run()
        animal.run()

class Dog( animal ):
    def run( self ):
        print 'Dog is running...'

#新增一个Animal的子类，不必对run_twice()做任何修改，实际上，
#任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态
#多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收
#Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型

#这就是著名的“开闭”原则：
#对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


class BaseClass(object):    
    def __init__(self):
        self.name = 'BaseClass'
        print('BaseCalss: Constructor called')
    def getname(self):
        print('BaseCalss: self name equals ' + self.name)
 
class DerivedClass(BaseClass):
    def __init__(self):
        #派生类定义__init__()时不会自动调用基类的__init__()方法因此要调用基类的
        #__init__()方法进行恰当的初始化
        BaseClass.__init__(self)
        #super(DerivedClass, self).__init__()
        print('DerivedClass: Constructor called')
 
if __name__ == '__main__':
    class1 = BaseClass()
    class1.getname()
    
    class2 = DerivedClass()
    class2.getname()
