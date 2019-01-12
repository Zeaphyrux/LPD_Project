#!/usr/bin/python
import geoip2.database
import sys 


#GeoIp location
#Takes an ip address and resolves the country, city and county
#Doesnt return anything, just prints to screen
def geoIp(ip):
    reader = geoip2.database.Reader('GeoIpDb.mmdb')
    returndata = reader.city(ip)
    print "***  Using Geolite2 Database of Cities ***"
    print "    Country       -->  ",returndata.country.iso_code
    print "    City          -->  ",returndata.city.name
    print "    Specific      -->  ",returndata.subdivisions.most_specific.name

