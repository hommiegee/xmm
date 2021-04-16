import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#------------------------------------------------------------------
# 读取excel数据，保存到data里
# 把data变成numpy.array格式的数组
data = pd.read_excel('./xm.xls')
data = np.array(data)
#------------------------------------------------------------------
# 获得大于10秒的起止位置
idx_10 = np.where(data[:, 0] > 7)
idx_10 = idx_10[0][0]
#------------------------------------------------------------------
data = data[idx_10: , :]
#------------------------------------------------------------------
# 搜索极大值
def localmax(x):
    ans = []
    index = []
    for i in range(12, len(x) - 12):
        if x[i] > x[i - 1] and x[i] > x[i - 2] and x[i] > x[i - 3] and x[i] > x[i - 4] and x[i] > x[i - 5]:
            if x[i] > x[i - 6] and x[i] > x[i - 7] and x[i] > x[i - 8] \
            and x[i] > x[i - 9] and x[i] > x[i - 10]:
                if x[i] > x[i - 11] and x[i] > x[i - 12]:
                    if x[i] >= x[i + 1] and x[i] >= x[i + 2] and x[i] >= x[i + 3] and x[i] >= x[i + 4] and x[i] >= x[i + 5]:
                        if x[i] >= x[i + 6] and x[i] >= x[i + 7] and x[i] >= x[i + 8] \
                        and x[i] >= x[i + 9] and x[i] >= x[i + 10]:
                            if x[i] >= x[i + 11] and x[i] >= x[i + 12]:
                                ans.append(x[i])
                                index.append(i)
    return ans, index
#------------------------------------------------------------------
# 获得极大值数值以及对应索引值
localmax_value, localmax_index = localmax(data[:, 1])
#------------------------------------------------------------------
idx_num = len(localmax_index)

localmax_x = data[:, 0][localmax_index]

T = []

for i in range(int(idx_num - 1)):
    tmp_T = localmax_index[i+1] - localmax_index[i]
    T.append(tmp_T)

T = np.sum(T) / len(T) * 0.01

print('周期：', T)

plt.plot(data[:, 0], data[:, 1])


plt.scatter(localmax_x, localmax_value, color='r')


plt.title('T: {}'.format(T))


plt.show()
