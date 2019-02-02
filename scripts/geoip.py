#!/usr/bin/python
import geoip2.database
import sys 
import settings
import datetime
import sqlite
import os
from writeCsv import writeCsv
from writePdf import writePdf

#GeoIp location
#Takes an ip address and resolves the country, city and county
#Doesnt return anything, just prints to screen
#Process flags work when geoIp is called as a secondary tool
def geoIp(ip, db, csv, pdf):
	if db:
		settings.init()
		db = settings.getDatabaseStatus()



	print os.getcwd()
	reader = geoip2.database.Reader('aux/GeoIpDb.mmdb')
	returndata = reader.city(ip)
	country = returndata.country.iso_code
	city = returndata.city.name
	specific = returndata.subdivisions.most_specific.name
	print "***  Using Geolite2 Database of Cities ***"
	print "    Country       -->  ",country
	print "    City          -->  ",city
	print "    Specific      -->  ",specific


	#If db flag is active we put data in the database
	if db or csv or pdf:
		if db:
			print "Inserting data gathered in the database"
			sqlite.checkDb()
		now = datetime.datetime.now()
		now = str(now)
		now = now[:-7]

		if country is None:
			country = 'None'
		if city is None:
			city = 'None'
		if specific is None:
			specific = 'None'
		fields = ['Data', 'Script','Ip', 'Country', 'City', 'Specific']
		values = [now,'GeoIp', ip, country, city,specific ]

		if db:
			print "Writing to ", db

			sqlite.insertIntoTable('Script', fields, values)
			sqlite.closeDb()

		if csv:
			print "Writing to ", csv

			path = settings.getCsv()
			csv = path + csv
			if not os.path.exists(csv):
				writeCsv(fields, filename=csv)

			writeCsv( values, filename=csv)
		if pdf:
			print "Writing to ", pdf

			path = settings.getPdf()
			pdf = path + pdf
			toPdf = [fields, values]
			writePdf(toPdf, filename=pdf)



		#print fields
		#print values
def geoip_country(ip):
	reader = geoip2.database.Reader('aux/GeoIpDb.mmdb')
	returndata = reader.city(ip)
	#print returndata.country.iso_code
	a = returndata.country.iso_code
	#print a
	if a is None:
		a = 'None'

	return a
def geoip_city(ip):
	reader = geoip2.database.Reader('aux/GeoIpDb.mmdb')
	returndata = reader.city(ip)
	a = returndata.city.name
	#print a
	if a is None:
		a = 'None'

	return a
def geoip_specific(ip):
	reader = geoip2.database.Reader('aux/GeoIpDb.mmdb')
	returndata = reader.city(ip)
	a = returndata.subdivisions.most_specific.name
	if a is None:
		a = 'None'

	return a
def main():
	ip = '220.181.108.106'
	a = geoip_specific(ip)
	


if __name__=='__main__':
	main()