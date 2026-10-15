# MNIST 手写数字识别实验记录

## 项目简介

用 PyTorch 在 MNIST 数据集上训练手写数字识别模型，并系统记录不同超参数对准确率的影响。

## 环境

- Python 3.10
- PyTorch 2.x
- 设备：NVIDIA RTX 4060（拯救者 R7000）

## 项目结构

```
mnist-project/
├── configs.py              # 实验配置
├── model.py                # 模型定义
├── train.py                # 训练逻辑
├── run_experiments.py      # 运行实验 + 记录结果
├── view_results.py         # 查看结果 + 导出 Markdown
└── experiments.csv         # 实验结果表
```

## 如何运行

```bash
pip install -r requirements.txt
python run_experiments.py
python view_results.py
```

## 实验结果

| name | model_type | hidden_size | learning_rate | optimizer | epochs | best_accuracy | training_time_sec | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cnn_baseline | cnn | 128 | 0.001 | adam | 5 | 0.9912 | 85.3 | 换成 CNN |
| fc_hidden_256 | fc | 256 | 0.001 | adam | 5 | 0.9780 | 42.1 | 隐藏层 256 |
| baseline_fc_128_adam_0.001 | fc | 128 | 0.001 | adam | 5 | 0.9720 | 40.5 | 基线 |

## 结论

- CNN 明显优于全连接网络，准确率提升约 2%
- 隐藏层从 128 增加到 256，准确率有小幅提升
- 学习率 0.01 对 Adam 过大，0.0001 收敛太慢

## 后续改进

- 加入数据增强
- 加入 BatchNorm 和 Dropout
- 尝试更深的 CNN