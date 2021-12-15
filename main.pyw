import json
import pyperclip
from tkinter import (
    Tk,
    Label,
    Entry,
    messagebox as mb
)

# converters
import binary_calculator as bc
import ipv4_calculator as ipc
from random import randint


class Node:
    def __init__(self, parent=None, title=None, function=None) -> None:
        self.title = title
        self.function = function

        self.parent = parent
        self.children = []

    def addChildNode(self, title=None, function=None):
        self.children.append(self, title, function)


class Window(Tk):
    def __init__(self, file: str) -> None:
        super().__init__()

        self.attributes('-topmost', True)
        self.overrideredirect(True)
        size = (60, 40)
        curpos = (self.winfo_pointerx() -
                  round(size[0] / 2), self.winfo_pointery() - round(size[1] / 1.3))
        self.geometry("{}x{}+{}+{}".format(*size, *curpos))

        self.file = file
        self.data = self.loadJson()
        self.root = self.build(None, 'converts', self.data['converts'])
        self.selected = self.root
        self.bind('<Key>', self.tranverse)
        self.bind('<Return>', self.use)

        self.label = Label(text=self.selected.title)
        self.entry = Entry()

        self.label.pack(side='top')
        self.entry.pack(side='top')

    def use(self, inp=None) -> None:
        if isinstance(self.selected.function, str):
            try:
                e = self.selected.function.format(self.entry.get())
                pyperclip.copy(eval(e))
            except:
                mb.showerror(
                    'Error', f'There was an error when trying "{self.selected.title}" with "{self.entry.get()}"')
                pyperclip.copy('')
            self.destroy()

    def updateSelected(self):
        self.label.configure(text=self.selected.title)

    def tranverse(self, inp) -> Node:
        if inp.keysym == "Left":
            if self.selected.parent != None:
                self.selected = self.selected.parent

        elif inp.keysym == "Right":
            if len(self.selected.children):
                self.selected = self.selected.children[0]

        elif inp.keysym == "Up":
            if self.selected.parent != None:
                temp = self.selected.parent
                selectedindex = temp.children.index(self.selected) - 1
                if selectedindex < 0:
                    self.selected = temp.children[len(temp.children) - 1]
                else:
                    self.selected = temp.children[selectedindex]

        elif inp.keysym == "Down":
            if self.selected.parent != None:
                temp = self.selected.parent
                selectedindex = temp.children.index(self.selected) + 1
                if selectedindex > len(temp.children) - 1:
                    self.selected = temp.children[0]
                else:
                    self.selected = temp.children[selectedindex]

        self.updateSelected()

    def build(self, parent: Node, title: str, function) -> Node:
        if isinstance(function, (dict, list)):
            temp = Node(parent, title)
            if parent != None:
                parent.children.append(temp)
            if isinstance(function, dict):
                for k, v in function.items():
                    self.build(temp, k, v)
            else:
                for l in function:
                    self.build(temp, l[0], l[1])
            return temp
        else:
            parent.children.append(Node(parent, title, function))

    def saveJson(self):
        self.data['previous'] = self.selected.title

        with open(self.file, 'w', encoding='utf-8') as j:
            json.dump(self.data, j)

    def loadJson(self):
        with open(self.file, 'r', encoding='utf-8') as j:
            return json.load(j)


def main():
    window = Window('conf.json')
    window.mainloop()


if __name__ == "__main__":
    main()
