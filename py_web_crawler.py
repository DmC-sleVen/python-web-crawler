import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

class MietenFetcher():
    def fetch(self):
        url = "https://www.immobilienscout24.de/Suche/de/baden-wuerttemberg/freiburg-im-breisgau/wohnung-kaufen"
        
        while url != "":
            print(url)
            time.sleep(1)
            r = requests.get(url)
            dok = BeautifulSoup(r.text, "html.parser")    

            
            for i in dok.select(".font-nowrap"):
                splitted = i.text.split()
                if splitted[1]=="€":
                    Mieten = splitted[0]
                    print(Mieten, "€")
                    
                

            next_page = dok.select_one(".icon-arrow-forward")
            if next_page:
                next_page = next_page.attrs["href"]
                baseurl = "https://www.immobilienscout24.de"
                nexturl = urljoin(baseurl, next_page)
                url = nexturl
            else:
                url = ""
            


    def jahresnettokaltmiete(self):
        print("This is has to be done! An issue is already open!")
        print("This is a test")
        return


        

fetcher=MietenFetcher()
fetcher.fetch()
for element in fetcher.fetch():
    print(element)

    
