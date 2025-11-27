import os, datetime, base64, io, sys, ctypes, requests, subprocess
import tkinter as tk
from PIL import ImageTk, Image
path=os.getcwd()
def newlog():
    open(path+"\\old.log","w")
    open(path+"\\latest.log","w")
    os.remove(path+"\\old.log")
    os.rename(path+"\\latest.log", path+"\\old.log")
newlog()
def log(message:str):

    logmessage="<"+str(datetime.datetime.now())+"> "+message+"\n"
    print(logmessage)
    file= open(path+"\\latest.log", "a")
    file.write(logmessage)
log("registerd function log")
try:
    import imagelib
    log("imagelib loaded")
except:
    log("imagelib missing")
    log("terminating...")
    sys.exit("no imagelib")
global version
checkversion=requests.get("https://raw.githubusercontent.com/Chaosflo677/Schedule-I-creator/main/latest-version").content
open(path+"\\temp", 'wb').write(checkversion)
latestversion=open(path+"\\temp", 'r').read()
os.remove(path+"\\temp")
try:
    import config
    version = config.version
    log("config loaded")
except:
    log("no config found loading default")
    version = 0
def saveconfig():
    configfile="version="+str(version)+"\n"
    log("new config\n\n"+configfile)
    file= open(path+"\\config.py", "w")
    log("writing config file")
    file.write(configfile)
    log("sucsessfuly wrote config file")
log("registerd function saveconfig")
log("checking version")
if version != latestversion:
    print(version)
    log("new version found")
    answer=ctypes.windll.user32.MessageBoxW(0, "would you like to update?", "not latest version", 4)
    if answer == 6:
        os.system("python "+path+"\\updater.py")
        log("updating")
        version=latestversion
saveconfig()
root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(imagelib.appimg))))
root.wm_iconphoto(False, img)
root.mainloop()