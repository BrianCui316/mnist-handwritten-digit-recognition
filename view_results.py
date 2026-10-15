# view_results.py
import csv
import os
import sys

CSV_FILE = "experiments.csv"


def load_rows():
    if not os.path.exists(CSV_FILE):
        print(f"还没有 {CSV_FILE}，先运行 run_experiments.py")
        sys.exit(1)
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def print_table(rows):
    """在终端里对齐打印表格。"""
    columns = ["name", "model_type", "hidden_size", "learning_rate",
               "optimizer", "epochs", "best_accuracy", "training_time_sec", "notes"]
    widths = {c: max(len(c), max(len(str(r[c])) for r in rows)) for c in columns}

    header = " | ".join(c.ljust(widths[c]) for c in columns)
    print(header)
    print("-" * len(header))
    for r in rows:
        print(" | ".join(str(r[c]).ljust(widths[c]) for c in columns))


def export_markdown(rows):
    """导出 Markdown 表格到 results.md。"""
    columns = ["name", "model_type", "hidden_size", "learning_rate",
               "optimizer", "epochs", "best_accuracy", "training_time_sec", "notes"]

    lines = []
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for r in rows:
        lines.append("| " + " | ".join(str(r[c]) for c in columns) + " |")

    with open("results.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("\n已导出 Markdown 表格到 results.md")
    print("你可以把里面的内容直接粘贴到 README.md")


def main():
    rows = load_rows()

    # 按最佳准确率从高到低排序
    rows.sort(key=lambda r: float(r["best_accuracy"]), reverse=True)

    print(f"共 {len(rows)} 个实验\n")
    print_table(rows)
    export_markdown(rows)


if __name__ == "__main__":
    main()