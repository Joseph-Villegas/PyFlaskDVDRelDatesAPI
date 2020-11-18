# filename: dvd_bot.py

import requests

from bs4 import BeautifulSoup


class DVDBot(object):
    """A Class to scrape dvd releases by week from the web"""

    def __init__(self):
        self.url = 'https://www.dvdsreleasedates.com'

        response = requests.get(self.url)

        self.soup = BeautifulSoup(response.content, features="lxml")

        self.releaseData = self.soup.findAll(
            attrs={'class': 'fieldtable-inner'})

    def getReleasesByWeek(self, week):
        """A function to get dvd releases by week (0-3) with release date"""
        if week > 3:
            print(f'{week} weeks ahead is to far to know :(')
            return "no date", []

        relWeek = self.releaseData[week].find(attrs={'class': 'reldate'})
        relWeek = relWeek.text.split('(')
        relWeek = relWeek[0] + ' (' + relWeek[1]

        imdbIDs = []

        for tag in self.releaseData[week].findAll(attrs={'class': 'imdblink left'}):
            imdbID = tag.find('a').attrs['href'].split('/')[4]
            imdbIDs.append(imdbID)

        dvds = []

        idIndex = 0
        for dvd in self.releaseData[week].findAll('img'):
            if 'src' in dvd.attrs:
                if dvd.attrs['src'].endswith('jpg'):
                    title = dvd.attrs['title'].replace(' DVD Release Date', '')
                    poster = dvd.attrs['src']
                    dvds.append(
                        {'title': title, 'imdbID': imdbIDs[idIndex], 'poster': poster})
                    idIndex += 1

        return relWeek, dvds
