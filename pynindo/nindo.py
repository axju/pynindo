import requests
from pynindo.const import CHARTS_URLS, VIRAL_URL, MILESTONES_URLS, ARTIST_URLS


class Concisely:
    """docstring for Concisely."""

    def __init__(self, data=None, levels=None):
        super(Concisely, self).__init__()
        self.data = data or {}
        self.levels = levels or []

    def load_data(self):
        self.data = {}

    def __getitem__(self, name):
        if not self.data:
            self.load_data()
        if name in self.levels or name in self.data:
            return self.__class__(self.data[name], list(self.levels + [name]))
        return None

    def __getattr__(self, name):
        return self[name]

    def __len__(self):
        return len(self.json())

    def __repr__(self):
        return str(self.data)

    def json(self):
        if not self.data:
            self.load_data()


class Charts(Concisely):

    def __repr__(self):
        result = ''
        for item in self.json():
            if 'platform' in item:
                result += '{:>10} | '.format(item['platform'])
            result += '{:>3} {:>10} {}\n'.format(item['rank'], item['value'], item['artistName'])
        return result

    def load_data(self):
        self.data = CHARTS_URLS

    def json(self):
        super().json()
        if isinstance(self.data, str) or len(self.levels) == 2:
            response = requests.get(self.data)
            return response.json()
        if len(self.levels) == 1:
            response = requests.get(self.data['small'])
            return response.json()
        if len(self.levels) == 0:
            result = []
            for platform, items in self.data.items():
                response = requests.get(items['small'])
                for item in response.json():
                    result.append(dict(item, platform=platform))
            return result
        return {}


class Viral(Concisely):
    """docstring for Viral."""

    def __repr__(self):
        result = ''
        for item in self.json():
            for name in ['platform', 'type']:
                if name in item:
                    result += '{:>20} | '.format(name + ':' + item[name])
            result += '{:>10} {}\n'.format(item['value'], item['_post']['_channel']['_artist']['name'])
        return result

    def load_data(self):
        response = requests.get(VIRAL_URL)
        for item in response.json():
            self.data[item['platform']] = self.data.get(item['platform'], {})
            self.data[item['platform']][item['type']] = item

    def json(self):
        super().json()
        if len(self.levels) == 0:
            return [dict(item, type=type, platform=p) for p, items in self.data.items() for type, item in items.items()]
        if len(self.levels) == 1:
            return [dict(item, type=type) for type, item in self.data.items()]
        if len(self.levels) == 2:
            return [self.data]
        return None


class Milestones(Concisely):
    """docstring for Milestones."""

    def __repr__(self):
        result = ''
        for item in self.json():
            for name in ['platform', 'type']:
                if name in item:
                    result += '{:>20} | '.format(name + ':' + item[name])
            result += '{:>10} {}\n'.format(item['currentSubs'], item['_channel']['_artist']['name'])
        return result

    def load_data(self):
        for kind, url in MILESTONES_URLS.items():
            self.data[kind] = {}
            response = requests.get(url)
            for item in response.json():
                platform = item['_channel']['platform']
                self.data[kind][platform] = self.data[kind].get(platform, [])
                self.data[kind][platform].append(item)

    def json(self):
        super().json()
        if len(self.levels) == 0:
            result = []
            for kind, data in self.data.items():
                for platform, items in data.items():
                    for item in items:
                        result.append(dict(item, type=kind, platform=platform))
            return result
        if len(self.levels) == 1:
            return [dict(item, platform=platform) for platform, items in self.data.items() for item in items]
        if len(self.levels) == 2:
            return self.data
        return None


class Artist:

    def __init__(self, key=None):
        super(Artist, self).__init__()
        self.data = {}
        if key:
            self.load_artist(key)

    def __getitem__(self, key):
        return Artist(key)

    def __getattr__(self, key):
        return self[key]

    def __repr__(self):
        result = '{} [{}]\n'.format(self.data.get('name', 'unknown id'), len(self.data['channels']))
        for channel in self.data['channels']:
            result += '{:>10} | {} - {}\n'.format(channel['platform'], channel['rank'], channel['name'])
        return result

    def load_artist(self, key):
        response = requests.get(ARTIST_URLS['id'].format(id=key))
        self.data = response.json()
        self.data['channels'] = []
        for channel in self.data.get('_channels', []):
            response = requests.get(ARTIST_URLS['channel'].format(id=channel['id'], platform=channel['platform']))
            channel_data = response.json()
            self.data['channels'].append(channel_data)

    def json(self):
        return self.data


class SearchArtist:
    """docstring for ApiArtist."""

    def __init__(self, data=None):
        super(SearchArtist, self).__init__()
        self.data = data or []

    def __repr__(self):
        return ''.join(['[{}] {}\n'.format(len(item['_channels']), item['name']) for item in self.json()])

    def __getitem__(self, name):
        if len(self.data) == 0:
            response = requests.get(ARTIST_URLS['search'].format(search=name))
            data = response.json()
            return SearchArtist(data)

        if name == 'list':
            return SearchArtist(self.data)

        if name == 'first':
            return Artist(self.data[0]['id'])
        if name == 'last':
            return Artist(self.data[-1]['id'])
        if isinstance(name, int) or (isinstance(name, str) and name.isdigit()):
            return Artist(self.data[int(name)]['id'])
        return None

    def __getattr__(self, name):
        return self[name]

    def count(self):
        return len(self.data)

    def json(self):
        return self.data


class Api:
    """docstring for Api."""
    artist = Artist()
    charts = Charts()
    viral = Viral()
    milestones = Milestones()
    search = SearchArtist()

    def __call__(self, *args, call=False):
        func = getattr(self, args[0])
        for arg in args[1:]:
            func = getattr(func, arg)
        if call:
            return func()
        return func

    def __getitem__(self, name):
        return getattr(self, name)
