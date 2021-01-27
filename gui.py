import tkinter as tk
import pickle, os

def font(size: float) -> tuple:
    return ("Comic Sans MS", size)

def info(grp: int, rond: int):
    if grp < 1 or grp > len(os.listdir("sets")) + 1:
        raise FileNotFoundError(f"group{grp} does not exist")
    elif rond < 1 or rond > len(os.listdir(f"sets/group{grp}")) + 1:
        raise FileNotFoundError(f"group{grp} exists, but no set{rond}")
    with open(f"sets/group{grp}/round{rond}.txt", 'rb') as f:
        p = pickle.load(f)
    return p

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
    packet = info(int(chosen_set), int(chosen_round))
    print(packet.questions)

sets = [str(i) for i in range(1, 13)]
rounds = [str(i) for i in range(1, 18)]

root = tk.Tk()
root.title("SciBowlReader")

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