from numpy import *
randMat = mat(random.rand(4,4))
print randMat
invRandMat = randMat.I
myEye = randMat * invRandMat
print myEye - eye(4)

