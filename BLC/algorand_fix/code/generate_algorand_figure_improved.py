#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生成改进的Algorand算法图示
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as mpath
import numpy as np
import os

def create_algorand_algorithm_figure():
    # 创建图形和坐标轴
    fig, ax = plt.subplots(figsize=(10, 14))
    
    # 设置坐标轴范围
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    
    # 隐藏坐标轴
    ax.axis('off')
    
    # 定义颜色
    process_color = '#AED6F1'  # 浅蓝色
    decision_color = '#A9DFBF'  # 浅绿色
    result_color = '#FCF3CF'    # 浅黄色
    
    # 绘制算法流程图
    # 开始框
    start_box = patches.Rectangle((4, 13), 2, 0.8, linewidth=1, edgecolor='black', facecolor=process_color)
    ax.add_patch(start_box)
    ax.text(5, 13.4, "Start", ha='center', va='center', fontsize=12)
    
    # 第一步标题
    ax.text(5, 12.5, "Step 1", ha='center', va='center', fontsize=14, weight='bold')
    
    # 投票框
    vote_box = patches.Rectangle((4, 11.5), 2, 0.8, linewidth=1, edgecolor='black', facecolor=process_color)
    ax.add_patch(vote_box)
    ax.text(5, 11.9, "Vote $b_i$", ha='center', va='center', fontsize=12)
    
    # 计票框
    count_box = patches.Rectangle((4, 10.5), 2, 0.8, linewidth=1, edgecolor='black', facecolor=process_color)
    ax.add_patch(count_box)
    ax.text(5, 10.9, "Count #(0), #(1)", ha='center', va='center', fontsize=12)
    
    # 条件判断框1 - #(0) ≥ 2t+1?
    cond1_box = patches.Polygon([(5, 9.5), (6.5, 9), (5, 8.5), (3.5, 9)], linewidth=1, edgecolor='black', facecolor=decision_color)
    ax.add_patch(cond1_box)
    ax.text(5, 9, "#(0) ≥ 2t+1?", ha='center', va='center', fontsize=12)
    
    # 结果框1 - bi = 0, Terminate
    result1_box = patches.Rectangle((7, 8.6), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor=result_color)
    ax.add_patch(result1_box)
    ax.text(8.25, 9, "$b_i = 0$, Terminate", ha='center', va='center', fontsize=12)
    
    # 条件判断框2 - #(1) ≥ 2t+1?
    cond2_box = patches.Polygon([(5, 7.5), (6.5, 7), (5, 6.5), (3.5, 7)], linewidth=1, edgecolor='black', facecolor=decision_color)
    ax.add_patch(cond2_box)
    ax.text(5, 7, "#(1) ≥ 2t+1?", ha='center', va='center', fontsize=12)
    
    # 结果框2 - bi = 1, Terminate
    result2_box = patches.Rectangle((7, 6.6), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor=result_color)
    ax.add_patch(result2_box)
    ax.text(8.25, 7, "$b_i = 1$, Terminate", ha='center', va='center', fontsize=12)
    
    # 第一步Otherwise结果框 - bi = 0
    otherwise1_box = patches.Rectangle((0.5, 6.6), 2, 0.8, linewidth=1, edgecolor='black', facecolor=result_color)
    ax.add_patch(otherwise1_box)
    ax.text(1.5, 7, "$b_i = 0$", ha='center', va='center', fontsize=12)
    
    # 第二步标题
    ax.text(1.5, 5.7, "Step 2", ha='center', va='center', fontsize=14, weight='bold')
    
    # 第二步计票框
    count2_box = patches.Rectangle((0.5, 4.7), 2, 0.8, linewidth=1, edgecolor='black', facecolor=process_color)
    ax.add_patch(count2_box)
    ax.text(1.5, 5.1, "Count #(0), #(1)", ha='center', va='center', fontsize=12)
    
    # 第二步条件判断框1 - #(0) ≥ 2t+1?
    cond3_box = patches.Polygon([(1.5, 3.7), (3, 3.2), (1.5, 2.7), (0, 3.2)], linewidth=1, edgecolor='black', facecolor=decision_color)
    ax.add_patch(cond3_box)
    ax.text(1.5, 3.2, "#(0) ≥ 2t+1?", ha='center', va='center', fontsize=12)
    
    # 第二步结果框1 - bi = 0, Terminate
    result3_box = patches.Rectangle((3.5, 2.8), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor=result_color)
    ax.add_patch(result3_box)
    ax.text(4.75, 3.2, "$b_i = 0$, Terminate", ha='center', va='center', fontsize=12)
    
    # 第二步条件判断框2 - #(1) ≥ 2t+1?
    cond4_box = patches.Polygon([(1.5, 1.7), (3, 1.2), (1.5, 0.7), (0, 1.2)], linewidth=1, edgecolor='black', facecolor=decision_color)
    ax.add_patch(cond4_box)
    ax.text(1.5, 1.2, "#(1) ≥ 2t+1?", ha='center', va='center', fontsize=12)
    
    # 第二步结果框2 - bi = 1, Terminate
    result4_box = patches.Rectangle((3.5, 0.8), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor=result_color)
    ax.add_patch(result4_box)
    ax.text(4.75, 1.2, "$b_i = 1$, Terminate", ha='center', va='center', fontsize=12)
    
    # 第二步Otherwise结果框 - bi = 1
    otherwise2_box = patches.Rectangle((7, 0.8), 2, 0.8, linewidth=1, edgecolor='black', facecolor=result_color)
    ax.add_patch(otherwise2_box)
    ax.text(8, 1.2, "$b_i = 1$", ha='center', va='center', fontsize=12)
    
    # 第三步标题
    ax.text(8, 3.7, "Step 3", ha='center', va='center', fontsize=14, weight='bold')
    
    # 第三步硬币框
    coin_box = patches.Rectangle((7, 2.8), 2, 0.8, linewidth=1, edgecolor='black', facecolor=process_color)
    ax.add_patch(coin_box)
    ax.text(8, 3.2, "Common Coin $c$", ha='center', va='center', fontsize=12)
    
    # 第三步结果框 - bi = c, Terminate
    result5_box = patches.Rectangle((7, 4.7), 2.5, 0.8, linewidth=1, edgecolor='black', facecolor=result_color)
    ax.add_patch(result5_box)
    ax.text(8.25, 5.1, "$b_i = c$, Terminate", ha='center', va='center', fontsize=12)
    
    # 连接线和箭头
    # 开始到投票
    ax.arrow(5, 13, 0, -0.7, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 投票到计票
    ax.arrow(5, 11.5, 0, -0.2, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 计票到条件1
    ax.arrow(5, 10.5, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 条件1到结果1 (Yes)
    ax.arrow(6.5, 9, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(6.7, 9.2, "Yes", fontsize=10)
    
    # 条件1到条件2 (No)
    ax.arrow(5, 8.5, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(5.1, 8.3, "No", fontsize=10)
    
    # 条件2到结果2 (Yes)
    ax.arrow(6.5, 7, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(6.7, 7.2, "Yes", fontsize=10)
    
    # 条件2到Otherwise1 (No)
    ax.arrow(3.5, 7, -1, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(3.3, 7.2, "No", fontsize=10)
    
    # Otherwise1到第二步计票
    ax.arrow(1.5, 6.6, 0, -1.1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 第二步计票到条件3
    ax.arrow(1.5, 4.7, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 条件3到结果3 (Yes)
    ax.arrow(3, 3.2, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(3.2, 3.4, "Yes", fontsize=10)
    
    # 条件3到条件4 (No)
    ax.arrow(1.5, 2.7, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(1.6, 2.5, "No", fontsize=10)
    
    # 条件4到结果4 (Yes)
    ax.arrow(3, 1.2, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(3.2, 1.4, "Yes", fontsize=10)
    
    # 条件4到Otherwise2 (No) - 使用曲线
    # 创建曲线路径
    Path = mpath.Path
    path_data = [
        (Path.MOVETO, (0, 1.2)),
        (Path.CURVE4, (2, 1.5)),
        (Path.CURVE4, (5, 1.5)),
        (Path.CURVE4, (7, 1.2)),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = patches.PathPatch(path, facecolor='none', edgecolor='black', lw=1)
    ax.add_patch(patch)
    
    # 添加箭头
    arrow_head = patches.Polygon([(6.9, 1.2), (7.0, 1.3), (7.0, 1.1)], fc='black', ec='black')
    ax.add_patch(arrow_head)
    
    # 添加"No"标签
    ax.text(3, 1.7, "No", fontsize=10)
    
    # Otherwise2到第三步硬币
    ax.arrow(8, 1.6, 0, 1.2, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 第三步硬币到结果5
    ax.arrow(8, 3.6, 0, 1.1, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # 调整图形大小以适应所有内容
    plt.tight_layout()
    
    # 确保输出目录存在
    os.makedirs('/home/ubuntu/algorand_fix/latex/zh/images', exist_ok=True)
    os.makedirs('/home/ubuntu/algorand_fix/latex/en/images', exist_ok=True)
    os.makedirs('/home/ubuntu/algorand_fix/output', exist_ok=True)
    
    # 保存图像
    plt.savefig('/home/ubuntu/algorand_fix/latex/zh/images/algorand_algorithm_improved.png', dpi=300, bbox_inches='tight')
    plt.savefig('/home/ubuntu/algorand_fix/latex/en/images/algorand_algorithm_improved.png', dpi=300, bbox_inches='tight')
    plt.savefig('/home/ubuntu/algorand_fix/output/algorand_algorithm_improved.png', dpi=300, bbox_inches='tight')
    
    plt.close()

if __name__ == "__main__":
    create_algorand_algorithm_figure()

