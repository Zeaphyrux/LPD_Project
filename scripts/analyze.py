#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Uses the information in the default database to analyze the data, generate
plots and export to pdf
'''

import sqlite
import settings
import matplotlib.pyplot as plt
from writeCsv import writeCsv
from writePdf import writePdf


def piePlot(labels, sizes, filename, title):
	'''
	Creates a pie plot

	labels:	
		Names for each chunk of data

	sizes:
		Values for each chunk in data

	filename:
		filename to export to

	title:
		Title of the chart
	'''
	#clean string
	x= 0
	label = []
	siz = []
	size = len(labels)
	while x<size:
		label.append(labels[x][0])
		siz.append(sizes[x])
		if labels[x][0] is None or labels[x][0]=='None':
			label.pop()
			siz.pop()
		x+=1

	if not label:
		print "Array is empty, skipping pie chart creation"
		return 0
	plt.title(title)

	#plt.pie(sizes,labels=labels,startangle=90, autopct='%1.1f%%')
	 

	patches, texts = plt.pie(siz, startangle=90)
	plt.legend(patches, label, loc='upper right', bbox_to_anchor=(1.15, 1.05),
           fancybox=True)

	plt.axis('equal')
	plt.savefig(filename)
	plt.clf()

def frequenciesDb(table, field):
	'''
	Gets frequencies for the specified table and field of the default database
	'''



	sql = '''select {} from {}   '''.format(field, table)
	info = []
	info = sqlite.executeSQL(sql)
	print "Calculating frequencies for ", field

	freq= {i:info.count(i) for i in info}
	#remove nones

	return freq

def run(table, field, filename, title):
	'''
	Run function to be called

	table:
		Table to query on the default database
	field:
		Field to query on the default database
	filename:
		Filename to export to
	title:
		Title of the plot
		'''
	info = frequenciesDb(table,field)
	values = info.values()
	keys = info.keys()
	piePlot(keys, values, filename, title)
def runPdfChartsScript(filename):
	'''
	Run function for the 'Script' table on the default database
	'''
	settings.init()
	sqlite.checkDb(db='output/LPD.db')
	run('Script', 'Ip', 'aux/images/pdfChartScript1.png', 'Ips')
	run('Script', 'Country', 'aux/images/pdfChartScript2.png', 'Countries')
	run('Script', 'City', 'aux/images/pdfChartScript3.png', 'Cities')
	run('Script', 'Specific', 'aux/images/pdfChartScript4.png', 'Region')
	run('Script', 'PortsOpen', 'aux/images/pdfChartScript5.png', 'Ports Open')
	writePdf(0, filename, images=['aux/images/pdfChartScript1.png','aux/images/pdfChartScript2.png',
		'aux/images/pdfChartScript3.png','aux/images/pdfChartScript4.png','aux/images/pdfChartScript5.png'])
	sqlite.closeDb()
def runPdfChartsLogs(filename):
	'''
	Run function for the 'Logs' table on the default database
	'''
	
	settings.init()
	sqlite.checkDb(db='output/LPD.db')
	run('Logs', 'SrcIp', 'aux/images/pdfChartLogs1.png', 'Source Ips')
	run('Logs', 'SrcCountry', 'aux/images/pdfChartLogs2.png', 'Source Ips Countries')
	run('Logs', 'SrcCity', 'aux/images/pdfChartLogs3.png', 'Source Ips Cities')
	run('Logs', 'SrcSpecific', 'aux/images/pdfChartLogs4.png', 'Source Ips Region')
	run('Logs', 'DstIp', 'aux/images/pdfChartLogs5.png', 'Destination Ips')
	run('Logs', 'DstCountry', 'aux/images/pdfChartLogs6.png', 'Destination Ips Countries')
	run('Logs', 'DstCity', 'aux/images/pdfChartLogs7.png', 'Destination Ips Cities')
	run('Logs', 'DstSpecific', 'aux/images/pdfChartLogs8.png', 'Destination Ips Region')


	writePdf(0, filename, images=['aux/images/pdfChartLogs1.png','aux/images/pdfChartLogs2.png',
		'aux/images/pdfChartLogs3.png','aux/images/pdfChartLogs4.png',
		'aux/images/pdfChartLogs5.png','aux/images/pdfChartLogs6.png',
		'aux/images/pdfChartLogs7.png','aux/images/pdfChartLogs8.png',])
	sqlite.closeDb()


def exportDbPdf(table):
	'''From the default database exports to pdf
	table:
		Table to export'''
	settings.init()
	sqlite.checkDb(db='output/LPD.db')

	sql = ''' select * from  {}'''.format(table)

	data = sqlite.executeSQL(sql)
	writePdf(data, 'output/pdf/'+table+'.pdf')
	sqlite.closeDb()
def exportDbCsv(table):
	'''From the default database exports to csv
	table:
		Table to export'''
	settings.init()
	sqlite.checkDb(db='output/LPD.db')

	sql = ''' select * from  {}'''.format(table)

	data = sqlite.executeSQL(sql)
	for i in range(len(data)):
		writeCsv(data[i], 'output/csv/'+table+'.csv')
		
	sqlite.closeDb()



def main():
	#run('Logs', 'DstIp', 'pie.png', 'title')
	runAll()

if __name__=='__main__':
	main()