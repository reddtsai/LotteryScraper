import urllib.request
import urllib.error
import urllib.parse
import re
from bs4 import BeautifulSoup

class lotto649:
    def __init__(self):
        self.url = "https://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx"
        self.__VIEWSTATE = None
        self.__VIEWSTATEGENERATOR = None
        self.__EVENTVALIDATION = None
        self._getViewData()

    def _get(self):
        try:
            resp = urllib.request.urlopen(self.url).read()
        except urllib.error.HTTPError:
            # print(e.code)
            return None
        else:
            html = BeautifulSoup(resp, "html.parser")
            return html

    def _post(self, data):
        formData = urllib.parse.urlencode(data).encode("ascii")
        try:
            resp = urllib.request.urlopen(self.url, formData).read()
        except urllib.error.HTTPError:
            # print(e.code)
            return None
        else:
            html = BeautifulSoup(resp, "html.parser")
            return html
    
    def _getViewData(self):
        view = self._get()
        self.__VIEWSTATE = view.find("input", id="__VIEWSTATE")["value"]
        self.__VIEWSTATEGENERATOR = view.find("input", id="__VIEWSTATEGENERATOR")["value"]
        self.__EVENTVALIDATION = view.find("input", id="__EVENTVALIDATION")["value"]

    def scrapingByTerm(self, term):
        viewData = {
            "__VIEWSTATE": self.__VIEWSTATE,
            "__VIEWSTATEGENERATOR": self.__VIEWSTATEGENERATOR,
            "__EVENTVALIDATION": self.__EVENTVALIDATION,
            "Lotto649Control_history$DropDownList1": 2,
            "Lotto649Control_history$chk": "radNO",
            "Lotto649Control_history$txtNO": term,
            "Lotto649Control_history$btnSubmit": "查詢"
        }
        html = self._post(viewData)
        lotto = html.find("table", id="Lotto649Control_history_dlQuery")
        if lotto is not None:
            tables = lotto.find_all('table')
            lottos = dict()
            for table in tables:
                term = table.find("span", {"id": re.compile("Lotto649Control_history_dlQuery_L649_DrawTerm_[0-9]$")}).text
                lotto = list()
                # 大小順序
                # num = table.find_all("span", {"id": re.compile("Lotto649Control_history_dlQuery_No[1-6]_[0-9]$")})
                # 開出順序
                num = table.find_all("span", {"id": re.compile("Lotto649Control_history_dlQuery_SNo[1-6]_[0-9]$")})
                for n in num:
                    lotto.append(n.text)
                sNum = table.find("span", id="SuperLotto638Control_history1_dlQuery_No7_0").text
                lotto.append(sNum)
                lottos.update({term: lotto})
            return lottos
        return None

    def scrapingByDate(self, yyy, mm):
        viewData = {
            "__VIEWSTATE": self.__VIEWSTATE,
            "__VIEWSTATEGENERATOR": self.__VIEWSTATEGENERATOR,
            "__EVENTVALIDATION": self.__EVENTVALIDATION,
            "Lotto649Control_history$DropDownList1": 2,
            "Lotto649Control_history$chk": "radYM",
            "Lotto649Control_history$dropYear": yyy,
            "Lotto649Control_history$dropMonth": mm,
            "Lotto649Control_history$btnSubmit": "查詢"
        }
        html = self._post(viewData)
        lotto = html.find("table", id="Lotto649Control_history_dlQuery")
        if lotto is not None:
            tables = lotto.find_all('table')
            lottos = dict()
            for table in tables:
                term = table.find("span", {"id": re.compile(r"Lotto649Control_history_dlQuery_L649_DrawTerm_\d*$")}).text
                lotto = list()
                # 大小順序
                # num = table.find_all("span", {"id": re.compile("Lotto649Control_history_dlQuery_No[1-6]_[0-9]$")})
                # 開出順序
                num = table.find_all("span", {"id": re.compile(r"Lotto649Control_history_dlQuery_SNo[1-6]_\d*$")})
                for n in num:
                    lotto.append(n.text)
                sNum = table.find("span", id="SuperLotto638Control_history1_dlQuery_No7_0").text
                lotto.append(sNum)
                lottos.update({term: lotto})
            return lottos
        return None

if __name__ == '__main__':
    lotto649 = lotto649()
    lottos = lotto649.scrapingByTerm(103000001)
    if lottos is not None:
        for k, v in sorted(lottos.items()):
            print(k, "-", v)
