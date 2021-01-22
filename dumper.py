from bs4 import BeautifulSoup
import pickle
from reader import Packet

with open('res\SciBowl.txt', 'r') as f:
    ht = f.read()
    soup = BeautifulSoup(ht)

    group = 0
    prefix = "https://science.osti.gov"
    for ul in soup.find_all('ul'):
        group += 1
        rnd = 0
        for li in ul.find_all('li'):
            rnd += 1
            url = prefix + li.find('a')['href']

            p = Packet(url)
            with open(f"sets/group{group}/round{rnd}.txt", 'wb') as out:
                pickle.dump(p, out)
