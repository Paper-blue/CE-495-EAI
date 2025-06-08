#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
修复后的Algorand共识算法模拟
严格遵循作业中描述的多步骤过程
"""

import random
import numpy as np
import matplotlib.pyplot as plt

class AlgorandSimulation:
    def __init__(self, t=3):
        """
        初始化Algorand模拟
        
        参数:
        t: 恶意节点数量，总节点数为n = 3t + 1
        """
        self.t = t
        self.n = 3 * t + 1
        self.honest_nodes = 2 * t + 1
        self.adversarial_nodes = t
        self.bits = [0] * self.n  # 所有节点的比特值
        self.terminated = [False] * self.n  # 节点是否已终止
        self.step = [1] * self.n  # 每个节点当前所处的步骤（1, 2, 或 3）
    
    def initialize_random(self):
        """随机初始化所有节点的比特值"""
        for i in range(self.n):
            self.bits[i] = random.randint(0, 1)
        self.terminated = [False] * self.n
        self.step = [1] * self.n
    
    def initialize_honest_zero(self):
        """将所有诚实节点的比特值初始化为0，恶意节点随机初始化"""
        for i in range(self.honest_nodes):
            self.bits[i] = 0
        for i in range(self.honest_nodes, self.n):
            self.bits[i] = random.randint(0, 1)
        self.terminated = [False] * self.n
        self.step = [1] * self.n
    
    def generate_common_coin(self):
        """生成公共硬币值（0或1）"""
        return random.randint(0, 1)
    
    def run_round(self):
        """执行一轮共识算法"""
        # 收集所有节点的投票
        votes = [0, 0]  # [票数0, 票数1]
        
        # 诚实节点投票
        for i in range(self.honest_nodes):
            if not self.terminated[i]:
                votes[self.bits[i]] += 1
        
        # 恶意节点随机投票
        for i in range(self.honest_nodes, self.n):
            if not self.terminated[i]:
                # 恶意节点随机投票
                adversarial_vote = random.randint(0, 1)
                votes[adversarial_vote] += 1
        
        # 生成公共硬币（如果需要）
        common_coin = self.generate_common_coin()
        
        # 诚实节点根据当前步骤更新比特值
        for i in range(self.honest_nodes):
            if not self.terminated[i]:
                if self.step[i] == 1:
                    # 第一步
                    if votes[0] >= 2*self.t + 1:
                        self.bits[i] = 0
                        self.terminated[i] = True
                    elif votes[1] >= 2*self.t + 1:
                        self.bits[i] = 1
                        self.terminated[i] = True
                    else:
                        # otherwise
                        self.bits[i] = 0
                        self.step[i] = 2
                elif self.step[i] == 2:
                    # 第二步
                    if votes[0] >= 2*self.t + 1:
                        self.bits[i] = 0
                        self.terminated[i] = True
                    elif votes[1] >= 2*self.t + 1:
                        self.bits[i] = 1
                        self.terminated[i] = True
                    else:
                        # otherwise
                        self.bits[i] = 1
                        self.step[i] = 3
                elif self.step[i] == 3:
                    # 第三步 - 使用公共硬币
                    self.bits[i] = common_coin
                    self.terminated[i] = True
        
        # 恶意节点随机更新比特值和步骤
        for i in range(self.honest_nodes, self.n):
            if not self.terminated[i]:
                self.bits[i] = random.randint(0, 1)
                # 随机决定是否终止或进入下一步
                action = random.choice(["terminate", "next_step", "stay"])
                if action == "terminate":
                    self.terminated[i] = True
                elif action == "next_step" and self.step[i] < 3:
                    self.step[i] += 1
        
        return votes, common_coin
    
    def all_honest_terminated(self):
        """检查所有诚实节点是否都已终止"""
        return all(self.terminated[:self.honest_nodes])
    
    def honest_agreement(self):
        """检查所有诚实节点是否达成一致"""
        if not self.all_honest_terminated():
            return False
        
        first_bit = self.bits[0]
        for i in range(1, self.honest_nodes):
            if self.bits[i] != first_bit:
                return False
        return True
    
    def simulate(self, max_rounds=20):
        """
        模拟Algorand共识过程
        
        参数:
        max_rounds: 最大轮数
        
        返回:
        rounds_data: 每轮的节点比特值、终止状态和步骤
        """
        rounds_data = []
        
        # 记录初始状态
        rounds_data.append({
            'round': 0,
            'bits': self.bits.copy(),
            'terminated': self.terminated.copy(),
            'step': self.step.copy(),
            'votes': [0, 0],
            'common_coin': None
        })
        
        for r in range(1, max_rounds + 1):
            votes, common_coin = self.run_round()
            
            # 记录本轮状态
            rounds_data.append({
                'round': r,
                'bits': self.bits.copy(),
                'terminated': self.terminated.copy(),
                'step': self.step.copy(),
                'votes': votes,
                'common_coin': common_coin
            })
            
            # 如果所有诚实节点都已终止，结束模拟
            if self.all_honest_terminated():
                break
        
        return rounds_data

def print_simulation_results(rounds_data, honest_nodes):
    """打印模拟结果"""
    print("轮次\t节点比特值\t\t\t终止状态\t\t\t步骤\t\t\t投票[0,1]\t公共硬币")
    for data in rounds_data:
        bits_str = ''.join(map(str, data['bits']))
        term_str = ''.join(['T' if t else 'F' for t in data['terminated']])
        step_str = ''.join(map(str, data['step']))
        
        # 标记诚实节点和恶意节点
        marked_bits = ''
        for i, bit in enumerate(bits_str):
            if i < honest_nodes:
                marked_bits += bit
            else:
                marked_bits += f"({bit})"
        
        # 标记步骤
        marked_steps = ''
        for i, step in enumerate(step_str):
            if i < honest_nodes:
                marked_steps += step
            else:
                marked_steps += f"({step})"
        
        coin_str = str(data['common_coin']) if data['common_coin'] is not None else "None"
        print(f"{data['round']}\t{marked_bits}\t{term_str}\t{marked_steps}\t{data['votes']}\t{coin_str}")

def main():
    # 问题1.1: 随机初始化
    print("问题1.1: 随机初始化所有节点的比特值")
    sim1 = AlgorandSimulation(t=3)
    sim1.initialize_random()
    rounds_data1 = sim1.simulate()
    print_simulation_results(rounds_data1, sim1.honest_nodes)
    print(f"所有诚实节点是否达成一致: {sim1.honest_agreement()}")
    print()
    
    # 问题1.2: 诚实节点初始化为0
    print("问题1.2: 将所有诚实节点的比特值初始化为0")
    sim2 = AlgorandSimulation(t=3)
    sim2.initialize_honest_zero()
    rounds_data2 = sim2.simulate()
    print_simulation_results(rounds_data2, sim2.honest_nodes)
    print(f"所有诚实节点是否达成一致: {sim2.honest_agreement()}")

if __name__ == "__main__":
    main()

