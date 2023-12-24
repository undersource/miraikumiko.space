from configparser import ConfigParser
from backend.misc.arguments import args

config = ConfigParser()
config.read(args.config)
