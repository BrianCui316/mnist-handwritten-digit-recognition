# configs.py

# 每个实验是一个字典，包含：
#   name          实验唯一名字（用来去重，不要重复）
#   model_type    模型类型：fc / fc_deep / cnn
#   hidden_size   隐藏层大小
#   learning_rate 学习率
#   optimizer     优化器：adam / sgd / adamw
#   batch_size    批大小
#   epochs        训练轮数
#   seed          随机种子（保证可复现）
#   notes         备注（写你改了啥）

EXPERIMENTS = [
    # ---------- 基线 ----------
    {
        "name": "baseline_fc_128_adam_0.001",
        "model_type": "fc",
        "hidden_size": 128,
        "learning_rate": 0.001,
        "optimizer": "adam",
        "batch_size": 64,
        "epochs": 5,
        "seed": 42,
        "notes": "基线：全连接 + 128 隐藏层 + Adam",
    },

    # ---------- 改隐藏层大小 ----------
    {
        "name": "fc_hidden_256",
        "model_type": "fc",
        "hidden_size": 256,
        "learning_rate": 0.001,
        "optimizer": "adam",
        "batch_size": 64,
        "epochs": 5,
        "seed": 42,
        "notes": "隐藏层从 128 改到 256",
    },
    {
        "name": "fc_hidden_64",
        "model_type": "fc",
        "hidden_size": 64,
        "learning_rate": 0.001,
        "optimizer": "adam",
        "batch_size": 64,
        "epochs": 5,
        "seed": 42,
        "notes": "隐藏层从 128 改到 64",
    },

    # ---------- 改学习率 ----------
    {
        "name": "fc_lr_0.01",
        "model_type": "fc",
        "hidden_size": 128,
        "learning_rate": 0.01,
        "optimizer": "adam",
        "batch_size": 64,
        "epochs": 5,
        "seed": 42,
        "notes": "学习率 0.001 -> 0.01",
    },
    {
        "name": "fc_lr_0.0001",
        "model_type": "fc",
        "hidden_size": 128,
        "learning_rate": 0.0001,
        "optimizer": "adam",
        "batch_size": 64,
        "epochs": 5,
        "seed": 42,
        "notes": "学习率 0.001 -> 0.0001",
    },

    # ---------- 换优化器 ----------
    {
        "name": "fc_sgd",
        "model_type": "fc",
        "hidden_size": 128,
        "learning_rate": 0.01,
        "optimizer": "sgd",
        "batch_size": 64,
        "epochs": 5,
        "seed": 42,
        "notes": "Adam 换成 SGD（学习率调大）",
    },

    # ---------- 加深网络 ----------
    {
        "name": "fc_deep_256",
        "model_type": "fc_deep",
        "hidden_size": 256,
        "learning_rate": 0.001,
        "optimizer": "adam",
        "batch_size": 64,
        "epochs": 5,
        "seed": 42,
        "notes": "两层隐藏层的全连接",
    },

    # ---------- CNN ----------
    {
        "name": "cnn_baseline",
        "model_type": "cnn",
        "hidden_size": 128,
        "learning_rate": 0.001,
        "optimizer": "adam",
        "batch_size": 64,
        "epochs": 5,
        "seed": 42,
        "notes": "换成 CNN，准确率应该更高",
    },
]