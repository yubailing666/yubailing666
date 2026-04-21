import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 设置绘图风格
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# ==========================================
# 1. 小灯泡伏安特性（内外接法对比）
# ==========================================
U_bulb = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0])
I_in = np.array([16, 24, 31, 36, 46, 56, 64, 72])    # 内接法电流(mA)
I_ex = np.array([24, 31, 37, 41, 51, 60, 68, 76])    # 外接法电流(mA)

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.plot(U_bulb, I_ex, 'bs-', markersize=4, label='电流表外接法')
plt.plot(U_bulb, I_in, 'ro-', markersize=4, label='电流表内接法')
plt.title('图1：钨丝小灯泡伏安特性曲线', fontsize=12)
plt.xlabel('电压 U (V)')
plt.ylabel('电流 I (mA)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# ==========================================
# 2. 发光二极管（LED）拟合与波长计算
# ==========================================
# 提取手稿中的 LED 数据
I_led = np.array([1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50])
V_green = np.array([2.360, 2.448, 2.591, 2.697, 2.786, 2.860, 3.006, 3.121, 3.206, 3.287, 3.336, 3.376, 3.416, 3.453])
V_blue = np.array([2.707, 2.793, 2.906, 2.984, 3.038, 3.082, 3.161, 3.219, 3.258, 3.278, 3.330, 3.330, 3.359, 3.380])

plt.subplot(132)
plt.plot(V_green, I_led, 'g^', label='绿色 LED 原始数据')
plt.plot(V_blue, I_led, 'b^', label='蓝色 LED 原始数据')

# 仿照学长报告进行线性拟合（取最后5组高电流数据）
def fit_led(V, I, color, name):
    slope, intercept, r_value, p_value, std_err = stats.linregress(V[-5:], I[-5:])
    V_fit = np.linspace(V[-6], V[-1]+0.2, 10)
    I_fit = slope * V_fit + intercept
    Ud = -intercept / slope # 计算横轴截距，即阈值电压
    plt.plot(V_fit, I_fit, color + '--', alpha=0.8, label=f'{name} 拟合线')
    return Ud

Ud_g = fit_led(V_green, I_led, 'g', '绿光')
Ud_b = fit_led(V_blue, I_led, 'b', '蓝光')

plt.title('图2：发光二极管伏安特性及拟合', fontsize=12)
plt.xlabel('电压 U (V)')
plt.ylabel('电流 I (mA)')
plt.annotate(f'Ud_green={Ud_g:.3f}V', xy=(Ud_g, 0), xytext=(Ud_g-0.5, 10), arrowprops=dict(arrowstyle='->'))
plt.annotate(f'Ud_blue={Ud_b:.3f}V', xy=(Ud_b, 0), xytext=(Ud_b+0.2, 5), arrowprops=dict(arrowstyle='->'))
plt.legend(fontsize=9)
plt.ylim(0, 55)

# ==========================================
# 3. 稳压二极管（正向与反向全特性）
# ==========================================
# 正向数据
I_z_fwd = np.array([1, 2, 4, 6, 8, 10, 15, 20, 30, 40, 50])
V_z_fwd = np.array([0.737, 0.773, 0.791, 0.802, 0.811, 0.817, 0.828, 0.838, 0.852, 0.863, 0.885])

# 反向数据（注意：反向测量时，电压和电流在坐标系中应呈现为负值）
I_z_rev = -np.array([1, 2, 4, 6, 8, 10, 15, 20, 30, 40, 50])
V_z_rev = -np.array([2.565, 2.773, 3.016, 3.173, 3.284, 3.369, 3.522, 3.635, 3.747, 3.807, 3.883])

plt.subplot(133)
plt.plot(V_z_fwd, I_z_fwd, 'ks-', markersize=4, label='正向特性')
plt.plot(V_z_rev, I_z_rev, 'ko-', markersize=4, label='反向特性')

# 添加坐标轴中心线（学长报告风格）
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.title('图3：稳压二极管正、反向伏安特性', fontsize=12)
plt.xlabel('电压 U (V)')
plt.ylabel('电流 I (mA)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()

# 输出波长计算结果（用于填入报告）
h, c, e = 6.626e-34, 2.998e8, 1.602e-19
lambda_g = (h * c) / (e * Ud_g) * 1e9
lambda_b = (h * c) / (e * Ud_b) * 1e9
print(f"计算所得绿光波长: {lambda_g:.1f} nm")
print(f"计算所得蓝光波长: {lambda_b:.1f} nm")