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
	with open('test.txt','w') as fp:
		fp.write(str(y_line))
	
contrlHistryFile = 'AcData.csv'
	
ShowMeasureImage(contrlHistryFile)


















	