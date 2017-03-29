import pandas as pd
import numpy as np 

data=pd.read_csv('20170215_Lib_FA_NE_CT_YR_v2.csv')
output=open('yirang_out.txt','w')

min_val = []
header = (list(data)[1:])

for i in range(len(header)):
	min_val.append(data[header[i]].iloc[-1])

size = list(data[data.columns[0]].iloc[:-2])

output.write('Sample'+'\t'+'Start_size'+'\t'+'Start_RFU'+'\t'+'End_size'+'\t'+'End_RFU'+'\t'+'Gap'+'\n')

for i in range( len(header) ):
	col = data[header[i]].iloc[:-2]
	col_min = min_val[i]
	numbers = []
	for x in range(340, 1077): ##340 is the index of size 150, 900 is about the size of 700
		val = col[x]
		if val > col_min:
			numbers.append((val, size[x]))
	start_val = numbers[0][0]
	start_idx = numbers[0][1]
	end_val = numbers[-1][0]
	end_idx = numbers[-1][1]
	gap = '{:.2f}'.format(float(end_idx)-float(start_idx))
	output.write(header[i]+'\t'+str(start_idx)+'\t'+str(start_val)+'\t'+str(end_idx)+'\t'+str(end_val)+'\t'+str(gap)+'\n')

output.close()





