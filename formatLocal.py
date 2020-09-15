#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
import xlrd
import os
data = xlrd.open_workbook('local.xlsx') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
#删除原文件 创建新文件
os.remove("ZYTestLocal/zh-Hans.lproj/loc.strings")
f=file("ZYTestLocal/zh-Hans.lproj/loc.strings","a+")
for i in range(nrows): # 循环逐行打印
	if i < 1: # 跳过第一,二行
		continue
	#主语言
	en = str(table.row_values(i)[3].encode('utf8'))
	#其他语言
	other = str(table.row_values(i)[4].encode('utf8'))
	if len(en) > 0:
		output = "\"{0}\" = \"{1}\";\n".format(en, other)
		f.write(output)
		#print output
	
#关闭文件
f.close()
