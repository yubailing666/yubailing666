import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# --- 1. 实验参数设置 ---
# 每段间距 3.478 cm，转换为米 (m)
L = 0.03478 
# 刻度点对应的总位移 (t9作为起点0, t8是1段距离, ..., t2是7段距离)
distances = np.array([0, 1, 2, 3, 4, 5, 6, 7]) * L

# --- 2. 录入实验数据 (单位: s) ---
# A球数据 (根据照片提取)
data_A = np.array([
    [2.04, 2.95, 3.98, 5.13, 6.21, 7.50, 8.70, 9.81],
    [3.07, 4.10, 5.27, 6.39, 7.48, 8.76, 9.89, 11.11],
    [3.83, 4.67, 5.42, 7.10, 8.35, 10.35, 11.57, 11.74]
])

# B球数据
data_B = np.array([
    [2.95, 4.73, 6.35, 7.80, 9.91, 11.66, 13.24, 15.00],
    [2.72, 4.38, 6.16, 7.90, 9.65, 11.23, 13.20, 15.00],
    [3.59, 5.55, 7.23, 8.79, 11.09, 12.50, 14.26, 15.91]
])

# C球数据
data_C = np.array([
    [4.05, 7.10, 10.07, 13.10, 16.10, 19.12, 22.27, 25.38],
    [3.54, 6.73, 9.76, 12.62, 15.82, 18.77, 21.87, 24.92],
    [3.79, 6.82, 9.76, 12.85, 15.73, 18.71, 21.60, 24.70]
])

def process_and_plot(name, time_data, dists, color):
    # 1. 计算三次实验的平均时间
    avg_times = np.mean(time_data, axis=0)
    # 2. 以第一个记录点t9为时间零点，计算相对时间
    rel_times = avg_times - avg_times[0]
    
    # 3. 线性回归拟合: s = v_f * t
    # 我们强制通过(0,0)点或者使用标准拟合。这里使用标准拟合以观察是否存在启动加速度
    slope, intercept, r_value, p_value, std_err = linregress(rel_times, dists)
    
    # 绘图
    plt.scatter(rel_times, dists, color=color, label=f'Ball {name} Data')
    plt.plot(rel_times, slope * rel_times + intercept, color=color, linestyle='--', 
             label=f'Ball {name} Fit (v_f={slope:.4f} m/s)')
    
    print(f"--- 球 {name} 结果 ---")
    print(f"平均收尾速度 v_f = {slope:.5f} m/s")
    print(f"拟合截距 (应接近0) = {intercept:.5f} m")
    print(f"拟合优度 R² = {r_value**2:.5f}\n")
    
    return slope

# --- 3. 执行计算与可视化 ---
plt.figure(figsize=(10, 7))

v_f_A = process_and_plot('A', data_A, distances, 'red')
v_f_B = process_and_plot('B', data_B, distances, 'blue')
v_f_C = process_and_plot('C', data_C, distances, 'green')

plt.title("Viscosity Experiment: Distance vs Time (L=3.478cm)")
plt.xlabel("Time relative to t9 (s)")
plt.ylabel("Falling Distance (m)")
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()