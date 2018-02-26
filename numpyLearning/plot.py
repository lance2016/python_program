# coding:utf-8
from numpy import *
from matplotlib import *
from matplotlib.pyplot import *
x = linspace(1, 2*pi, 50)

# pl.plot(sin(x))


# x = random.rand(200)*200
# y = random.rand(200)*200
# size = random.rand(200)*30
# color = random.rand(200)
# pl.scatter(x, y, size, color)
# pl.colorbar()
# pl.show()
# # 显示颜色条
t = linspace(0, 2*pi, 50)
x = sin(t)
y = cos(t)
# pl.figure()
# pl.plot(x)
# pl.figure()
# pl.plot(y)


show()
plot(x)
hold(False)
plot(y)
hold(True)
show()


