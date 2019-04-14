#In python every .py files is called a module
#We can import a module in other module using import statement
"""
import Session20B
Session20B.sysDemo()
Session20B.show()
"""
"""
import Session20B as S20B   #Alias
S20B.sysDemo()
S20B.show()
"""
"""
from Session20B import  *
sysDemo()
#show() ->This isn't imported
"""

from mypack import one
from mypack import two

one.hello()
two.bye()
# Assignment : Try exploring what can work with mypack as in above import statements