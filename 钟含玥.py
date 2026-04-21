import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 1. 实验原始数据
t_celsius = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
Ig = np.array([245, 342, 454, 588, 693, 807, 903, 987, 1074, 1114])

# 2. 平滑曲线处理 (需要已安装 scipy)
t_smooth = np.linspace(t_celsius.min(), t_celsius.max(), 300)
spl = make_interp_spline(t_celsius, Ig, k=3)
Ig_smooth = spl(t_smooth)

# 3. 绘图
plt.figure(figsize=(8, 6), dpi=100)
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

plt.scatter(t_celsius, Ig, color='blue', label='实验测量点', zorder=5)
plt.plot(t_smooth, Ig_smooth, color='red', linewidth=2, label='定标曲线 $t-I_g$')

# 注意这里的 r'' 前缀，解决了你的 SyntaxWarning
plt.xlabel(r'温度 $t$ ($^\circ$C)', fontsize=12)
plt.ylabel(r'检流计电流 $I_g$ ($\times 10^{-3}$ mA)', fontsize=12)
plt.title(r'热敏电阻定标曲线 ($t-I_g$)', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()