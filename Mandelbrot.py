import numpy as np
def 离散复平面网络(长,宽,实轴左端点,实轴右端点,虚轴左端点,虚轴右端点,最大迭代次数):
    实部数组=np.linspace(实轴左端点,实轴右端点,长)
    虚部数组=np.linspace(虚轴左端点,虚轴右端点,宽)
    结果矩阵=np.ones((长,宽),dtype=np.float32)
    for x in range(长):
        for y in range(宽):
            c=np.complex64(实部数组[x]+虚部数组[y]*1j)
            z=np.complex64(0)
            for i in range(最大迭代次数):
                z=z*z+c
                if(np.abs(z)>2):
                    结果矩阵[y,x]=0
                    break
    return 结果矩阵

#导出图形
from time import time
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

if __name__=='__main__':
    t1=time()
    生成集合=离散复平面网络(512,512,-2,2,-2,2,256)
    t2=time()
    生成集合时间=t2-t1
    t3=time()
    分型图=plt.figure(1)
    plt.imshow(生成集合,extent=(-2,2,-2,2))
    plt.savefig('1.png',dpi=分型图.dpi)
    t4=time()
    画图时间=t4-t3
    print("生成集合时间为",生成集合时间,"画图时间为",画图时间)

