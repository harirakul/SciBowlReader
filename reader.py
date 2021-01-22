from typing import final
from PyPDF2 import PdfFileReader
import io
import requests
import qparser
import pickle

class Packet():
    def __init__(self, url: str) -> None:
        r = requests.get(url)
        f = io.BytesIO(r.content)
        self.reader = PdfFileReader(f)
        self.info = self.reader.getDocumentInfo()
        self.txt = self.reader.getPage(0).extractText().strip().replace('\n','')
        self.pages = [self.reader.getPage(i) for i in range(self.reader.getNumPages())]        
        self.load_questions()
    
    def load_questions(self):
        self.questions = []
        for page in self.pages:
            self.questions.extend(qparser.parse_questions(page))

            # txt = page.extractText().strip().replace('\n','')
            # quests = re.split(r'[1-9]{1,2}\)', txt)
            # # quests = re.split(r' [1-9]\)| [1-9][1-9]\)', txt)
            # for q in quests[1:]:
            #     try:
            #         self.questions.append(qparser.parseQ(q))
            #     except:
            #         continue


if __name__ == "__main__":
    current = "sets/group4/"
    for i in range(1, 18):
        print(f"Saving Round {i}...")
        url = f'https://science.osti.gov/-/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-4/Round{i}.pdf'
        p = Packet(url)
        f = open(f"{current}round{i}.txt", 'wb')
        pickle.dump(p, f)
        f.close()
