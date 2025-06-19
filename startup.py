from tkinter import Tk, Button, Label
from subprocess import Popen
from psutil import Process
from os import path

manager = path.realpath(__file__).replace('startup.py', 'manage.py')

def kill(proc_pid):
    process = Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

def start_server_func():
    global proc

    proc = Popen(['python', manager, 'runserver'])

root = Tk()

header = Label(text = 'Manage System', font = 'Calibri 32')

proc = None

start_server = Button(root, text = 'Start Server', command = lambda: start_server_func(), font = 'Calibri 18')
stop_server = Button(root, text = 'Stop Server', command = lambda: kill(proc.pid), font = 'Calibri 18')


header.pack(pady = 10, padx = 10)
start_server.pack(pady = (0, 5))
stop_server.pack(pady = (0, 10))

root.mainloop()