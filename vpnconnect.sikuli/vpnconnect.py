import configparser

# read config
inifile = configparser.ConfigParser()
inifile.read('config.ini','utf-8')

### connect to VPN
password = App.getClipboard()
print(password)

sonicwall = inifile.get('sikuli','sonicwall')
print(sonicwall)
app1 = App(sonicwall)
app1.open()
sleep(2)

region_1 = Region(-1195,41,468,397)
region_1.click("images/connect.png")
print('click connect button')
#sleep(3)

region_2 = Region(-937,139,77,27)
if region_2.exists("images/next.png"):
    region_2.click("images/next.png")
    print('click next button')

region_3 = Region(-1160,66,398,151)
region_3.paste("images/textbox4pass.png",password)
print('paste password')
sleep(1)

region_3.click("images/login.png")
print('click login button')

region_1.exists("images/Disconnect.png",60)
print('vpn connect is established')

### signIn to StoreWeb
citrix = inifile.get('sikuli','citrix')
print(citrix)
app2 = App(citrix)
app2.open()
sleep(5)

region_4 = Region(-1498,43,179,147)
region_4.click("images/desktopicon.png")
sleep(5)