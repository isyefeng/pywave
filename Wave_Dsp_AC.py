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

def ShowMeasureImage(temperture_file):
	width=32  # 16进制数所占位数
	x_line = []
	y_line = []
	cnt = 0	
	with open(temperture_file) as csv_f:
		csv_file = csv.reader(csv_f)
		#list = next(csv_file)
		for line in csv_file:
			cnt = cnt + 1
			x_line.append(cnt)
			ybuf = hextotem(line[1])
			y_line.append(ybuf)
	''''
	for num in list:
		cnt = cnt + 1
		x_line.append(cnt)
		y_line.append(float(num))
	'''	
		
	fig = plt.figure(dpi=128,figsize=(10,6))
	
	
	#s 表示散点的大小，形如 shape (n, )
    #label 表示显示在图例中的标注
    #alpha 是 RGBA 颜色的透明分量
    #edgecolors 指定三点圆周的颜色    
	plt.xlabel('x',fontsize=14)
	plt.ylabel('y',fontsize=14)
	plt.scatter(x_line, y_line, edgecolor='none', s=40)
	
	#plt.ylim(-1,6)
	plt.plot(x_line, y_line, c='red')								#alpha:透明度

	plt.title('PID',  fontsize = 24)
	plt.xlabel('time', fontsize = 15)
	plt.ylabel('PID-DA-OUT(V)', fontsize = 15)
	fig.autofmt_xdate()
	plt.show()
	
contrlHistryFile = 'AcData.csv'
	
ShowMeasureImage(contrlHistryFile)


















	