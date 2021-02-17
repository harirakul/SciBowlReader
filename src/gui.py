import tkinter as tk
import pickle, os
import pyttsx3
import threading

def font(size: float) -> tuple:
    return ("Comic Sans MS", size)

def load_packet(grp: int, rond: int):
    if grp < 1 or grp > len(os.listdir("sets")) + 1:
        raise FileNotFoundError(f"group{grp} does not exist")
    elif rond < 1 or rond > len(os.listdir(f"sets/group{grp}")) + 1:
        raise FileNotFoundError(f"group{grp} exists, but no set{rond}")
    with open(f"sets/group{grp}/round{rond}.txt", 'rb') as f:
        p = pickle.load(f)
    return p

def text(root, txt: str, size: float) -> tk.Label:
    return tk.Label(
     root, text=txt, bg="#0F6636", fg="white", font=font(size)
    )

def text_by_var(root, var: tk.StringVar, size = 14) -> tk.Label:
    return tk.Label(root, textvariable=var, bg="#0F6636", fg="white", font=font(size))

############# GAMEPLAY SCREEN #############

class GUI(threading.Thread):
    def __init__(self, grp: int, rond: int) -> None:
        threading.Thread.__init__(self)
        self.grp = grp
        self.rond = rond    
        self.packet = load_packet(grp, rond)  
        self.engine = pyttsx3.init()
        self.start()
        self.greet()

    def run(self):
        self.root = tk.Tk()
        self.root.title(f"Science Bowl Practice: Set {self.grp}, Round {self.rond}")
        self.height = 300; self.width = 600
        self.canvas = tk.Canvas(self.root, bg="#0F6636", height=self.height, width=self.width)
        self.create_vars(kwargs={
            "Question #": (160, 10),
            "Score": (self.width - 50, 10),
            "Type": (70, self.height/3),
            "Subject": (self.width - 200, self.height/3)
        })
        self.canvas.pack()
        self.root.mainloop()
    
    def create_vars(self, kwargs) -> None:
        self.vars = {i: tk.StringVar(value="None") for i in kwargs}
        for arg in kwargs:
            x, y = kwargs[arg][0], kwargs[arg][1]
            text_by_var(self.root, self.vars[arg]).place(x = x, y = y)
            text(self.root, f"{arg}: ", 14).place(x = x - len(arg)*15, y=y)

    def greet(self) -> None:
        self.engine.say(f"Welcome. Commencing Set {self.grp}, Round {self.rond}")
        self.engine.runAndWait()

############# CONFIGURATION SCREEN #############
WIDTH = 300
HEIGHT = 175
chosen_set = '1'
chosen_round = '1'

def update_set(new_set): 
    global chosen_set
    chosen_set = new_set

def update_round(new_round): 
    global chosen_round
    chosen_round = new_round

def start() -> None:
    root.destroy()
    GUI(int(chosen_set), int(chosen_round))

sets = [str(i) for i in range(1, 13)]
rounds = [str(i) for i in range(1, 18)]

root = tk.Tk()
root.title("Configure...")

C = tk.Canvas(root, bg="#0F6636", height=HEIGHT, width=WIDTH)

curr_set = tk.StringVar(root)
curr_round = tk.StringVar(root)
curr_set.set('1')
curr_round.set('1')

choose_set = tk.OptionMenu(root, curr_set, *sets, command=update_set)
choose_round = tk.OptionMenu(root, curr_round, *sets, command=update_round)
title = tk.Label(
    root, text="Science Bowl Reader", bg="#0F6636", fg="white", font=font(18)
)
practice = tk.Button(
    root,
    text="Practice",
    bg="orange",
    fg="white",
    font="sans 12 bold",
    width=20,
    command=start
)

title.place(x=WIDTH/2, y=HEIGHT/6, anchor=tk.CENTER)
tk.Label(root, text = "Set #: ", bg="#0F6636", fg="white", font=font(14)).place(x = WIDTH/5, y = HEIGHT/2.5, anchor="w")
choose_set.place(x = WIDTH*3/5, y = HEIGHT/2.5, anchor="w")

tk.Label(root, text = "Round #: ", bg="#0F6636", fg="white", font=font(14)).place(x = WIDTH/5, y = HEIGHT*6/9, anchor="w")
choose_round.place(x = WIDTH*3/5, y = HEIGHT*6/9, anchor="w")
practice.place(x=WIDTH/2, y=HEIGHT*8/9, anchor=tk.CENTER)
C.pack()

root.mainloop()
