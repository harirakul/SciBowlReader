import re
import PyPDF2

def extract_questions(page: PyPDF2.pdf.PageObject) -> list:
    txt = page.extractText().strip().replace('\n','')
    matches = list(re.finditer(r' [1-9]\)\s+[A-Z][A-Z]| [1-9][1-9]\)\s+[A-Z][A-Z]| [1-9]\.\s+[A-Z][A-Z]| [1-9][1-9]\.\s+[A-Z][A-Z]', txt))
    questions = []
    for i in range(len(matches)):
        end = len(txt) if i == len(matches) - 1 else matches[i+1].end()
        q = txt[matches[i].start():end]
        questions.append(q)
    return [x.strip() for x in questions]

def parse_questions(page: PyPDF2.pdf.PageObject) -> list:
    rlist = []
    for q in extract_questions(page):
        try:
            qdict = {}
            splitted = re.split('\s+', q)

            try: num = int(splitted[0][:2])
            except:num = int(splitted[0][0])
            typnums = [2, 3]

            if splitted[1] == "EARTH": 
                subj = "EARTH AND SPACE"
                typnums = [4, 5]
            else: 
                subj = splitted[1]

            typ = splitted[typnums[0]] + " " + splitted[typnums[1]]

            qdict = {'Number': num, 'Subject': subj, 'Type': typ}

            if typ == 'Multiple Choice':
                quest = q[q.find(typ) + len(typ):q.find('W)')].strip()
                opts = re.split(r'[W-Z]\)', q[q.find('W)'):q.find('ANS')])[1:]
                opts = dict(zip(["W", "X", "Y", "Z"], [x.strip() for x in opts]))
                ans = re.search(r'[W-Z]\)', q[q.find('ANSWER')+7:]).group(0)[0]
                qdict.update({"Question": quest, "Options": opts, "Answer": ans})

            else: #Short Answer
                quest = q[q.find(typ) + len(typ):q.find('ANS')].strip()
                ans = q[q.find('ANSWER')+6:].strip()
                ans = re.split(r'\: | \(| [BT]O|\? ', ans)[1].strip()
                qdict.update({"Question": quest, "Answer": ans})
        except:
            continue

        rlist.append(qdict)

    return rlist

# def parseQ(q: str) -> dict:
#     splitted = re.split('\s+', q)
#     subj = splitted[2].strip()
#     typ = splitted[4] + " " + splitted[5]
#     quest = q[q.find(typ)+len(typ):q.find('ANSWER')].strip()
#     end = q[q.find('ANSWER')+6:]
#     rdict = {"Subject": subj, "Type": typ, "Question": quest}
#     ans = re.split(r': | \(| [BT]O', end)[1].strip()
#     rdict.update({"Answer": ans})
    
#     if typ == "Multiple Choice":
#         options = q[q.find(':  W')+3:q.find('ANSWER')]
#         options = re.split('[W-Z]\)  ', options)[1:]
#         options = [i.strip() for i in options]
#         keys = ["W", "X", "Y", "Z"]
#         options = dict(zip(keys, options))
#         quest = quest[:quest.find(':  W')].strip()
#         ans = end[3]
#         rdict.update({"Question": quest, "Options": options, "Answer": ans})

#     return rdict

if __name__ == "__main__":
    from reader import Packet
    p = Packet('https://science.osti.gov/-/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-7/ROUND-11.pdf?la=en&hash=E794D6EEB4B96471BBF8E40970483D61FD848B4E')
    print(p.questions)