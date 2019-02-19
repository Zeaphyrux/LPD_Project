#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Reads the data from the default database and generates images plotting 
the data associated with the countries in a geographical world map
'''


import matplotlib.pyplot as plt
import cartopy
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import numpy as np
import pandas as pd

import sqlite
import settings

def plotMap(x, y,s, filename=''):
	'''
	Plots the map and exports to an image file

	x and y:
		coordinates of the data points
	s:
		Size of the data points
	filename:
		Optional file to export. If its not exporter its shown on the screen
		'''

	ax = plt.axes(projection=ccrs.PlateCarree())
	#ax.add_feature(cartopy.feature.LAND)
	ax.add_feature(cartopy.feature.OCEAN)
	#ax.add_feature(cartopy.feature.COASTLINE)
	#ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
	#ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
	#ax.add_feature(cartopy.feature.RIVERS)
	ax.set_extent([-150, 60, -25, 60])

	shpfilename = shpreader.natural_earth(resolution='110m',
	                                      category='cultural',
	                                      name='admin_0_countries')
	reader = shpreader.Reader(shpfilename)
	countries = reader.records()
	#x = np.arance(0, 5, 0.1)
	x = np.array([x])
	y = np.array([y])
	total=0
	#print s
	for i in range(len(s)):
		total+=s[i]
	#print total
	for i in range(len(s)):
		s[i] = s[i]*100/total 
	#print s
	plt.scatter(x, y,s=s, marker='o', color='b')

	#plt.plot(9,9 , marker='o', label='1.1.1.1')
	if filename:
		print "Writting file ", filename
		plt.savefig(filename)
	else:
		plt.show()
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

def mapCountryCoord(country):
	'''
	Maps a country to the latitude and longitude

	country:
		Country initials. Ex: Portugal - PT
		'''
	df = pd.read_csv('aux/countriesCord.csv')
	for i in range(len(df['country'])):
		if country==str(df['country'][i]):
			y = df['latitude'][i]
			x = df['longitude'][i]
			coord = [x, y]
			return coord


def runDbGeoMap(table, field, filename):
	'''
	Run function to be called

	table:
		Table to query on the default database
	field:
		Field to query on the default database
	filename:
		Filename to export to

		'''
	info = frequenciesDb(table,field)
	values = info.values()
	keys = info.keys()

	x = 0
	keyss = []
	valuess = []
	while x<len(values):
		keyss.append(keys[x][0])
		valuess.append(values[x])
		if keys[x][0] is None or keys[x][0]=='None':
			keyss.pop()
			valuess.pop()

		x+=1



	x = []
	y = []
	for i in range(len(valuess)):
		coord = mapCountryCoord(keyss[i])
		if coord:
			x.append(coord[0])
			y.append(coord[1])
		else:
			print "Country's coordinates not found on the database"



	plotMap(x, y, valuess, filename)
def runDbGeoMapS(filename):
	'''
	Run function for the 'Script' table on the default database
	'''
	sqlite.checkDb()	

	runDbGeoMap('Script', 'Country','output/images/'+ filename)
	sqlite.closeDb()
def runDbGeoMapL(filename):
	'''
	Run function for the 'Logs' table on the default database
	'''
	sqlite.checkDb()	

	runDbGeoMap('Logs', 'SrcCountry', 'output/images/Src'+filename)
	runDbGeoMap('Logs', 'DstCountry', 'output/images/Dst'+filename)
	sqlite.closeDb()

def main():
	run()
	#a = mapCountryCoord('PT')
	#print a
	#plotMap(0, 0)
if __name__=='__main__':
	main()