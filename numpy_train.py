import numpy as np

# 序列转矩阵
array = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(array)
print("number of dim:", array.ndim)
print("shape:", array.shape)
print("size:", array.size)

# 指定数据dtype
array = np.array([[1, 2, 3],
                  [4, 5, 6]], dtype=np.int)
print(array.dtype)

# 常用函数
z = np.zeros((3, 2))
a = np.ones((3, 4), dtype=int)
e = np.empty((2, 3))
r = np.arange(10, 20, 2)
r1 = np.arange(12).reshape((3, 4))
l = np.linspace(10, 20, 3)
print(z)
print(a)
print(e)
print(r)
print(r1)
print(l)

# 常用基本运算
a = np.array([12, 20, 30, 40])
b = np.arange(4)

print("a-b:", a - b)
print("a+b:", a + b)
print("a*b:", a * b)
print("b的平方:", b**2)
print("b的sin:", np.sin(b))
print("b的tan:", np.tan(b))
print("对b逻辑判断:", b > 3)

# 多维运算
a = np.array([[1, 2], [3, 4]])
b = np.random.random((2,2))
print("a b 矩阵运算方式1:", np.dot(a, b))
print("a b 矩阵运算方式2:", a.dot(b))
print("求a的最大值:", np.max(a))
print("求a的所有数的和:", np.sum(a))
print("求a的最小值:", np.min(a))
# axis为1时以行为查找单位，为0时以列为查找单位
print("求a行的最小值:", np.min(a, axis=1))
print("求a列的最小值:", np.min(a, axis=0))
print("求a列的和:", np.sum(a, axis=0))

print("求a最大值的索引:", np.argmax(a))
print("求a最小值的索引:", np.argmin(a))

print("求a的中位数:", np.median(a))
print("求a的均数:", np.mean(a))
print("求a的均数:", a.mean())
print("a的累加:", np.cumsum(a))
print("a的累差:", np.diff(a))
print("非零项nonzero:", np.nonzero(a))
print("a的排序:", np.sort(a))
print("a的转置:", np.transpose(a))
print("a的转置:", a.T)
print("clip函数:", a.clip(2, 3))

A = np.arange(3, 15)
print("A中索引为3的元素:", A[3])
A = np.arange(3, 15).reshape((3, 4))
print("A:", A)
print("A矩阵中索引为[1,2]的元素:", A[1, 2])
print("A矩阵中2行，2到3列:", A[1, 1:3])
# 按行打印
for row in A:
    print(row)

# 按列打印
for col in A.T:
    print(col)

# 将A展开为1行的数列
print("将A展开为一行的数列:", A.flatten())
# 将A一个个元素打印，迭代器flat
for item in A.flat:
    print(item)

# numpy的array合并
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
print("a b纵向合并:", np.vstack((a, b)))
print("a b横向合并:", np.hstack((a, b)))

# np.newaxis
print("将a数组转为矩阵:", a[np.newaxis, :])
print("矩阵a的shape:", a[np.newaxis, :].shape)
print("将a数组转为矩阵:", a[:, np.newaxis])
print("矩阵a的shape:", a[:, np.newaxis].shape)

a = np.array([1, 1, 1])[:, np.newaxis]
b = np.array([2, 2, 2])[:, np.newaxis]

# axis为零纵向合并，为1横向合并
print("多个矩阵合并，纵向合并axis=0:", np.concatenate((a, b, b, a), axis=0))
print("多个矩阵合并，横向合并axis=1:", np.concatenate((a, b, b, a), axis=1))

# numpy的array分割 axis为1表示按行做函数操作，为0表示按列做函数操作
a = np.arange(12).reshape(3, 4)
print(a)
print("分割为2部分，axis=1:", np.split(a, (1, 2, 3), axis=1))

# 如果一个多维数组是2*3*2，他就是3维的，参数axis=0指的就是第一维，即2那一个数轴，axis=1,即3的那个数轴，axis=2,即最后2的那个数轴。也可以说是shape元素的索引。
# np.vsplit() np.hsplit()







