import wget


def main():
    with open('download_links.txt', 'r') as file:
        url_list = [url.rstrip('\n') for url in file.readlines()]
        print(url_list)
        for url in url_list:
            wget.download(url)


if __name__ == '__main__':
    main()
