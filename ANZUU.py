import os, platform, time, sys
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system("xdg-open https://chat.whatsapp.com/D24huQnSnb44lXB5iUrJVG")
os.system('git pull --quiet 2>/dev/null')
Anzu = platform.architecture()[0]
if Anzu == '64bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit')
 import fgc
elif Anzu == '32bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is 32bit which is not supported yet')
