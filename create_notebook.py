import nbformat as nbf

nb = nbf.v4.new_notebook()

# 创建所有单元格
cells = []

# 添加第一个markdown单元格（介绍）
cells.append(nbf.v4.new_markdown_cell('''# 强化学习基础作业：马尔科夫决策过程（MDP）

本次作业将帮助你理解和实现马尔科夫决策过程的基本概念。我们将通过一个简单的网格世界环境来实践MDP的核心组件。

## 学习目标
1. 理解MDP的五个基本要素：状态集、动作集、转移概率、奖励函数、折扣因子
2. 实现一个简单的网格世界环境
3. 计算状态价值函数和动作价值函数
4. 实现策略评估和策略改进

## 环境说明
我们将使用一个4x4的网格世界作为我们的环境：
- 智能体从起始位置(S)出发，目标是到达终点(G)
- 网格中有一些障碍物(#)和陷阱(T)
- 智能体可以采取上、下、左、右四个动作
- 到达目标获得+1奖励，掉入陷阱获得-1奖励，其他步骤获得-0.04奖励

```
S  .  .  .
.  #  .  .
.  .  T  G
.  T  .  .
```'''))

# 添加导入库的代码单元格
cells.append(nbf.v4.new_code_cell('''import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict
import random'''))

# 添加环境实现的markdown说明
cells.append(nbf.v4.new_markdown_cell('''## 第1部分：环境实现

首先，我们需要实现网格世界环境。这个环境需要包含以下功能：
1. 初始化网格世界
2. 定义状态转移函数
3. 定义奖励函数
4. 可视化功能

### 任务1.1：实现GridWorld类
请实现以下方法：
- `__init__`: 初始化网格世界的基本参数
- `get_next_state`: 根据当前状态和动作计算下一个状态
- `get_reward`: 根据状态返回奖励
- `is_terminal`: 判断是否为终止状态
- `get_all_states`: 获取所有可能的状态
- `visualize`: 可视化网格世界（可选择性地展示状态价值）'''))

# 添加GridWorld类的代码框架
cells.append(nbf.v4.new_code_cell('''class GridWorld:
    def __init__(self):
        """初始化网格世界环境"""
        # TODO: 实现初始化方法
        pass
    
    def get_next_state(self, state: Tuple[int, int], action: str) -> Tuple[int, int]:
        """根据当前状态和动作计算下一个状态"""
        # TODO: 实现状态转移函数
        pass
    
    def get_reward(self, state: Tuple[int, int]) -> float:
        """根据状态返回奖励"""
        # TODO: 实现奖励函数
        pass
    
    def is_terminal(self, state: Tuple[int, int]) -> bool:
        """判断是否为终止状态"""
        # TODO: 实现终止状态判断
        pass
    
    def get_all_states(self) -> List[Tuple[int, int]]:
        """获取所有可能的状态"""
        # TODO: 实现获取所有状态的方法
        pass
    
    def visualize(self, values: Dict[Tuple[int, int], float] = None):
        """可视化网格世界，可选择性地展示状态价值"""
        # TODO: 实现可视化方法
        pass'''))

# 添加测试环境的markdown说明
cells.append(nbf.v4.new_markdown_cell('''### 任务1.2：测试环境

创建环境实例并测试基本功能：
1. 创建GridWorld实例
2. 测试可视化功能
3. 测试状态转移和奖励计算'''))

# 添加测试环境的代码单元格
cells.append(nbf.v4.new_code_cell('''# TODO: 创建环境实例并测试基本功能
env = GridWorld()

# 测试代码...'''))

# 添加策略评估的markdown说明
cells.append(nbf.v4.new_markdown_cell('''## 第2部分：策略评估

接下来，我们将实现策略评估算法。给定一个策略π，我们需要计算该策略下的状态价值函数V_π。

策略评估的更新公式为：

V_π(s) = Σ_a π(a|s) Σ_s' P(s'|s,a)[R(s,a,s') + γV_π(s')]

在我们的简化版本中：
- π是均匀随机策略（每个动作的概率相等）
- P是确定性的（transition_prob = 1.0）
- γ (gamma) 设为0.9

### 任务2.1：实现策略评估算法'''))

# 添加策略评估的代码单元格
cells.append(nbf.v4.new_code_cell('''def policy_evaluation(env: GridWorld, gamma: float = 0.9, theta: float = 1e-6) -> Dict[Tuple[int, int], float]:
    """
    策略评估：计算均匀随机策略下的状态价值函数
    
    参数：
        env: 网格世界环境
        gamma: 折扣因子
        theta: 收敛阈值
    
    返回：
        状态价值函数字典 {state: value}
    """
    # TODO: 实现策略评估算法
    pass'''))

# 添加运行策略评估的markdown说明
cells.append(nbf.v4.new_markdown_cell('''### 任务2.2：测试策略评估

使用策略评估算法计算均匀随机策略下的状态价值函数，并可视化结果。'''))

# 添加运行策略评估的代码单元格
cells.append(nbf.v4.new_code_cell('''# TODO: 运行策略评估并可视化结果'''))

# 添加最优策略的markdown说明
cells.append(nbf.v4.new_markdown_cell('''## 第3部分：最优策略

现在，我们将实现价值迭代算法来找到最优策略。价值迭代的更新公式为：

V*(s) = max_a Σ_s' P(s'|s,a)[R(s,a,s') + γV*(s')]

### 任务3.1：实现价值迭代算法'''))

# 添加价值迭代的代码单元格
cells.append(nbf.v4.new_code_cell('''def value_iteration(env: GridWorld, gamma: float = 0.9, theta: float = 1e-6) -> Tuple[Dict[Tuple[int, int], float], Dict[Tuple[int, int], str]]:
    """
    价值迭代算法
    
    参数：
        env: 网格世界环境
        gamma: 折扣因子
        theta: 收敛阈值
    
    返回：
        (最优价值函数, 最优策略)
    """
    # TODO: 实现价值迭代算法
    pass'''))

# 添加运行价值迭代的markdown说明
cells.append(nbf.v4.new_markdown_cell('''### 任务3.2：测试价值迭代

使用价值迭代算法找到最优策略，并可视化结果。'''))

# 添加运行价值迭代的代码单元格
cells.append(nbf.v4.new_code_cell('''# TODO: 运行价值迭代并可视化结果'''))

# 添加策略执行的markdown说明
cells.append(nbf.v4.new_markdown_cell('''## 第4部分：策略执行

### 任务4.1：实现策略执行和可视化
实现以下功能：
1. 执行给定的策略并记录轨迹
2. 可视化智能体的运动轨迹'''))

# 添加策略执行的代码单元格
cells.append(nbf.v4.new_code_cell('''def execute_policy(env: GridWorld, policy: Dict[Tuple[int, int], str], max_steps: int = 100) -> List[Tuple[int, int]]:
    """执行给定的策略并返回轨迹"""
    # TODO: 实现策略执行
    pass

def visualize_trajectory(env: GridWorld, trajectory: List[Tuple[int, int]]):
    """可视化智能体的运动轨迹"""
    # TODO: 实现轨迹可视化
    pass'''))

# 添加执行最优策略的代码单元格
cells.append(nbf.v4.new_code_cell('''# TODO: 执行最优策略并可视化轨迹'''))

# 添加思考题
cells.append(nbf.v4.new_markdown_cell('''## 思考题

1. 为什么最优策略下的轨迹会选择这条路径？请结合奖励设置和折扣因子进行分析。

2. 如果我们改变折扣因子γ的值（比如设为0.5或0.99），最优策略会有什么变化？为什么？

3. 在当前的设置下，为什么有些状态的价值是负的？这些负价值状态对最优策略有什么影响？

4. 如果我们想让智能体更倾向于选择更短的路径到达目标，应该如何修改奖励函数？请给出具体的修改建议。'''))

# 设置notebook的metadata
nb.metadata = {
    'kernelspec': {
        'display_name': 'Python (RL)',
        'language': 'python',
        'name': 'rl_env'
    },
    'language_info': {
        'codemirror_mode': {
            'name': 'ipython',
            'version': 3
        },
        'file_extension': '.py',
        'mimetype': 'text/x-python',
        'name': 'python',
        'nbconvert_exporter': 'python',
        'pygments_lexer': 'ipython3',
        'version': '3.9.0'
    }
}

# 将所有单元格添加到notebook中
nb.cells = cells

# 保存notebook
with open('assignment/MDP_assignment.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f) 