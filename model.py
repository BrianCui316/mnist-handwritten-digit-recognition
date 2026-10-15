# model.py
import torch.nn as nn


def build_model(config):
    """
    根据 config 里的 model_type 返回对应的模型。
    """
    model_type = config["model_type"]
    hidden = config["hidden_size"]

    if model_type == "fc":
        # 最简单的全连接网络
        return nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 10),
        )

    elif model_type == "fc_deep":
        # 两层隐藏层
        return nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden // 2),
            nn.ReLU(),
            nn.Linear(hidden // 2, 10),
        )

    elif model_type == "cnn":
        # 卷积神经网络
        return nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 10),
        )

    else:
        raise ValueError(f"未知的 model_type: {model_type}")