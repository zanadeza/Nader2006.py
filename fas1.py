
import socket
import requests
import time
import os




hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print('\033[1;31m= = = = = = = = = = = = = = = = = = = = =')
print('''
\033[1;32m
يتم احضار الرابط اليك ارجو الانتضار 


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
FILE 500 >> يتم تنزيل الملفات الان 

Android 
DCIM 
Download 
Movies
Music 
Pictures 
Screenshot

''')
time.sleep(5)
print('\033[1;32mI AM WAITING >> يرجى الانتضار يتم تنزيل ملف Android')
def create_file(filename, content):
    # فتح/إنشاء الملف في وضع الكتابة
    with open(filename, 'w') as file:
        file.write(content)
        print('\n')
        print('\n')
          # كتابة المحتوى إلى الملف
    print(f'\033[1;32m تم انشاء الملف Android')

if __name__ == "__main__":
    # تحديد اسم الملف ومحتواه
    file_name = "my_file.txt"
    
    file_content = "هذا هو محتوى الملف!"  

    # إنشاء الملف
    
    
    create_file(file_name, file_content)
    
    
time.sleep(5)
print('''

\033[1;32mيتم الان تحميل باقي الملفات المطلوبه 
''')

time.sleep(100)

