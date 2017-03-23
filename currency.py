from openexchangerates import OpenExchangeRatesClient
#import kresna_email as em 
import datetime
client = OpenExchangeRatesClient('f3aace9f692243aa909eda0e0c35bf32')

s = client.latest()

#for x in s:
#	print x
x = s["rates"]

def print_menu():
	print "=================================="
	print "MONEY CONVERTER"
	print "=================================="
	print "Data retrieved at", (datetime.datetime.fromtimestamp(
        						int(s["timestamp"])
    						).strftime('%Y-%m-%d %H:%M:%S'))
	print "type 'P' to print menu"
	print "type 'USD' to convert USD to IDR"
	print "type 'SGD' to convert SGD to IDR"
	print "type 'EUR' to convert EUR to IDR"
	print "type 'Q' to quit"
	print "=================================="

def USD(money):
	l = float(x["IDR"]) * money 
	print "USD in IDR = Rp", l
	text =  "USD in IDR = Rp", l
	em.simple_msg("kresna.jenie@gmail.com","Money Converter Report",text)
def SGD(money):
	l =  (float(x["IDR"])/float(x["SGD"])) * money 
	print "SGD in IDR = Rp", l
	text =  "SGD in IDR = Rp", l
	em.simple_msg("kresna.jenie@gmail.com","Money Converter Report",text)

def EUR(money):
	l = (float(x["IDR"])/float(x["EUR"])) * money 
	print "EUR in IDR = Rp", l
	text =  "EUR in IDR = Rp", l
	em.simple_msg("kresna.jenie@gmail.com","Money Converter Report",text)

def IDR():
	l = str(x["IDR"])
	return l

def SGDIDR():
	l = float(x["IDR"])/float(x["SGD"])
	return l

def EURIDR():
	l = float(x["IDR"])/float(x["EUR"])
	return l








