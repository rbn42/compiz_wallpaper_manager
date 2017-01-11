import json
import os.path


def save(filename, info):
    s = json.dumps(info)
    path = filename + '.json'
    with open(path, 'w') as f:
        f.write(s)


def load(filename):
    path = filename + '.json'
    path = os.path.expanduser(path)
    if os.path.exists(path):
        with open(path) as f:
            s = f.read()
        return json.loads(s)
    else:
        return {'filenamename': filename}
