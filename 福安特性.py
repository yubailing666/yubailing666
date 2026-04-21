import numpy as np
import matplotlib.pyplot as plt

# --- 1. 原始实验数据录入 ---
t_celsius = np.array([40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
T_kelvin = t_celsius + 273.15                                 
Rt = np.array([3580, 2900, 2380, 1960, 1720, 1510, 1375, 1272, 1180, 1142])

# --- 2. 变量变换 ---
X = 1 / T_kelvin     
Y = np.log(Rt)       

# --- 3. 线性拟合 (使用 numpy.polyfit，更简洁) ---
# B 为斜率(对应 b)，A 为截距(对应 ln a)
B, A = np.polyfit(X, Y, 1)
a = np.exp(A)
b = B

# 计算相关系数 r
r = np.corrcoef(X, Y)[0, 1]

print("------ 实验数据处理结果 ------")
print(f"拟合直线方程: Y = {A:.4f} + {B:.4f} * X")
print(f"材料常数 b: {b:.2f} K")
print(f"材料常数 a: {a:.6f} Ohm")
print(f"相关系数 r: {r:.4f}")

# --- 4. 绘图可视化 ---
# 注意：如果你的电脑没装 SimHei 字体，请删除下面这两行，或者换成系统自带的中文字体
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 子图1: 使用 r'' 解决转义警告
ax1.scatter(X, Y, color='red', label='实验观测值')
ax1.plot(X, A + B*X, color='blue', label='拟合直线')
ax1.set_xlabel('1/T ($K^{-1}$)')
ax1.set_ylabel(r'$\ln(R_t)$') # 这里加了 r
ax1.set_title(r'线性化拟合: $\ln(R_t)$ vs $1/T$')
ax1.legend()
ax1.grid(True)

# 子图2
ax2.scatter(t_celsius, Rt, color='green', label='原始数据点')
t_smooth = np.linspace(t_celsius.min(), t_celsius.max(), 100)
Rt_smooth = a * np.exp(b / (t_smooth + 273.15))
ax2.plot(t_smooth, Rt_smooth, color='orange', label='拟合曲线')
ax2.set_xlabel('温度 t (°C)')
ax2.set_ylabel('电阻 $R_t$ ($\Omega$)')
ax2.set_title('热敏电阻 $R_t-t$ 特性曲线')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()