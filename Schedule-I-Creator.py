import os, datetime, base64, io, sys
import tkinter as tk
from PIL import ImageTk, Image
path=os.getcwd()+"\\SICreator\\"
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

try:
    import config
    version = config.version
    log("config loaded")
except:
    log("no config found loading default")
    version = "0.0.0"

def saveconfig():
    configfile="version="+str(version)+"\n"
    log("new config\n\n"+configfile)
    file= open(path+"\\config.py", "w")
    log("writing config file")
    file.write(configfile)
    log("sucsessfuly wrote config file")
log("registerd function saveconfig")
def update():
    os.system("python "+path+"\\updater.py")
    log("updating")
log("registerd function update")
saveconfig()
root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(imagelib.appimg))))
root.wm_iconphoto(False, img)
root.mainloop()