from pathlib import Path

def read_single_txt(file_path: str | Path):
    path = Path(file_path)
    #判断文件是否存在
    if not path.exists():
        print("文件不存在！！！")
        return ""
    #双保险：如果utf-8格式不对的话，那么可以使用gbk格式去解析
    try:
        with open(path,"r",encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path,"r",encoding="gbk") as f:
            return f.read()
    #上述代码存在问题：如果我传入的文件路径是文件夹的路径，程序不会报错也不会有结果
    #所以我需要继续进行报错处理
    except Exception as e:
        print(f"读取失败：{e}")
        return ""

if __name__ == "__main__":
    content = read_single_txt("./docs/test.txt")
    print(content)