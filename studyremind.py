import pynotify
from time import sleep

def sendmessage(title,msg):
    pynotify.init("Break")
    notice = pynotify.Notification(title,msg)
    notice.show()
    return
    

while True:
    news= "Study for exam :D"
    sendmessage("Study",news)
    sleep(900)
