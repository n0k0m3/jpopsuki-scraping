import requests
import urllib3

site = 'https://jpopsuki.eu/'
site_torrent_list = 'torrents.php?page={}&order_by=s4&order_way=ASC&action=advanced'
cookie_valid = False
number_of_pages = 5
username = ''
password = ''


def get_cookie(username, password):
    http = requests.Session()
    fields = {'username': username, 'password': password}
    http.post(site + 'login.php', fields)
    cookies_dict = http.cookies.get_dict()
    global cookie_valid
    cookie_valid = True
    return cookies_dict['PHPSESSID']


def get_html_per_page(cookie, page):
    http = urllib3.PoolManager()
    headers = {'cookie': "PHPSESSID=" + cookie}
    response = http.request("GET", site + site_torrent_list.format(page), headers=headers)
    return response.data


def scrape(username, password, number_of_pages):
    cookie = get_cookie(username, password)
    global cookie_valid
    print("First cookie requested")
    page = 0
    while page < number_of_pages:
        page += 1
        page_str = '-'.join([str((page - 1) * 50 + 1), str(page * 50)])
        if not cookie_valid:
            cookie = get_cookie(username, password)
            print("New cookie requested")
        with open('data/jpopsuki_' + str(page) + ".html", 'wb') as file:
            try:
                file.write(get_html_per_page(cookie, page))
            except:
                cookie_valid = False
                print("FAILED page", page, 'Range', page_str)
                page -= 1
                continue
            print("Done page", page, 'Range', page_str)


if __name__ == '__main__':
    scrape(username, password, number_of_pages)
