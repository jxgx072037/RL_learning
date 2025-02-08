import nbformat as nbf

nb = nbf.v4.new_notebook()

# 添加markdown单元格
markdown_cell = nbf.v4.new_markdown_cell('''# 强化学习基础知识练习

本练习将帮助您理解和实践强化学习的基础概念。我们将从简单的马尔科夫链开始，逐步深入到MRP和MDP。

## 准备工作''')

# 添加代码单元格
code_cell = nbf.v4.new_code_cell('''import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子以确保结果可重现
np.random.seed(42)''')

# 添加更多markdown单元格
task1_cell = nbf.v4.new_markdown_cell('''## 练习1：马尔科夫链

### 任务1.1：实现状态转移
创建一个简单的天气系统，包含三个状态：晴天(0)、多云(1)、雨天(2)

1. 创建状态转移矩阵
2. 实现一个函数，模拟状态转移过程
3. 记录并显示状态转移序列''')

# 添加任务代码单元格
task1_code_cell = nbf.v4.new_code_cell('''# 定义状态转移矩阵
P = np.array([
    [0.7, 0.2, 0.1],  # 晴天的转移概率
    [0.3, 0.4, 0.3],  # 多云的转移概率
    [0.2, 0.3, 0.5]   # 雨天的转移概率
])

def simulate_markov_chain(P, start_state, n_steps):
    """模拟马尔科夫链状态转移
    
    参数：
        P: 状态转移矩阵
        start_state: 初始状态
        n_steps: 模拟步数
        
    返回：
        状态序列
    """
    # 在这里实现函数
    pass

# 测试代码
# states = simulate_markov_chain(P, start_state=0, n_steps=10)
# print("状态序列:", states)''')

# 将单元格添加到notebook中
nb.cells = [markdown_cell, code_cell, task1_cell, task1_code_cell]

# 保存notebook
with open('assignment/RL_basics_assignment.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f) 