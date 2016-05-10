import os.path
try:
    # python2
    import ConfigParser
    config = ConfigParser.RawConfigParser()
except:
    # python3
    import configparser
    config = configparser.ConfigParser()
path = '~/.config/compiz-1/compizconfig/Default.ini'
path = os.path.expanduser(path)
config.read(path)


def getSize():
    h, v = 4, 1
    try:
        h = config.getint('core', 's0_hsize')
    except:
        pass
    try:
        v = config.getint('core', 's0_vsize')
    except:
        pass
    return h, v
