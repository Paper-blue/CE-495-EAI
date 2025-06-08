#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生成修复后的Algorand算法图示
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

def create_algorand_algorithm_figure():
    # 创建图形和坐标轴
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 设置坐标轴范围
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    
    # 隐藏坐标轴
    ax.axis('off')
    
    # 绘制算法流程图
    # 开始框
    start_box = patches.Rectangle((5, 9), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(start_box)
    ax.text(6, 9.4, "Start", ha='center', va='center', fontsize=12)
    
    # 第一步标题
    ax.text(6, 8.5, "Step 1", ha='center', va='center', fontsize=14, weight='bold')
    
    # 投票框
    vote_box = patches.Rectangle((5, 7.5), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(vote_box)
    ax.text(6, 7.9, "Vote $b_i$", ha='center', va='center', fontsize=12)
    
    # 计票框
    count_box = patches.Rectangle((5, 6.5), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(count_box)
    ax.text(6, 6.9, "Count #(0), #(1)", ha='center', va='center', fontsize=12)
    
    # 条件判断框1
    cond1_box = patches.Polygon([(6, 5.5), (7.5, 5), (6, 4.5), (4.5, 5)], linewidth=1, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(cond1_box)
    ax.text(6, 5, "#(0) ≥ 2t+1?", ha='center', va='center', fontsize=10)
    
    # 条件判断框2
    cond2_box = patches.Polygon([(6, 3.5), (7.5, 3), (6, 2.5), (4.5, 3)], linewidth=1, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(cond2_box)
    ax.text(6, 3, "#(1) ≥ 2t+1?", ha='center', va='center', fontsize=10)
    
    # 结果框1
    result1_box = patches.Rectangle((8, 4.6), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(result1_box)
    ax.text(9, 5, "$b_i = 0$, Terminate", ha='center', va='center', fontsize=12)
    
    # 结果框2
    result2_box = patches.Rectangle((8, 2.6), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(result2_box)
    ax.text(9, 3, "$b_i = 1$, Terminate", ha='center', va='center', fontsize=12)
    
    # 第一步Otherwise结果框
    otherwise1_box = patches.Rectangle((2, 3.6), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(otherwise1_box)
    ax.text(3, 4, "$b_i = 0$", ha='center', va='center', fontsize=12)
    
    # 第二步标题
    ax.text(3, 2.5, "Step 2", ha='center', va='center', fontsize=14, weight='bold')
    
    # 第二步计票框
    count2_box = patches.Rectangle((2, 1.5), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(count2_box)
    ax.text(3, 1.9, "Count #(0), #(1)", ha='center', va='center', fontsize=12)
    
    # 第二步条件判断框1
    cond3_box = patches.Polygon([(3, 0.5), (4.5, 0), (3, -0.5), (1.5, 0)], linewidth=1, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(cond3_box)
    ax.text(3, 0, "#(0) ≥ 2t+1?", ha='center', va='center', fontsize=10)
    
    # 第二步条件判断框2
    cond4_box = patches.Polygon([(3, -1.5), (4.5, -2), (3, -2.5), (1.5, -2)], linewidth=1, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(cond4_box)
    ax.text(3, -2, "#(1) ≥ 2t+1?", ha='center', va='center', fontsize=10)
    
    # 第二步结果框1
    result3_box = patches.Rectangle((5, -0.4), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(result3_box)
    ax.text(6, 0, "$b_i = 0$, Terminate", ha='center', va='center', fontsize=12)
    
    # 第二步结果框2
    result4_box = patches.Rectangle((5, -2.4), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(result4_box)
    ax.text(6, -2, "$b_i = 1$, Terminate", ha='center', va='center', fontsize=12)
    
    # 第二步Otherwise结果框
    otherwise2_box = patches.Rectangle((0, -1.4), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(otherwise2_box)
    ax.text(1, -1, "$b_i = 1$", ha='center', va='center', fontsize=12)
    
    # 第三步标题
    ax.text(1, -3, "Step 3", ha='center', va='center', fontsize=14, weight='bold')
    
    # 第三步硬币框
    coin_box = patches.Rectangle((0, -4), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(coin_box)
    ax.text(1, -3.6, "Common Coin c", ha='center', va='center', fontsize=12)
    
    # 第三步结果框
    result5_box = patches.Rectangle((0, -5), 2, 0.8, linewidth=1, edgecolor='black', facecolor='lightyellow')
    ax.add_patch(result5_box)
    ax.text(1, -4.6, "$b_i = c$, Terminate", ha='center', va='center', fontsize=12)
    
    # 连接线
    # 开始到投票
    ax.arrow(6, 9, 0, -0.7, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 投票到计票
    ax.arrow(6, 7.5, 0, -0.2, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 计票到条件1
    ax.arrow(6, 6.5, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 条件1到结果1
    ax.arrow(7.5, 5, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(7.7, 5.1, "Yes", fontsize=10)
    
    # 条件1到条件2
    ax.arrow(6, 4.5, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(6.1, 4.3, "No", fontsize=10)
    
    # 条件2到结果2
    ax.arrow(7.5, 3, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(7.7, 3.1, "Yes", fontsize=10)
    
    # 条件2到Otherwise1
    ax.arrow(4.5, 3, -0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(4.3, 3.1, "No", fontsize=10)
    
    # Otherwise1到第二步计票
    ax.arrow(3, 3.6, 0, -1.3, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 第二步计票到条件3
    ax.arrow(3, 1.5, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 条件3到结果3
    ax.arrow(4.5, 0, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(4.7, 0.1, "Yes", fontsize=10)
    
    # 条件3到条件4
    ax.arrow(3, -0.5, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(3.1, -0.7, "No", fontsize=10)
    
    # 条件4到结果4
    ax.arrow(4.5, -2, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(4.7, -1.9, "Yes", fontsize=10)
    
    # 条件4到Otherwise2
    ax.arrow(1.5, -2, -0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(1.3, -1.9, "No", fontsize=10)
    
    # Otherwise2到第三步硬币
    ax.arrow(1, -1.4, 0, -1.8, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 第三步硬币到结果5
    ax.arrow(1, -4, 0, -0.2, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 调整图形大小以适应所有内容
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # 确保输出目录存在
    os.makedirs('/home/ubuntu/algorand_fix/latex/zh/images', exist_ok=True)
    os.makedirs('/home/ubuntu/algorand_fix/latex/en/images', exist_ok=True)
    
    # 保存图像
    plt.savefig('/home/ubuntu/algorand_fix/latex/zh/images/algorand_algorithm_fixed.png', dpi=300, bbox_inches='tight')
    plt.savefig('/home/ubuntu/algorand_fix/latex/en/images/algorand_algorithm_fixed.png', dpi=300, bbox_inches='tight')
    
    plt.close()

if __name__ == "__main__":
    create_algorand_algorithm_figure()

