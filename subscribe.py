import paho.mqtt.subscribe as subscribe
import currency as cur

def print_msg(client,userdata,message):
	pesan = message.payload
	if pesan.upper() == "USD":
		x = "USD sekarang adalah Rp " + str(cur.IDR())
	elif pesan.upper() == "SGD":
		x = "SGD sekarang adalah Rp " + str(cur.SGDIDR())
	elif pesan.upper() == "EUR":
		x = "EUR sekarang adalah Rp " + str(cur.EURIDR())
	print message.topic + ": " + str(x)

subscribe.callback(print_msg, "kolla/kresna", hostname="test.mosquitto.org")
