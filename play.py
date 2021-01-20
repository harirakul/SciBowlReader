import pyttsx3
from reader import Packet

engine = pyttsx3.init()
engine.setProperty('rate', 140)

def play(url: str) -> None:
    p = Packet(url)
    for q in p.questions:
        for field in ('Subject', 'Type', 'Question'):
            engine.say(q[field])

        if q['Type'] == 'Multiple Choice':
            for i in q['Options']:
                engine.say(i)
                engine.say(q['Options'][i])

        engine.runAndWait()
        ans = input('Answer: ')
        if(ans.upper() == q['Answer']):
            engine.say('Good job, that is correct.')
        else:
            engine.say('Sorry, that is incorrect.')
        engine.runAndWait()
        input("Press enter to continue...")

if __name__ == "__main__":
    URL = input("ÜRL to SciBowl Packet: ")
    play(URL)