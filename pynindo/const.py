
PLATFORM = ['youtube', 'instagram', 'twitter', 'twitch', 'tiktok']

CHARTS_URLS = {
    'youtube': {
        'small': 'https://api.nindo.de/ranks/charts/youtube/rankViews/small',
        'likes': 'https://api.nindo.de/ranks/charts/youtube/rankLikes/big',
        'views': 'https://api.nindo.de/ranks/charts/youtube/rankViews/big',
        'subscribers': 'https://api.nindo.de/ranks/charts/youtube/rankSubGain/big',
        'rank': 'https://api.nindo.de/ranks/charts/youtube/rank/big'
    },
    'instagram': {
        'small': 'https://api.nindo.de/ranks/charts/instagram/rankLikes/small',
        'likes': 'https://api.nindo.de/ranks/charts/instagram/rankLikes/big',
        'subscribers': 'https://api.nindo.de/ranks/charts/instagram/rankSubGain/big',
        'rank': 'https://api.nindo.de/ranks/charts/instagram/rank/big',
    },
    'twitter': {
        'small': 'https://api.nindo.de/ranks/charts/twitter/rankLikes/small',
        'likes': 'https://api.nindo.de/ranks/charts/twitter/rankLikes/big',
        'retweets': 'https://api.nindo.de/ranks/charts/twitter/rankRetweets/big',
        'subscribers': 'https://api.nindo.de/ranks/charts/twitter/rankSubGain/big',
        'rank': 'https://api.nindo.de/ranks/charts/twitter/rank/big',
    },
    'twitch': {
        'small': 'https://api.nindo.de/ranks/charts/twitch/rankViewer/small',
        'views': 'https://api.nindo.de/ranks/charts/twitch/rankViewer/big',
        'peak': 'https://api.nindo.de/ranks/charts/twitch/rankPeakViewer/big',
        'subscribers': 'https://api.nindo.de/ranks/charts/twitch/rankSubGain/big',
        'rank': 'https://api.nindo.de/ranks/charts/twitch/rank/big',
    },
    'tiktok': {
        'small': 'https://api.nindo.de/ranks/charts/tiktok/rankLikes/small',
        'likes': 'https://api.nindo.de/ranks/charts/tiktok/rankLikes/big',
        'views': 'https://api.nindo.de/ranks/charts/tiktok/rankViews/big',
        'subscribers': 'https://api.nindo.de/ranks/charts/tiktok/rankSubGain/big',
        'rank': 'https://api.nindo.de/ranks/charts/tiktok/rank/big'
    },
}

MILESTONES_URLS = {
    'new': 'https://api.nindo.de/ranks/milestones',
    'past': 'https://api.nindo.de/ranks/pastMilestones',
}

VIRAL_URL = 'https://api.nindo.de/viral'

ARTIST_URLS = {
    'search': 'https://api.nindo.de/search/smart/{search}',
    'id': 'https://api.nindo.de/artist/{id}',
    'channel': 'https://api.nindo.de/channel/{platform}/{id}'
}

VIRAL_TYPES = {
    'youtube': ['likes', 'kommentare', 'views'],
    'instagram': ['likes', 'kommentare'],
    'twitter': ['likes', 'retweets'],
    'twitch': ['max. zuschauer', 'längster stream'],
    'tiktok': ['likes', 'kommentare', 'views']
}
