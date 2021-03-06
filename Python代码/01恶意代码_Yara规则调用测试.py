#-*-coding:utf-8-*-
import yara
import os
import os.path 
rootdir = "E:\\Vir"    # 病毒目录
YaraRule_dir = "E:\\yara-rule.txt"  



def mycallback(data):
    if data['strings']:
        print(data['rule']) #输出 匹配到的特征
        yara.CALLBACK_CONTINUE



for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:                        #输出文件信息
        print(filename)
        rules = yara.compile(YaraRule_dir)            # yara规则调用 
        matches = rules.match(os.path.join(parent,filename), callback=mycallback)
#       print("the full name of the file is:" + os.path.join(parent,filename)) #输出文件路径信息