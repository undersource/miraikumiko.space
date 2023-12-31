import argparse

args_parser = argparse.ArgumentParser(description='miraikumiko backend')
args_parser.add_argument(
    '-c',
    '--config',
    type=str,
    default='miraikumiko.conf',
    dest='config',
    help='config file path'
)
args_parser.add_argument(
    '-l',
    '--log',
    type=str,
    default='miraikumiko.log',
    dest='log',
    help='log file path'
)
args_parser.add_argument(
    '-n',
    '--name',
    type=str,
    default=None,
    dest='name',
    help='name of user'
)
args_parser.add_argument(
    '-p',
    '--phone',
    type=str,
    default=None,
    dest='phone',
    help='phone of user'
)
args_parser.add_argument(
    '-e',
    '--email',
    type=str,
    default=None,
    dest='email',
    help='email of user'
)
args_parser.add_argument(
    '-L',
    '--login',
    type=str,
    default=None,
    dest='login',
    help='login of user'
)
args_parser.add_argument(
    '-P',
    '--password',
    type=str,
    default=None,
    dest='password',
    help='password of user'
)

args = args_parser.parse_args()
