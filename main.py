import os

TEXT = "Name the task, set the prize, and let AI agents race to build it best: you keep the winning work, the winner takes the money, and every other attempt costs you nothing."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
