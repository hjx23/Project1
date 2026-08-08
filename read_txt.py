from pathlib import Path

def read_single_txt(file_path: str | Path):
    path = Path(file_path)
    # 判断文件是否存在
    if not path.exists():
        print("目标文件不存在")
        return ""
    # 双编码兜底读取
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="gbk") as f:
            return f.read()

if __name__ == "__main__":
    content = read_single_txt("./docs/test.txt")
    print(content)