# pip install -i  https://pypi.tuna.tsinghua.edu.cn/simple 改变镜像源
##test2
##test3
import pandas as pd
import os
import csv
import numpy as np
import glob
import linecache
import re

#提取指定两列，所有key的热度排名处理。skipfooter跳过最后一行
temp = 'tmp.txt'
n = 2
data = pd .read_csv(temp,header=None,names=[n,'counter'],skiprows=[0,1],skipfooter=1,usecols=[0,1],delimiter='\s+',engine='python')
#data.colunms=['1','counter']
print(data)

#提取指定两列，随时间变化的ops
#temp = 'res.txt'
#data = pd .read_csv(temp,header=None,skiprows=[0,1],usecols=[3,9],delimiter='\s+',engine='python')#usecols会选取指定列
#print(data[3],data[9])
#print(data)
#df2 = pd.DataFrame(data)
#df2.columns = ('time','ops/s')
#df2.to_csv('timeOps.csv',index=None)

#提取perf输出文件中cache miss的值
#temp = 'tmp.txt'
#data = pd.read_csv(temp, header=None, skiprows=[0,1,2,4,5], delimiter='\s+',engine='python')
#print(list(data[0]))

#垂直合并多个csv文件
##导包并设置csv文件目录
#path = os.path.abspath('D:\\experiment\\redis\\memtier_test\\size-ops\\server\\fixed')  # 文件夹路径
#filename_extenstion = '.csv'  # 文件后缀
#new_file_name = 'data.csv'  # 合并后的文件名
#cols_new_name = ['total','total']  # 汇总后的列名，根据需要修改
#cols_num = [1]  # 需要合并的列的索引，从0开始
##读取并保存所有文件名
#file_allname = []  # 用于存储全部文件的名字
#for filename in os.listdir(path):
#    if os.path.splitext(filename)[1] == filename_extenstion and filename != new_file_name:  # 按.csv后缀匹配
#        t = os.path.splitext(filename)[0]
#        file_allname.append(t + filename_extenstion)  # 拼接.csv后缀，生成完整文件名
##合并文件
#df = pd.DataFrame(cols_new_name).T
#try:
#    print('开始合并：')
#    df.to_csv(path + '\\' + new_file_name, encoding='gbk', header=False, index=False)
#    for fn in file_allname:
#        data = pd.read_csv(path + '\\' + fn)
#        #print('合并' + fn)
#        #data = a.iloc[1:, cols_num]  # 跳过标题行
#        data.to_csv(path + '\\' + new_file_name, mode='a', encoding='gbk', header=False, index=False)
#    print('合并结束，生成新文件：' + new_file_name)
#except PermissionError as e:
#    print('出现异常:' + str(type(e)) + '！\n文件已打开？请先关闭')

#水平合并多个csv文件，处理fix和range的ops
#output_file = "ndf.csv"
#input_list = glob.glob('D:\\experiment\\redis\\memtier_test\\defrag-ops\\test2\\test2\\ndf\\*')
##input_list = glob.glob('D:\\experiment\\redis\\memtier_test\\cacheMiss\\jemalloc\\range\\*')
##input_list = glob.glob('D:\\experiment\\redis\\memtier_test\\time-defragOps\\test2\\defragR10\\*')
#list = []
#for i in input_list:
#    list.append(pd.read_csv(i,usecols=[1]))
#out_csv = pd.concat(list,axis=1)
#out_csv.to_csv(output_file,index=False)

#处理key和counter，为从counter的csv文件中提取出来的列添加key的表头，将所有的进行水平合并
#output_file = "key-counter.csv"
#input_list = glob.glob('D:\\experiment\\redis\\memtier_test\\key-valSize&Counter\\1-10000-x20\\hotChange\\*')
#list = []
#colname=[]
#for i in input_list:
#    key = re.findall(r'ge\\(.+).txt',i)[0]
#    colname.append(key)
#    col = pd.read_csv(i,usecols=[0],header=None)
#    col.columns=colname
#    colname.clear()
#    #print(col)
#    list.append(col)
#out_csv = pd.concat(list,axis=1)
#out_csv.to_csv(output_file,index=False)

#提取多个文件的文件名和其第一行的内容放到一个csv中
#input_list = glob.glob('D:\\experiment\\redis\\memtier_test\\key-valSize&Counter\\1-10000-x20\\sizeChange\\*')
#result = []
#rowList = []
#for i in input_list:
#    key = re.findall(r'ge\\(.+).txt',i)
#    rowList.append(key[0])
#    valSize = linecache.getline(i,1).strip()
#    rowList.append(valSize)
#    result.append(rowList.copy())
#    rowList.clear()
#print(result)
#df = pd.DataFrame(result)
#df.columns=('key','valSize')
#df.to_csv('key-valSize.csv', index=None)

#simple test
#input_list = glob.glob('D:\\experiment\\redis\\memtier_test\\size-ops\\server\\range\\*')
#for i in input_list:
#    print(re.findall(r'\\(.+)\.txt',i))
#i = 'D:\\experiment\\redis\\memtier_test\\key-valSize&Counter\\1-10000\\1\\memtier-8815.txt'
#print(re.findall(r'1\\(.+).txt',i))

#file_path = 'D:\\experiment\\redis\\memtier_test\\key-valSize&Counter\\1-10000\\1\\memtier-8815.txt'
#line_number = 1
#print(linecache.getline(file_path, line_number).strip())