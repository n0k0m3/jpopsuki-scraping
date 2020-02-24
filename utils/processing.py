import re
import os
from bs4 import BeautifulSoup


def main():
    with open('download_links.txt', 'w+') as dl:
        for filename in os.listdir('data'):
            with open('data/' + filename, 'rb') as file:
                html = file.read()
                soup = BeautifulSoup(html, features="lxml")
                for a_class in soup.find_all('a'):
                    link_part = a_class.get('href')
                    if link_part is not None and re.search('action=download&id=\d', link_part) is not None:
                        url = "https://jpopsuki.eu/" + link_part
                        dl.writelines(url + "\n")


if __name__ == '__main__':
    main()
