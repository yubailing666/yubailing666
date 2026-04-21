import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_circuit_schematic():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    
    # 绘制外接法示意框
    # 电源线
    ax.plot([1, 2], [4, 4], 'k-') 
    # 电流表 A
    circle_a = patches.Circle((2.5, 4), 0.3, fill=False, edgecolor='k')
    ax.add_patch(circle_a)
    ax.text(2.4, 3.9, 'A', fontsize=12)
    
    # 连接线
    ax.plot([2.8, 5, 5], [4, 4, 3.5], 'k-')
    
    # 负载 L
    rect_l = patches.Rectangle((4.5, 2.5), 1, 1, fill=False, edgecolor='k')
    ax.add_patch(rect_l)
    ax.text(4.8, 2.9, 'R_L', fontsize=10)
    
    # 电压表 V (外接)
    ax.plot([3.5, 3.5, 6.5, 6.5], [4, 1.5, 1.5, 2.5], 'k-') # 跨接线
    circle_v = patches.Circle((5, 1.5), 0.3, fill=False, edgecolor='k')
    ax.add_patch(circle_v)
    ax.text(4.9, 1.4, 'V', fontsize=12)
    
    ax.set_title("实验原理：电流表外接法示意图", fontsize=14)
    ax.axis('off')
    plt.show()

draw_circuit_schematic()