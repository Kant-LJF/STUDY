#!/user/bin/env python
# _*_coding=utf-8_*_

import os

# os.listdir
print(os.getcwd())
print(os.listdir(r"J:\zj")) #列出指定目录所有文件目录

for path in os.listdir(r"J:\zj"):
    paths="J:\zj"+"\\"+path
    print(paths)
    if os.path.isdir(paths):
        os.listdir(os.path.join(r"J:\zj",path))
        print("{0}还需要做进一步处理".format(path))
    else:
        print("这个已经是穷尽的路径了",os.path.join(r"J:\zj",path))