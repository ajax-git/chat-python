from tkinter import *
import socket
import _thread

ADRESS = '192.168.2.244'
PORT = 12345
BUFOR = 1000

# client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# server
listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind( ('0.0.0.0', PORT) )
 
root = Tk()
root.title("Chat")
 
def SendMessage():
    send = e.get()
    e.delete(0, END)
    client.sendto ( send.encode('utf8'), (ADRESS, PORT) )

def GetMessages():
    while True:
        data, client = listener.recvfrom( BUFOR )
        txt.insert(END, client[0] + ": " + data.decode('utf8') + "\n")
        

txt = Text(root, bg="#FFFFFF", fg="#000000", font="Arial 11", width=60)
txt.grid(row=1, column=0, columnspan=2)
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(root, bg="#FFFFFF", fg="#000000", font="Arial 11", width=55)
e.grid(row=2, column=0)
 
send = Button(root, text="Wyślij", font="Arial 12", bg="#B2C7C6",
              command=SendMessage).grid(row=2, column=1)

_thread.start_new_thread(GetMessages, () ) 
root.mainloop()