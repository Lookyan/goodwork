import requests
from HTMLParser import HTMLParser

h = HTMLParser()

START_ID = 1
COUNT = 3000
STATS = {
    'successfully': 0,
    'failed': 0
}


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def get_company(company_id):
    page = requests.get('https://api.hh.ru/employers/%d' % company_id,
                        headers={'User-Agent': 'ISOR/1.0 (support@isor.ru)'})
    if page.status_code != 200:
        print 'cant get company from hh'
        return None
    return page.json()


def main():
    start = START_ID
    for i in xrange(COUNT):
        response = get_company(start)
        start += 1
        if not response:
            STATS['failed'] += 1
            continue
        # get logo
        no_logo = False
        try:
            logo_url = response['logo_urls']['original']
        except (IndexError, TypeError):
            no_logo = True
        if not no_logo:
            logo = requests.get(logo_url)
        payload = {
            'name': response['name'],
            'description': strip_tags(h.unescape(response['description'])).strip(),  # TODO: TypeError handling
            'website': response['site_url']
        }
        files = None
        if not no_logo:
            files = {
                'logo': logo.content
            }
        res = requests.post('http://localhost/api/company/add/', data=payload, files=files)
        if res.status_code == 200:
            STATS['successfully'] += 1
        else:
            STATS['failed'] += 1
        print res.status_code

    print '----------'
    print STATS
    print '----------'

if __name__ == '__main__':
    main()