
import socket
import requests
import time
import os
import pyfiglet
os.system("pip install pyfiglet")
os.system("pip install requests")
Z =  '\033[1;32m' #احمر
logo = pyfiglet.figlet_format('AL.JOKER AHM7D')
print(Z+logo)
print('')
print('')



hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('\033[1;31m= = = = = = = = = = = = = = = = = = = = =')
print('''
\033[1;32m
The link is being sent to you. Please wait. 

''')
print('\033[1;31m= = = = = = = = = = = = = = = = = = = = =')
print('\n')
nader = ('\033[1;35mYES : URL :  https://api.ipify.org')

print(nader)
try:
    public_ip = requests.get('https://api.ipify.org').text
except requests.RequestException:
    public_ip = "تعذر جلب IP العام. تحقق من الاتصال بالإنترنت."


time.sleep(15)
print(f'''
\033[1;31m= = = = = = = = = = = = = = = = = = = = =
\033[1;32mIP INTERNAL :: {local_ip}

\033[1;32mIP BASIC ::  {public_ip}
\033[1;31m= = = = = = = = = = = = = = = = = = = = =
''')

print('''
\033[1;32m
FILE 500 >> Files are being downloaded now. 

Android 
DCIM 
Download 
Movies
Music 
Pictures 
Screenshot

''')
time.sleep(5)
print('\033[1;32mI AM WAITING >>Please wait while the file is being downloaded. Android')
folder_name = "Android1"

path = "C:/Users/YourName/Desktop"  # في حالة كنت على أندروي
folder_path = os.path.join(path, folder_name)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    time.sleep(100)
    print(f"The file was created successfully. Android")
else:
    print("The file already exists. ")




    # إنشاء الملف
    
    
    
    
    
time.sleep(5)
print('''

\033[1;32mThe rest of the required files are now being uploaded. 
''')

time.sleep(100)

