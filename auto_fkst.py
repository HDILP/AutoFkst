import uiautomator2 as u2

pak_name = 'com.yaerxing.fksu'

d = u2.connect() # connect to device
print(d.info)
d.app_stop(pak_name)

d.press("home") # press the home key, with key name
d.app_start(pak_name)
