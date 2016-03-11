from pkg_resources import get_distribution

try:
    __version__ = get_distribution('socorrolib').version
except DistributionNotFound:
    __version__ = 'Please install this project with setup.py'
