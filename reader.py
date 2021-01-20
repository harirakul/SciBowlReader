from PyPDF2 import PdfFileReader
import re, io
import requests
import qparser

class Packet():
    def __init__(self, url: str) -> None:
        r = requests.get(url)
        f = io.BytesIO(r.content)
        self.reader = PdfFileReader(f)
        self.info = self.reader.getDocumentInfo()
        self.title = self.info['/Title']
        self.pages = [self.reader.getPage(i) for i in range(self.reader.getNumPages())]        
        self.load_questions()
    
    def load_questions(self):
        self.questions = []
        for page in self.pages:
            txt = page.extractText().strip().replace('\n','')
            quests = re.split(' [1-9]\)| [1-9][1-9]\)', txt)
            for q in quests[1:]:
                try:
                    self.questions.append(qparser.parseQ(q))
                except:
                    continue


if __name__ == "__main__":
    url = 'https://science.osti.gov/-/media/wdts/nsb/pdf/HS-Sample-Questions/Sample-Set-1/round5.pdf'
    p = Packet(url)
    print(len(p.questions))