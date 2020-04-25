import configparser
import myModule
import pyperclip
import subprocess
import time

# read config
inifile = configparser.ConfigParser()
inifile.read('/Users/yoshidatatsuya/Documents/GitHub/automation/vpnconnect.sikuli/config.ini','utf-8')

# get onetime password
url = inifile.get('ePass','url')
username = inifile.get('ePass','username')
prefix = inifile.get('ePass','prefix')
row = inifile.get('ePass','row')
col = inifile.get('ePass','col')

password = myModule.getepass(url,username,prefix,int(row),int(col))
#print(password)

# copy to clipboard
pyperclip.copy(password)
#time.sleep(2)

# run sikuli (RPA)
java = inifile.get('sikuli','java')
jarfile = inifile.get('sikuli','jarfile')
sikulidir = inifile.get('sikuli','sikulidir')

path = java + ' -jar ' + jarfile + ' -r ' + sikulidir
subprocess.run(path, shell=True)

