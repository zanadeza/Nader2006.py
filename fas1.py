import requests
import sys
import os
import subprocess
import threading,requests
import os
import sys
import time
import uuid
import json
import string
import random,webbrowser
import requests
from requests.exceptions import ConnectionError as net_error
from concurrent.futures import ThreadPoolExecutor as speed

from concurrent.futures import ThreadPoolExecutor
def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  server = requests.get('https://github.com/zanadeza/Nader2006.py/blob/main/key.txt').text
  os.system(" clear")                          
  print(f" \033[1;33m  THIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST \n اهلا وسهلا بك في اداتي المتواضعه\033[1;37m\n")
  print(f"")
  print(f"\x1b[1;92m   contract Admin to Buy this Tools   عليك مراسله المطور نادر لتفعيل");time.sleep (0.1) 
  print(f"")
  print(f"\033[1;32  المفتاح الخاص بك    YOUR  KEY : "+id)
  print(f"")
  print(f"\033[1;31m   COPY YOUR KEY AND SEND TO ADMIN قم بمراسله نادر فورا ليقوم باعطائك مفتاح  ");time.sleep(0.1)
  print(f"")
  uu = '''	
~ بسم الله الرحمان الرحيم
~ السكربت مدفوع عشان برتفع على سيرفر خاص فيك
~ اسعار الاشتراك 
اسبوع ب5$
شهر ب25$
دائمي ب30$
بدون تشفير ب50$

«ملاحظة» 
السكربت لن يعمل الى بمفتاح يتم تسليمك المفتاح عند اتمام الشراء 
«ملاحضه» 
المفتاح الخاص بك هو 
'''
  try:
    a = uu+id
    httpCaht = requests.get("https://github.com/zanadeza/Nader2006.py/blob/main/key.txt").text
    if id in httpCaht:
      print("\033[1;92m   YOUR KEY APROVED المفتاح مفعل لاسبوع   ");time.sleep(2)
      msg = str(os.geteuid())
      
      time.sleep(0.5)
      pass
    else:
      print(f"\x1b[1;92m    Sorry Bro Your Key not Aproved اسف يا صاحبي المفتاح تبعك معطل  ")
      print(f"    Send Wave or Kpay  to Admin and get aproval راسل نادر عشان يعطيك مفتاح مدفوع"); time.sleep(2)
      webbrowser.open('https://t.me/N_0_N_7?text='+a)
      
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == 'main':
     print(logo)
     menu_apikey()
menu_apikey()
url = "https://zezsoft.eu/PSApp/PsArchive/getPFF.php"
ee = input('[⊰⊱]\033[1;37m  اسم الشخص : ')
ee1 = input('[⊰⊱]\033[1;37m  اسم الاب : ')
ee2 = input('[⊰⊱]\033[1;37m  اسم العيله : ')
payload = {
  'father': ee1,
  'name': ee,
  'family': ee2,
  '': ""
}


headers = {
  'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; Lenovo TB-X306X Build/RP1A.200720.011)",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Authorization': "Basic WmV6c29mdFVzZXJAMjAyNTpaZXpzb2Z0JFBhc3MjMjAyNQ=="
}

re = requests.post(url, data=payload, headers=headers).json()
id = re['psarchive'][0]['id']
g = re['psarchive'][0]['gfather']
f = re['psarchive'][0]['family']
m = re['psarchive'][0]['mother']
h = re['psarchive'][0]['hae']
b = re['psarchive'][0]['birth']
if 'NoneType' in re:
	print('ناسف يا صديقي تم حدف المعلومات بناء على طلب خاص')
	
	


	
else:
	
	print(f'''
بسم الله الرحمان الرحيم

اللهم صلي وسلم وبارك على سيدنا محمد

IDENTITY  : {id}
NAME : {ee}
FATHER : {ee1}
GRANDFATHER : {g}
FAMILY : {ee2}
MOM  : {m}
AREA : {h}
DATE : {b}

''')
