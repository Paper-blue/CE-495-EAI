#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用weasyprint生成修复后的中文PDF文档V3
"""

from weasyprint import HTML
import os

def create_chinese_pdf():
    # 创建HTML内容
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>区块链共识算法作业（修复版V3）</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }
            h1 {
                text-align: center;
                margin-bottom: 30px;
            }
            h2 {
                margin-top: 30px;
                border-bottom: 1px solid #ddd;
                padding-bottom: 5px;
            }
            h3 {
                margin-top: 20px;
            }
            p {
                margin-bottom: 15px;
            }
            .figure {
                text-align: center;
                margin: 20px 0;
            }
            .figure img {
                max-width: 80%;
            }
            .figure .caption {
                font-style: italic;
                margin-top: 10px;
            }
            pre {
                background-color: #f5f5f5;
                padding: 10px;
                border-radius: 5px;
                overflow-x: auto;
            }
        </style>
    </head>
    <body>
        <h1>区块链共识算法作业（修复版V3）</h1>
        
        <h2>问题1：Algorand算法 (20分)</h2>
        
        <p>考虑一个由n = 3t + 1个节点组成的委员会，其中t个节点是恶意的，剩余的2t + 1个节点是诚实的。每个节点以一个单比特开始。令bi表示节点i的比特。诚实节点执行共识算法。恶意节点可能以任意方式偏离算法，包括被单个攻击者指导。节点在算法的每一轮中更新它们的bi。我们希望共识算法对所有诚实节点终止，并满足：</p>
        
        <ul>
            <li>一致性：所有诚实节点的比特相同。</li>
            <li>一致性：如果所有诚实节点以相同的比特开始，则它们以相同的比特结束。</li>
        </ul>
        
        <p>考虑课堂上讨论的Algorand共识算法（第19讲），如图1所示。节点i记录它收到的0票数为#(0)和1票数为#(1)（包括自己的票）。</p>
        
        <div class="figure">
            <img src="../output/algorand_algorithm_improved.png" alt="Algorand共识算法">
            <div class="caption">图1：Algorand共识算法</div>
        </div>
        
        <p>使用t = 3（因此n = 10）模拟该过程。</p>
        
        <h3>随机初始化</h3>
        
        <p>让所有节点的比特随机初始化。恶意节点不应计票，而是简单地为随机比特投票。执行共识协议。输出每轮中所有10个节点的比特，直到所有诚实节点终止。标记每个节点终止的位置。简要解释输出。</p>
        
        <h4>模拟结果</h4>
        
        <p>我们使用Python实现了Algorand共识算法的模拟，严格遵循图1所示的多步骤过程。在随机初始化的情况下，模拟结果如下：</p>
        
        <pre>
轮次	节点比特值			终止状态			步骤			投票[0,1]	公共硬币
0	0010001(0)(1)(1)	FFFFFFFFFF	1111111(1)(1)(1)	[0, 0]	None
1	0000000(0)(1)(0)	FFFFFFFFTT	2222222(1)(1)(1)	[6, 4]	1
2	0000000(1)(1)(0)	TTTTTTTTTT	2222222(1)(1)(1)	[7, 1]	0
所有诚实节点是否达成一致: True
        </pre>
        
        <p>在上述输出中：</p>
        <ul>
            <li>第一列表示轮次，从0开始（初始状态）。</li>
            <li>第二列表示每个节点的比特值，前7个是诚实节点，后3个是恶意节点（用括号标记）。</li>
            <li>第三列表示每个节点是否已终止，"T"表示已终止，"F"表示未终止。</li>
            <li>第四列表示每个节点当前所处的步骤（1, 2, 或 3）。</li>
            <li>第五列表示该轮的投票结果，[0票数, 1票数]。</li>
            <li>第六列表示该轮使用的公共硬币值（如果适用）。</li>
        </ul>
        
        <h4>结果分析</h4>
        
        <p>在初始状态（轮次0）中，7个诚实节点的比特值随机初始化为"0010001"，3个恶意节点的比特值随机初始化为"011"。所有节点都处于第1步，未终止。</p>
        
        <p>在第1轮中，所有节点进行投票。根据算法，诚实节点投票自己当前的比特值，而恶意节点随机投票。计票结果为[6, 4]，表示有6票投给0，4票投给1。</p>
        
        <p>由于t=3，终止条件为2t+1 = 7。由于#(0)=6 < 7且#(1)=4 < 7，没有达到第一步的终止条件。根据第一步的"otherwise"规则，所有诚实节点将比特值更新为0，并进入第2步。两个恶意节点随机终止。</p>
        
        <p>在第2轮中，投票结果为[7, 1]，表示有7票投给0，1票投给1。由于#(0)=7 = 2t+1，达到了第二步的终止条件。所有诚实节点保持比特值为0并终止。此时所有节点都已终止。</p>
        
        <p>最终，所有诚实节点成功达成一致，比特值均为0。这表明Algorand算法在存在恶意节点的情况下仍能有效地达成共识。</p>
        
        <h3>诚实节点初始化为0</h3>
        
        <p>将所有诚实节点的比特初始化为0。重复第1部分。</p>
        
        <h4>模拟结果</h4>
        
        <p>在所有诚实节点初始化为0的情况下，模拟结果如下：</p>
        
        <pre>
轮次	节点比特值			终止状态			步骤			投票[0,1]	公共硬币
0	0000000(1)(0)(0)	FFFFFFFFFF	1111111(1)(1)(1)	[0, 0]	None
1	0000000(0)(0)(0)	TTTTTTTTFT	1111111(1)(2)(1)	[8, 2]	1
所有诚实节点是否达成一致: True
        </pre>
        
        <h4>结果分析</h4>
        
        <p>在初始状态（轮次0）中，所有7个诚实节点的比特值都初始化为0，3个恶意节点的比特值随机初始化为"100"。所有节点都处于第1步，未终止。</p>
        
        <p>在第1轮中，所有节点进行投票。诚实节点投票自己当前的比特值（全为0），而恶意节点随机投票。计票结果为[8, 2]，表示有8票投给0，2票投给1。</p>
        
        <p>由于t=3，终止条件为2t+1 = 7。由于#(0)=8 > 7，达到了第一步的终止条件。所有诚实节点保持比特值为0并终止。大部分恶意节点也终止，只有一个进入第2步。</p>
        
        <p>最终，所有诚实节点成功达成一致，比特值均为0。这验证了Algorand算法的一致性属性：如果所有诚实节点以相同的比特开始，则它们以相同的比特结束。</p>
        
        <h3>算法实现说明</h3>
        
        <p>我们的实现严格遵循了图1所示的Algorand共识算法的多步骤过程：</p>
        
        <ol>
            <li><strong>第一步</strong>：
                <ul>
                    <li>节点计算收到的0票数 #(0) 和1票数 #(1)</li>
                    <li>如果 #(0) ≥ 2t+1，则节点设置 bi=0 并终止</li>
                    <li>如果 #(1) ≥ 2t+1，则节点设置 bi=1 并终止</li>
                    <li>否则（otherwise），节点设置 bi=0 并进入第二步</li>
                </ul>
            </li>
            <li><strong>第二步</strong>：
                <ul>
                    <li>节点再次计算收到的0票数 #(0) 和1票数 #(1)</li>
                    <li>如果 #(0) ≥ 2t+1，则节点设置 bi=0 并终止</li>
                    <li>如果 #(1) ≥ 2t+1，则节点设置 bi=1 并终止</li>
                    <li>否则（otherwise），节点设置 bi=1 并进入第三步</li>
                </ul>
            </li>
            <li><strong>第三步</strong>：
                <ul>
                    <li>节点使用公共硬币 c</li>
                    <li>节点设置 bi=c 并终止</li>
                </ul>
            </li>
        </ol>
        
        <p>这种多步骤的设计确保了算法在各种条件下的正确行为，而不仅仅是在特定的初始条件和投票模式下。</p>
        
        <h2>问题2：最快违规 (50分)</h2>
        
        <p>在这个问题中，我们研究最长链分叉选择规则的安全性。问题是：假设攻击者从时间0开始攻击系统，即在创世区块被挖掘后立即开始，创建第一个安全违规的最小预期时间或挖掘的区块数是多少？</p>
        
        <h3>基本问题的清晰简洁表述</h3>
        
        <p>基本问题可以表述如下：</p>
        
        <p>在工作量证明的区块链系统中，考虑一个攻击者从创世区块开始进行私有挖掘攻击，目标是创造安全违规。系统中有诚实矿工（挖掘率为h）和恶意矿工（挖掘率为a），且满足1/a > 1/h + Δ，其中Δ是区块传播延迟（在基本问题中Δ = 0）。</p>
        
        <p>攻击者可以采用带重置的私有挖掘策略：从创世区块开始挖掘私有链，并可以在任何时间点将基础区块重置为最高的诚实区块，然后在新基础上开始挖掘新的私有链。攻击目标是基础区块的第一个诚实子区块。</p>
        
        <p>当目标区块在公共链中至少为k深，且包含当前基础的私有链是最长链时，安全违规发生。</p>
        
        <p>问题是：设计一个重置策略，使得从时间0开始到第一次安全违规发生的预期时间最小。</p>
        
        <h3>设计重置策略以保证违规</h3>
        
        <p>为了保证违规，我们设计了几种不同的重置策略，并通过模拟比较它们的性能：</p>
        
        <ol>
            <li><strong>基本策略（不重置）</strong>：从创世区块开始挖掘私有链，不进行重置。</li>
            <li><strong>基于落后程度的重置策略</strong>：当私有链落后公共链超过一定阈值（如3个区块）时重置。</li>
            <li><strong>基于概率的重置策略</strong>：每次检查时以一定概率（如0.1）重置。</li>
            <li><strong>基于时间的重置策略</strong>：每隔一定时间（如50个时间单位）重置一次。</li>
            <li><strong>动态调整策略</strong>：结合多种因素动态决定是否重置：
                <ul>
                    <li>如果私有链落后太多（如5个区块），立即重置</li>
                    <li>如果目标区块接近k确认，不重置</li>
                    <li>否则，以较低概率（如0.05）重置</li>
                </ul>
            </li>
        </ol>
        
        <p>我们使用Python实现了这些策略的模拟，参数设置为a = 0.3，h = 0.7，k = 5，运行了100次模拟。模拟结果如下表所示：</p>
        
        <div class="figure">
            <img src="../output/reset_strategy_table.png" alt="不同重置策略的比较">
            <div class="caption">图2：不同重置策略的比较</div>
        </div>
        
        <p>从结果可以看出，基于概率的重置策略在平均时间上表现最好（10.24），但成功率较低（0.06）。基于时间的重置策略成功率最高（0.24），但平均时间较长（13.36）。动态调整策略在成功率（0.21）和稳定性（标准差2.21）方面表现较好。</p>
        
        <h3>设计最优重置策略</h3>
        
        <p>设计最优重置策略的目标是使第一次违规的预期时间尽可能小。基于我们的模拟结果和理论分析，我们提出以下优化方向：</p>
        
        <h4>理论分析</h4>
        
        <p>从理论上讲，最优重置策略应该考虑以下因素：</p>
        
        <ol>
            <li><strong>公私链长度差距</strong>：当私有链落后公共链太多时，继续在当前基础上挖掘成功概率很低，应该重置。</li>
            <li><strong>目标区块确认深度</strong>：如果目标区块接近k确认，且私有链有赶上公共链的可能，应该坚持当前攻击而不重置。</li>
            <li><strong>挖掘率比例</strong>：a/h的比值影响攻击成功的概率，当a接近h时，不重置的策略可能更有效。</li>
            <li><strong>已投入时间</strong>：考虑已经投入的挖掘时间，避免过早放弃有希望的攻击。</li>
        </ol>
        
        <h4>马尔可夫决策过程方法</h4>
        
        <p>一个更系统的方法是将问题建模为马尔可夫决策过程（MDP）：</p>
        
        <ul>
            <li><strong>状态</strong>：(l_h, l_a, d)，其中l_h是公共链长度，l_a是私有链长度，d是目标区块在公共链中的深度。</li>
            <li><strong>动作</strong>：继续当前攻击或重置基础区块。</li>
            <li><strong>转移概率</strong>：基于a和h计算下一个区块由谁挖出的概率。</li>
            <li><strong>奖励</strong>：当违规发生时为正值，其他情况为负值（表示时间成本）。</li>
        </ul>
        
        <p>通过值迭代或策略迭代算法，可以求解最优策略。但这需要离散化连续时间模型，增加了计算复杂性。</p>
        
        <h4>强化学习方法</h4>
        
        <p>另一种方法是使用强化学习，特别是Q-learning或深度Q网络（DQN）来学习最优策略：</p>
        
        <ul>
            <li>智能体通过与环境交互学习最优策略</li>
            <li>状态表示为公私链长度、目标深度等特征</li>
            <li>奖励设计为违规发生时的正奖励减去时间成本</li>
        </ul>
        
        <p>这种方法的优势是可以处理大状态空间，并且不需要精确的环境模型。</p>
        
        <h4>实际挑战</h4>
        
        <p>在实际实现最优重置策略时，我们面临以下挑战：</p>
        
        <ol>
            <li><strong>状态空间爆炸</strong>：随着链长增加，状态空间呈指数增长。</li>
            <li><strong>模型精度</strong>：实际区块链网络中的挖掘过程可能不完全符合指数分布假设。</li>
            <li><strong>参数敏感性</strong>：最优策略对a、h、k等参数非常敏感。</li>
            <li><strong>计算复杂性</strong>：求解精确的最优策略计算开销很大。</li>
        </ol>
        
        <h4>改进的动态策略</h4>
        
        <p>基于上述分析，我们提出一个改进的动态重置策略：</p>
        
        <ol>
            <li>当l_h - l_a > α · √l_h时重置（α是可调参数）</li>
            <li>当目标区块深度d > β · k且l_a > γ · l_h时不重置（β、γ是可调参数）</li>
            <li>根据当前状态动态调整重置概率：p_reset = min(1, max(0, (l_h - l_a - δ)/l_h))</li>
        </ol>
        
        <p>这个策略结合了确定性规则和随机性，可以适应不同的网络状态，有望在平均情况下获得更好的性能。</p>
        
        <h2>总结</h2>
        
        <p>在本作业中，我们研究了两个区块链共识相关的问题：</p>
        
        <ol>
            <li>通过模拟验证了Algorand共识算法在存在恶意节点的情况下仍能有效达成共识，并满足一致性属性。我们严格遵循了作业中描述的多步骤过程，包括正确的终止条件和公共硬币机制。</li>
            <li>分析了区块链中最快违规问题，设计并比较了多种重置策略，提出了理论上的最优策略框架。</li>
        </ol>
        
        <p>我们的研究表明，在区块链安全性分析中，理论分析和计算机模拟相结合的方法是非常有效的。未来工作可以进一步探索强化学习在优化攻击策略中的应用，以及考虑更复杂的网络模型（如非零传播延迟）对安全性的影响。</p>
    </body>
    </html>
    """
    
    # 确保输出目录存在
    os.makedirs('/home/ubuntu/algorand_fix/output', exist_ok=True)
    
    # 创建临时HTML文件
    html_path = '/home/ubuntu/algorand_fix/output/temp.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 转换HTML为PDF
    output_path = '/home/ubuntu/algorand_fix/output/assignment_zh_fixed_v3.pdf'
    HTML(html_path).write_pdf(output_path)
    
    # 删除临时HTML文件
    os.remove(html_path)
    
    print(f"修复后的中文PDF V3已生成: {output_path}")

if __name__ == "__main__":
    create_chinese_pdf()

