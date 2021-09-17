import json

def readJson(file: str) -> dict:
    x = open(file, 'r', encoding='utf-8')
    y = json.load(x)
    return y

def saveJson() -> None:
    json_f['previous'] = selected
    with open(conf_f, 'w', encoding='utf-8') as f:
        json.dump(json_f, f)
        f.close()


conf_f = "conf.json" # path to conf.json
json_f = readJson(conf_f)

# -----------------------------

import pyperclip # install with pip 
from tkinter import (
    Tk,
    Entry,
    Label
)

# import converter modules here
import binary_calculator as bc
import ipv4_calculator as ipc
from random import randint

def exitProgram() -> None:
    saveJson()
    exit(root.destroy())

def returnPressed(inp) -> None:
    try:
        pyperclip.copy(eval(selected[0][selected[1]][1].format(entry.get())))
    except:
        pyperclip.copy("ERROR")
    exitProgram()

def keyPressed(inp) -> None:
    inp = inp.keysym
    global selected, selectable_range
    if inp == 'Left':
        selected = [json_f['converts'], selected[2], selected[2]]
        selectable_range = len(modes)

    elif inp == 'Right':
        if selected[0] != json_f['converts']: return
        selected[2] = selected[1]
        selectable_range = len(json_f['converts'][modes[selected[1]]])
        selected = [json_f['converts'][modes[selected[1]]], 0, selected[2]]

    elif inp == 'Up':
        if selected[1] <= 0: return
        selected[1] -= 1

    elif inp == 'Down':
        if selected[1] >= selectable_range - 1: return
        selected[1] += 1

    elif inp == 'Escape':
        exitProgram()

    else:
        return

    updateLabel()

def updateLabel() -> None:
    show = []
    try:
        for i in selected[0].keys(): show.append(i)
    except:
        for i in selected[0]: show.append(i[0])

    label.configure(text=show[selected[1]])


json_root = json_f['converts']
selected = json_f['previous']
modes = []
for i in json_f['converts'].keys():
    modes.append(i)
selectable_range = len(json_f['converts'][modes[selected[2]]])

root = Tk()
root.bind('<Key>', keyPressed)
root.attributes('-topmost', True)
root.overrideredirect(True)

size = (60, 40)
curpos = (root.winfo_pointerx() - round(size[0] / 2), root.winfo_pointery() - round(size[1] / 1.3))
root.geometry("{}x{}+{}+{}".format(*size, *curpos))

label = Label(root)
updateLabel()
label.pack(side='top')

entry = Entry(root)
entry.bind('<Return>', returnPressed)
entry.pack(side='top')


root.mainloop()
