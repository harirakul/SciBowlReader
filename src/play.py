import pyttsx3
from reader import Packet
import pickle
import re
import os
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def play(p: Packet) -> None:
    engine.say("Reading science bowl questions in practice mode.")
    for q in p.questions:
        engine.say("Number " + str(q["Number"]))
        for field in ('Subject', 'Type', 'Question'):
            engine.say(q[field])

        if q['Type'] == 'Multiple Choice':
            for i in q['Options']:
                engine.say(i)
                engine.say(q['Options'][i])

        engine.runAndWait()
        ans = input('Answer: ')
        start = time.time()
        if(ans.upper() == q['Answer']):
            engine.say('Good job, that is correct.')
        else:
            engine.say(f'Sorry, that is incorrect. The correct answer is, {q["Answer"]}')
        engine.runAndWait()
        input("Press enter to continue...")

def get_info(data: str) -> tuple:    
    grp, rond = [int(val) for val in re.findall(r'\d+', data)]
    if grp < 1 or grp > len(os.listdir("sets")) + 1:
        raise FileNotFoundError(f"group{grp} does not exist")
    else:
        if rond < 1 or rond > len(os.listdir(f"sets/group{grp}")) + 1:
            raise FileNotFoundError(f"group{grp} exists, but no set{rond}")
    return grp, rond

if __name__ == "__main__":
    while True:
        data = input("URL or (<Group#>, <Set#>) of a SciBowl Packet: ")
        if data.startswith("http"):
            p = Packet(data)
        else:
            grp, rond = get_info(data)
            with open(f"sets/group{grp}/round{rond}.txt", 'rb') as f:
                p = pickle.load(f)
        play(p)