from lotto.lottery import lotto649
from lotto.repository import lotto649Repo
from datetime import datetime

def termlotto(term):
    tmp = term
    while tmp > 0:
        lottos = lotto649.scrapingByTerm(tmp)
        if lottos is not None:
            for k, v in lottos.items():
                repo.add(k, v[0], v[1], v[2], v[3], v[4], v[5], v[6])
            tmp += 1
        else:
            tmp = -1

def datelotto():
    yyy = 103
    mm = 1
    while True:
        lottos = lotto649.scrapingByDate(yyy, mm)
        if lottos is not None:
            for k, v in lottos.items():
                repo.add(k, v[0], v[1], v[2], v[3], v[4], v[5], v[6])
        else:
            break
        mm += 1
        if mm == 13:
            mm = 1
            yyy += 1

lotto649 = lotto649()
repo = lotto649Repo()
term = repo.first()
if term is None:
    datelotto()
else:
    tmp = term["Term"] + 1
    termlotto(tmp)