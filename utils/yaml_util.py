import os

import yaml

# 将yaml文件写入数据
def write_yaml(filename,data):
    with open(os.getcwd()+"/data/"+filename,mode="a+",encoding="utf-8")as f:
        yaml.safe_dump(data,stream=f)
# 读取yaml文件中的数据
def read_yaml(filename,key):
    with open(os.getcwd()+"/data/"+filename,mode="a+",encoding="utf-8")as f:
        data=yaml.safe_load(f)
        return data[key]
# 清空
def clear_yaml(filename,key):
    with open(os.getcwd() + "/data/" + filename, mode="a+", encoding="utf-8") as f:
        f.truncate()