from matplotlib import pyplot as plt
from datetime import datetime
import csv
import re

def hextotem( hexdata ):
	x = int(hexdata,16)
	if( x > 32768 ):
		x = 65536-x
		x = x*-1
	return x

def ShowMeasureImage():
	width=32  # 16进制数所占位数
	x_line = []
	y_line = []
	cnt = 0	
	with open('AcData1.csv') as csv_f:
		csv_file = csv.reader(csv_f)
		#list = next(csv_file)
		for line in csv_file:
			cnt = cnt + 1
			x_line.append(cnt)
			ybuf = hextotem(line[1])
			y_line.append(ybuf)
			
	x1_line = []
	y1_line = []
	cnt = 0	
	with open('AcData2.csv') as csv_f:
		csv_file = csv.reader(csv_f)
		#list = next(csv_file)
		for line in csv_file:
			cnt = cnt + 1
			x1_line.append(cnt)
			ybuf = hextotem(line[1])
			y1_line.append(ybuf)
			
	x2_line = []
	y2_line = []
	cnt = 0	
	with open('AcData3.csv') as csv_f:
		csv_file = csv.reader(csv_f)
		#list = next(csv_file)
		for line in csv_file:
			cnt = cnt + 1
			x2_line.append(cnt)
			ybuf = hextotem(line[1])
			y2_line.append(ybuf)
			
	x3_line = []
	y3_line = []
	cnt = 0	
	with open('AcData4.csv') as csv_f:
		csv_file = csv.reader(csv_f)
		#list = next(csv_file)
		for line in csv_file:
			cnt = cnt + 1
			x3_line.append(cnt)
			ybuf = hextotem(line[1])
			y3_line.append(ybuf)
			
	xx_line = []
	yy_line = []
	cnt = 0	
	for line in range(1124):
		cnt = cnt + 1
		xx_line.append(cnt)
		yy_line.append(1000)
		
	fig = plt.figure(dpi=128,figsize=(10,6))
	
	#s 表示散点的大小，形如 shape (n, )
    #label 表示显示在图例中的标注
    #alpha 是 RGBA 颜色的透明分量
    #edgecolors 指定三点圆周的颜色    

	plt.scatter(x_line, y_line, edgecolor='none', s=40)
	plt.plot(x_line, y_line, c='red')								#alpha:透明度
	
	plt.scatter(x1_line, y1_line, edgecolor='none', s=40)
	plt.plot(x1_line, y1_line, c='yellow')								#alpha:透明度
	
	plt.scatter(x2_line, y2_line, edgecolor='none', s=40)
	plt.plot(x2_line, y2_line, c='green')								#alpha:透明度
	
	plt.scatter(x3_line, y3_line, edgecolor='none', s=40)
	plt.plot(x3_line, y3_line, c='gray')								#alpha:透明度
	
	plt.scatter(xx_line, yy_line, edgecolor='none', s=40)
	plt.plot(xx_line, yy_line, c='gray')								#alpha:透明度

	'''
	plt.title('PID',  fontsize = 24)
	plt.xlabel('time', fontsize = 15)
	plt.ylabel('PID-DA-OUT(V)', fontsize = 15)
	'''
	fig.autofmt_xdate()
	plt.show()
	

	
ShowMeasureImage()


















	