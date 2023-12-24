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

args = args_parser.parse_args()
