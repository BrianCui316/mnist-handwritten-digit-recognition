# run_experiments.py
import csv
import os
from datetime import datetime

from configs import EXPERIMENTS
from train import run_experiment

CSV_FILE = "experiments.csv"

# CSV 的列（顺序就是表格的列顺序）
FIELDNAMES = [
    "experiment_id",
    "timestamp",
    "name",
    "model_type",
    "hidden_size",
    "learning_rate",
    "optimizer",
    "batch_size",
    "epochs",
    "seed",
    "final_accuracy",
    "best_accuracy",
    "per_epoch_accuracy",
    "training_time_sec",
    "device",
    "checkpoint",
    "notes",
]


def load_existing_ids():
    """读取已经跑过的实验名字，避免重复。"""
    if not os.path.exists(CSV_FILE):
        return set()
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return {row["experiment_id"] for row in reader}


def append_result(row):
    """把一条实验结果追加到 CSV。"""
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def main():
    existing = load_existing_ids()
    total = len(EXPERIMENTS)

    for idx, config in enumerate(EXPERIMENTS, 1):
        exp_id = config["name"]

        if exp_id in existing:
            print(f"[{idx}/{total}] 跳过已完成的实验: {exp_id}")
            continue

        print(f"\n[{idx}/{total}] ===== 运行实验: {exp_id} =====")
        print(f"配置: {config}")

        result = run_experiment(config)

        row = {
            "experiment_id": exp_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": config["name"],
            "model_type": config["model_type"],
            "hidden_size": config["hidden_size"],
            "learning_rate": config["learning_rate"],
            "optimizer": config["optimizer"],
            "batch_size": config["batch_size"],
            "epochs": config["epochs"],
            "seed": config["seed"],
            "final_accuracy": result["final_accuracy"],
            "best_accuracy": result["best_accuracy"],
            "per_epoch_accuracy": result["per_epoch_accuracy"],
            "training_time_sec": result["training_time_sec"],
            "device": result["device"],
            "checkpoint": result["checkpoint"],
            "notes": config.get("notes", ""),
        }
        append_result(row)

        print(f"✅ 完成: {exp_id}, 最佳准确率 {result['best_accuracy']}")
        print(f"   结果已写入 {CSV_FILE}")

    print("\n全部实验完成。运行 python view_results.py 查看汇总表。")


if __name__ == "__main__":
    main()