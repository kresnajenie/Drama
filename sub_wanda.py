import paho.mqtt.subscribe as subscribe
import currency as cur
import os
import sys
import time
import translate as trans

def print_msg(client,userdata,message):
	transcript = message.payload
	if transcript.lower().find("dollar") >= 0:
                dolar = cur.IDR()
                os.system("say dolar hari ini adalah  " + str(dolar) + "rupiah ")
            elif transcript.lower().find("tidur") >= 0:
                os.system("say saya tidur dulu")
                sys.exit(0)
            elif transcript.lower().find("halo wanda") >= 0:
                os.system("say halo, apa yang bisa saya bantu")
            elif transcript.lower().find("wanda") >= 0:
                os.system("say apa yang bisa saya bantu")
            elif transcript.lower().find("jam berapa") >= 0:
                jam = time.strftime("%H")
                mins = time.strftime("%M")
                os.system("say sekarang jam " + jam + "lewat " + mins + "menit")
            elif transcript.lower().find("tanggal berapa") >= 0:
                tgl = time.strftime("%d")
                bln = trans.en_to_id(time.strftime("%B"))
                os.system("say sekarang tanggal " + tgl + "bulan " + bln )
            elif transcript.lower().find("hari") >= 0:
                hari = trans.en_to_id(time.strftime("%A"))
                tgl = time.strftime("%d")
                bln = trans.en_to_id(time.strftime("%B"))
                os.system("say sekarang hari " + hari + "tanggal " + tgl + "bulan " + bln)
            elif transcript.lower().find("translate menjadi inggris"):
                l = transcript
                os.system("say " + trans.id_to_en(l))
            else:
                os.system("say maaf, coba ulang lagi")
	
subscribe.callback(print_msg, "kolla/kresna", hostname="test.mosquitto.org")
