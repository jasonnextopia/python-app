from os import getenv, path
from json import dumps, load

class Config():
    DBHOST = getenv("DBHOST", 'localhost')
    DBUSER = getenv("DBUSER", 'root')
    DBPASSWORD = getenv("DBPASSWORD", 'admin1234')
    DBNAME = getenv("DBNAME", "readitlater")

def load_conf():
    conf_obj = {}
    if (path.isfile('./config.json')):
        with open('./config.json', 'r') as f:
            conf_obj.update(load(f))

    return Config(**conf_obj)