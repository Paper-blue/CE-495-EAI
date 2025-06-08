#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生成重置策略结论表格
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def create_reset_strategy_table():
    # 定义表格数据
    data = {
        'Strategy': ['basic', 'lag', 'probability', 'time', 'dynamic'],
        'Avg Time': [11.76, 12.69, 10.24, 13.36, 11.90],
        'Median Time': [9.54, 11.88, 9.25, 10.75, 11.79],
        'Min Time': [4.16, 3.99, 8.21, 4.20, 7.32],
        'Max Time': [23.69, 19.20, 16.30, 42.12, 17.41],
        'Std Dev': [5.29, 5.26, 2.78, 8.70, 2.21],
        'Success Rate': [0.21, 0.06, 0.06, 0.24, 0.21]
    }
    
    # 创建DataFrame
    df = pd.DataFrame(data)
    
    # 设置索引
    df.set_index('Strategy', inplace=True)
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 隐藏坐标轴
    ax.axis('off')
    
    # 创建表格
    table = ax.table(
        cellText=df.reset_index().values,
        colLabels=['Strategy', 'Avg Time', 'Median Time', 'Min Time', 'Max Time', 'Std Dev', 'Success Rate'],
        cellLoc='center',
        loc='center',
        bbox=[0, 0, 1, 1]
    )
    
    # 设置表格样式
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5)
    
    # 设置标题行样式
    for i, key in enumerate(table._cells):
        if key[0] == 0:  # 标题行
            cell = table._cells[key]
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#4472C4')
    
    # 设置交替行颜色
    for i in range(1, len(df) + 1):
        for j in range(len(df.columns) + 1):
            cell = table._cells[(i, j)]
            if i % 2 == 0:
                cell.set_facecolor('#D9E1F2')
            else:
                cell.set_facecolor('#E9EDF4')
    
    # 确保输出目录存在
    os.makedirs('/home/ubuntu/algorand_fix/latex/zh/images', exist_ok=True)
    os.makedirs('/home/ubuntu/algorand_fix/latex/en/images', exist_ok=True)
    os.makedirs('/home/ubuntu/algorand_fix/output', exist_ok=True)
    
    # 保存图像
    plt.savefig('/home/ubuntu/algorand_fix/latex/zh/images/reset_strategy_table.png', dpi=300, bbox_inches='tight')
    plt.savefig('/home/ubuntu/algorand_fix/latex/en/images/reset_strategy_table.png', dpi=300, bbox_inches='tight')
    plt.savefig('/home/ubuntu/algorand_fix/output/reset_strategy_table.png', dpi=300, bbox_inches='tight')
    
    plt.close()
    
    # 创建LaTeX表格代码
    latex_table = """
\\begin{table}[h]
\\centering
\\begin{tabular}{|l|c|c|c|c|c|c|}
\\hline
\\textbf{Strategy} & \\textbf{Avg Time} & \\textbf{Median Time} & \\textbf{Min Time} & \\textbf{Max Time} & \\textbf{Std Dev} & \\textbf{Success Rate} \\\\
\\hline
basic & 11.76 & 9.54 & 4.16 & 23.69 & 5.29 & 0.21 \\\\
\\hline
lag & 12.69 & 11.88 & 3.99 & 19.20 & 5.26 & 0.06 \\\\
\\hline
probability & 10.24 & 9.25 & 8.21 & 16.30 & 2.78 & 0.06 \\\\
\\hline
time & 13.36 & 10.75 & 4.20 & 42.12 & 8.70 & 0.24 \\\\
\\hline
dynamic & 11.90 & 11.79 & 7.32 & 17.41 & 2.21 & 0.21 \\\\
\\hline
\\end{tabular}
\\caption{Comparison of Different Reset Strategies}
\\label{tab:reset_strategies}
\\end{table}
"""
    
    # 保存LaTeX表格代码
    with open('/home/ubuntu/algorand_fix/output/reset_strategy_table.tex', 'w') as f:
        f.write(latex_table)
    
    print("重置策略表格已生成")

if __name__ == "__main__":
    create_reset_strategy_table()

