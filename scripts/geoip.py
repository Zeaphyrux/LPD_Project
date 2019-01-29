#!/usr/bin/python
import geoip2.database
import sys 
import settings
import datetime
import sqlite
import os


#GeoIp location
#Takes an ip address and resolves the country, city and county
#Doesnt return anything, just prints to screen
#Process flags work when geoIp is called as a secondary tool
def geoIp(ip, process=False):
	if not process:
		settings.init()
		db = settings.getDatabaseStatus()
	else:
		db = False
	print os.getcwd()
	reader = geoip2.database.Reader('GeoIpDb.mmdb')
	returndata = reader.city(ip)
	country = returndata.country.iso_code
	city = returndata.city.name
	specific = returndata.subdivisions.most_specific.name
	print "***  Using Geolite2 Database of Cities ***"
	print "    Country       -->  ",country
	print "    City          -->  ",city
	print "    Specific      -->  ",specific


	#If db flag is active we put data in the database
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
		fields = ['Data', 'Ip', 'Country', 'City', 'Specific']
		values = [now, ip, country, city,specific ]

		sqlite.insertIntoTable('Script', fields, values)

		#print fields
		#print values
		sqlite.closeDb()
def geoip_country(ip):
	reader = geoip2.database.Reader('scripts/GeoIpDb.mmdb')
	returndata = reader.city(ip)
	#print returndata.country.iso_code
	a = returndata.country.iso_code
	#print a
	if a is None:
		a = 'None'

	return a
def geoip_city(ip):
	reader = geoip2.database.Reader('scripts/GeoIpDb.mmdb')
	returndata = reader.city(ip)
	a = returndata.city.name
	#print a
	if a is None:
		a = 'None'

	return a
def geoip_specific(ip):
	reader = geoip2.database.Reader('scripts/GeoIpDb.mmdb')
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