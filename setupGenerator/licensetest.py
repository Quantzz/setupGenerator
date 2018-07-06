import bs4 as bs
import requests

def getLicens(license):
    r = requests.get("https://spdx.org/licenses/").text
    soup = bs.BeautifulSoup(r, 'lxml')


