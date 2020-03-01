# -*- coding: utf-8 -*-
# Author: Pranshu Mandal
# Date: 01/03/2020

import numpy as np
import pandas as pd

filename = "stdout_14atom_CE"

data = open("./" + filename, 'r')

keyword = "E+L*chi2"   # beginning keyword
keyword1 = "* * * SCF has converged * * *"   # end keyword
 
n = 1
print(type(data))

m_l_n = [] #matching line number for keyword
m_l_n_1 = [] ##matching line number for keyword1

for line in data:
	if keyword in line:
		m_l_n.append(n)
	if keyword1 in line:
		m_l_n_1.append(n)

	n += 1
data.close()
# getting the table in the middle of the two keywords

lines_for_table = []

for i in range(len(m_l_n)):
	table_start = m_l_n[i] - 2
	table_end = m_l_n_1[i+1] - 3
	lines= np.arange(table_start, table_end, 1)
	lines_for_table.append(lines)

for i in range(len(lines_for_table)):
	lines = lines_for_table[i]
	fp   = open("./stdout_14atom_CE", "r")
	src = fp.readlines()
	dat = [(index, line) for index, line in enumerate(src) if index in lines]
	df = pd.DataFrame(dat)
	df2 = df.iloc[[-1]]   # line number selection
	print(df2)
	df2.to_csv(r'./output_last_3.txt', header=None, index=None, sep=' ', mode='a')

fp.close()