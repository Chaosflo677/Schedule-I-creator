import requests,os,base64,io,imagelib,sys,tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
path=os.getcwd()
global version
version="latest"
sourcerepo="https://raw.githubusercontent.com/Chaosflo677/Schedule-I-creator/main/versions/"
def getfile(file):
    r = requests.get(sourcerepo+version+"/"+file+".py", allow_redirects=True)
    open(file+".py", 'wb').write(r.content)
def update():
    getfile("imagelib")
    getfile("Schedule-I-Creator")
    sys.exit()
def on_selection(event):
    selected_indices = versions.curselection()
    for index in selected_indices:
        version=versions.get(index)
        button['text'] = 'install '+version
updater=tk.Tk()
img = ImageTk.PhotoImage(Image.open(io.BytesIO(base64.b64decode(imagelib.appimg))))
updater.wm_iconphoto(False, img)
updater.title("updater")
updater.geometry("500x200")
updater.resizable(False,False)
tk.Label(updater,text="Select a version to install",font=font.Font(size=24)).pack()
versions=tk.Listbox(updater,height=5)
versions.pack()
versions.insert(tk.END, "latest")
versions.insert(tk.END, "1.0.0")
versions.bind("<<ListboxSelect>>", on_selection)
button = tk.Button(updater,
	text = 'latest',
	command = update)  
button.pack()
updater.mainloop()