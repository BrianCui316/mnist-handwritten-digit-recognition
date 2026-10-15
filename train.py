# train.py
import os
import time
import random
import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from model import build_model


def set_seed(seed):
    """固定随机种子，保证每次结果可复现。"""
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    np.random.seed(seed)


def get_data(batch_size):
    """加载 MNIST 数据。"""
    transform = transforms.ToTensor()
    train_data = datasets.MNIST(
        root="./data", train=True, download=True, transform=transform
    )
    test_data = datasets.MNIST(
        root="./data", train=False, download=True, transform=transform
    )
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader


def train_one_epoch(dataloader, model, loss_fn, optimizer, device):
    model.train()
    for X, y in dataloader:
        X, y = X.to(device), y.to(device)
        pred = model(X)
        loss = loss_fn(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


def evaluate(dataloader, model, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            correct += (pred.argmax(1) == y).sum().item()
            total += y.size(0)
    return correct / total


def build_optimizer(name, model, lr):
    if name == "adam":
        return torch.optim.Adam(model.parameters(), lr=lr)
    elif name == "sgd":
        return torch.optim.SGD(model.parameters(), lr=lr)
    elif name == "adamw":
        return torch.optim.AdamW(model.parameters(), lr=lr)
    else:
        raise ValueError(f"未知的 optimizer: {name}")


def run_experiment(config, verbose=True):
    """
    运行单个实验，返回结果字典。
    """
    set_seed(config["seed"])
    device = "cuda" if torch.cuda.is_available() else "cpu"

    train_loader, test_loader = get_data(config["batch_size"])
    model = build_model(config).to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = build_optimizer(config["optimizer"], model, config["learning_rate"])

    start_time = time.time()
    best_acc = 0.0
    final_acc = 0.0
    per_epoch = []

    for epoch in range(config["epochs"]):
        train_one_epoch(train_loader, model, loss_fn, optimizer, device)
        acc = evaluate(test_loader, model, device)
        per_epoch.append(round(acc, 4))
        final_acc = acc
        if acc > best_acc:
            best_acc = acc
        if verbose:
            print(f"  Epoch {epoch + 1}/{config['epochs']}, 测试准确率: {acc:.4f}")

    elapsed = time.time() - start_time

    # 保存最佳模型
    os.makedirs("checkpoints", exist_ok=True)
    ckpt_path = f"checkpoints/{config['name']}.pt"
    torch.save(model.state_dict(), ckpt_path)

    return {
        "final_accuracy": round(final_acc, 4),
        "best_accuracy": round(best_acc, 4),
        "per_epoch_accuracy": ";".join(str(x) for x in per_epoch),
        "training_time_sec": round(elapsed, 2),
        "device": device,
        "checkpoint": ckpt_path,
    }