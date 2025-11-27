import subprocess,sys,requests,os
path=os.getcwd()
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("pillow")
version:str
sourcerepo="https://raw.githubusercontent.com/Chaosflo677/Schedule-I-creator/main/versions/"+version+"/"
def getfile(file):
    r = requests.get(sourcerepo+file+".py", allow_redirects=True)
    open(file+".py", 'wb').write(r.content)
getfile("imagelib")
getfile("Schedule-I-Creator")