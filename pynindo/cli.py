from argparse import ArgumentParser
from pynindo import __version__, api
from pynindo.const import PLATFORM, CHARTS_URLS, VIRAL_TYPES


def create_parser():
    """Create the parser"""
    parser = ArgumentParser(
        description='The cli for the pynindo api.',
        epilog='pynindo {} by AxJu'.format(__version__),
    )
    parser.add_argument(
        '-v', '--verbose', action='count', default=0,
        help='verbosity (-v, -vv, etc)'
    )
    subparsers = parser.add_subparsers(title='required commands', help='Select one of:', dest='command')

    parser_charts = subparsers.add_parser('charts', help='Show the charts')
    parser_charts_platform = parser_charts.add_subparsers(dest='platform')
    parser_charts_platform.add_parser('all', help='The small charts from all platforms')
    for platform, data in CHARTS_URLS.items():
        actions = list(data.keys())
        parser_platform = parser_charts_platform.add_parser(platform, help=platform)
        parser_platform.add_argument('action', choices=actions, default='small', const='small', nargs='?', )

    parser_viral = subparsers.add_parser('viral', help='Viral posts')
    parser_viral_platform = parser_viral.add_subparsers(dest='platform')
    parser_viral_platform.add_parser('all', help='All viral posts')
    for platform, actions in VIRAL_TYPES.items():
        parser_platform = parser_viral_platform.add_parser(platform, help=platform)
        parser_platform.add_argument('action', choices=actions + ['all'], default='all', const='all', nargs='?',)

    parser_milestones = subparsers.add_parser('milestones', help='Milestones')
    parser_milestones.add_argument('type', choices=['all', 'new', 'past'], default='all', const='all', nargs='?',)
    parser_milestones.add_argument('platform', choices=PLATFORM + ['all'], default='all', const='all', nargs='?',)

    parser_search = subparsers.add_parser('search', help='Search')
    parser_search.add_argument('name')
    parser_search.add_argument('-f', '--full', action='store_true')

    return parser


def charts(args):
    if args.platform == 'all' or not hasattr(args, 'action'):
        print(api('charts'))
    elif args.action == 'all':
        print(api('charts', args.platform))
    else:
        print(api('charts', args.platform, args.action))


def viral(args):
    if args.platform == 'all' or not hasattr(args, 'action'):
        print(api('viral'))
    elif args.action == 'all':
        print(api('viral', args.platform))
    else:
        print(api('viral', args.platform, args.action))


def milestones(args):
    if args.type == 'all':
        print(api('milestones'))
    elif args.platform == 'all':
        print(api('milestones', args.type))
    else:
        print(api('milestones', args.type, args.platform))


def search(args):
    if args.full:
        for artist in api('search', args.name).json():
            print(api.artist[artist['id']])
    else:
        print(api('search', args.name))


def main(args=None):
    """entry point for the main cli"""
    func_map = {
        'charts': charts,
        'viral': viral,
        'milestones': milestones,
        'search': search,
    }
    parser = create_parser()
    args = parser.parse_args(args)
    func = func_map.get(args.command)
    if func:
        func(args)
    else:
        parser.print_help()
