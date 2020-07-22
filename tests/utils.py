import os
import json
import requests
from pynindo.const import CHARTS_URLS, VIRAL_URL, MILESTONES_URLS


datafilename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')

SKIP_REAL = os.getenv('SKIP_REAL', True)
if isinstance(SKIP_REAL, str):
    SKIP_REAL = SKIP_REAL == 'True'

TEST_DATA = {
    'charts': {},
    'milestones': {
        'new': [],
        'past': [],
    },
    'viral': [],
}

if os.path.isfile(datafilename):
    with open(datafilename) as json_file:
        TEST_DATA = json.load(json_file)


def load_url(url):
    print('[*] url:', url)
    response = requests.get(url)
    return response.json()


def create_data():
    data = dict(TEST_DATA)
    print('load charts')
    for platform, urls in CHARTS_URLS.items():
        data['charts'][platform] = {}
        for action, url in urls.items():
            data['charts'][platform][action] = load_url(url)

    print('load viral')
    data['viral'] = load_url(VIRAL_URL)

    print('load milestones')
    for key, url in MILESTONES_URLS.items():
        data['milestones'][key] = load_url(url)

    print('save data to:', datafilename)
    with open(datafilename, 'w') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=4)


if __name__ == '__main__':
    create_data()
