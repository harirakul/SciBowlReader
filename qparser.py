import re

def parseQ(q: str) -> dict:
    splitted = q.split(' ')
    subj = splitted[2].strip()
    typ = splitted[4] + " " + splitted[5]
    quest = q[q.find(typ)+len(typ):q.find('ANSWER')].strip()
    end = q[q.find('ANSWER')+6:]
    rdict = {"Subject": subj, "Type": typ, "Question": quest}
    ans = re.split(': | \(| [BT]O', end)[1].strip()
    rdict.update({"Answer": ans})
    
    if typ == "Multiple Choice":
        options = q[q.find(':  W')+3:q.find('ANSWER')]
        options = re.split('[W-Z]\)  ', options)[1:]
        options = [i.strip() for i in options]
        keys = ["W", "X", "Y", "Z"]
        options = dict(zip(keys, options))
        quest = quest[:quest.find(':  W')].strip()
        ans = end[3]
        rdict.update({"Question": quest, "Options": options, "Answer": ans})

    return rdict