import os, datetime, base64, io, sys, requests
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

try:
    import config
    log("config loaded")
except:
    log("no config found loading default")

def saveconfig():
    configfile="\n"
    log("new config\n\n"+configfile)
    file= open(path+"\\config.py", "w")
    log("writing config file")
    file.write(configfile)
    log("sucsessfuly wrote config file")
log("registerd function saveconfig")
def update():
    
    open("updater.py", 'wb').write(requests.get("https://raw.githubusercontent.com/Chaosflo677/Schedule-I-creator/main/versions/latest/updater.py", allow_redirects=True).content)
    log("updating updater")
    os.system("python "+path+"\\updater.py")
    log("updating")
    sys.exit()
log("registerd function update")
saveconfig()
root = tk.Tk()
img = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(imagelib.appimg))))
root.wm_iconphoto(False, img)
menu_bar = tk.Menu(root)
workspaces = tk.Menu(menu_bar, tearoff=0)
SICreatorconfig = tk.Menu(menu_bar, tearoff=0)
workspaces.add_command(label="new")
workspaces.add_command(label="delete")
SICreatorconfig.add_command(label="wiki")
SICreatorconfig.add_command(label="update")
menu_bar.add_cascade(label="workspaces", menu=workspaces)
menu_bar.add_cascade(label="SICreator", menu=SICreatorconfig)
root.config(menu=menu_bar)
root.mainloop()