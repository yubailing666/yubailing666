import matplotlib.pyplot as plt
import pandas as pd

# 1. 整理实验数据
data = {
    'x': range(-9, 10),
    'B1': [239, 261, 281, 295, 300, 298, 287, 268, 244, 219, 193, 169, 147, 126, 109, 93, 79, 68, 58],
    'B2': [56, 65, 75, 88, 103, 119, 139, 162, 186, 213, 238, 262, 283, 296, 301, 296, 283, 262, 240],
    'B_measured': [295, 328, 360, 387, 408, 422, 430, 434, 435, 436, 435, 436, 430, 423, 410, 391, 364, 335, 303]
}
df = pd.DataFrame(data)

# 2. 设置绘图风格
plt.figure(figsize=(10, 6), dpi=100)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示（如果环境支持）
plt.rcParams['axes.unicode_minus'] = False 

# 3. 绘制三条曲线
# 单线圈1 (虚线)
plt.plot(df['x'], df['B1'], label='单线圈 1 (B1)', color='#ff7f0e', linestyle='--', marker='s', markersize=4, alpha=0.8)
# 单线圈2 (虚线)
plt.plot(df['x'], df['B2'], label='单线圈 2 (B2)', color='#1f77b4', linestyle='--', marker='^', markersize=4, alpha=0.8)
# 亥姆霍兹线圈测量值 (实线，加粗)
plt.plot(df['x'], df['B_measured'], label='亥姆霍兹线圈 (测量值)', color='#d62728', linestyle='-', marker='o', markersize=6, linewidth=2)

# 4. 图表美化
plt.title('亥姆霍兹线圈轴线磁场分布特性图', fontsize=14)
plt.xlabel('轴线位置 x (cm)', fontsize=12)
plt.ylabel('磁感应强度 B (μT)', fontsize=12) # 单位请根据实验仪器确认，通常为μT或Gs

# 添加辅助线，突出中心均匀区
plt.axvspan(-2, 2, color='gray', alpha=0.1, label='磁场均匀区')

plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend(loc='best')

# 5. 保存并展示
plt.tight_layout()
plt.savefig('helmholtz_plot.png') # 自动保存为清晰图片
plt.show()