from pathlib import Path

#定义读取txt文档的函数
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

#定义拼接文件夹中txt文档的函数
def load_all_docs(folder: str = "./docs",max_len=6000): #传参是文件夹地址————默认的
    dir_path = Path(folder)#拿到对应文件夹的地址
    txt_list = dir_path.glob("*.txt")#将对应文件夹中的所有txt文件做为迭代器
    total_text = ""
    for file in txt_list:
        text = read_single_txt(file)
        total_text += f"【{file.name}】:\n{text}\n"
    return total_text[:max_len]

if __name__ == "__main__":
    merge_text = load_all_docs()
    print(merge_text)