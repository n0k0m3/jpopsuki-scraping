from utils import scraping, processing, download
import os

number_of_pages = 5
username = 'USERNAME'
password = 'PASSWORD'

if __name__ == '__main__':
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.listdir("data"):
        scraping.scrape(username, password, number_of_pages)
    if 'download_links.txt' not in os.listdir():
        processing.main()
    #download.main()