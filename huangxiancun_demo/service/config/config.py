# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2020/11/23 3:13 PM

# File_name: 'config.py'

"""
Describe: this is a demo!
"""

import os
import os.path as osp
import numpy as np
from easydict import EasyDict as edict
import yaml

__C = edict()
cfg = __C

# Root directory of project
__C.ROOT_DIR = osp.abspath(osp.join(osp.dirname(__file__), ".."))

# Data directory
__C.DATA_DIR = osp.abspath(osp.join(__C.ROOT_DIR, "data"))

# Model directory
__C.MODELS_DIR = osp.abspath(osp.join(__C.ROOT_DIR, "models"))

# dictionary
__C.DICTIONARY_PATH = osp.abspath(osp.join(__C.ROOT_DIR, "dictionary"))

# logging config
__C.LOGFILE = osp.abspath(osp.join(__C.ROOT_DIR, "config/logging.conf"))


# database config
__C.DBCONFIG = edict()
__C.DBCONFIG.MINCACHED = 5
__C.DBCONFIG.MAXCACHED = 10
__C.DBCONFIG.MAXCONNECTIONS = 50
__C.DBCONFIG.BLOCKING = True
__C.DBCONFIG.MAXSHARED = 51

# __C.DBCONFIG.HOST = "111.231.114.205"
# __C.DBCONFIG.PORT = 9208
# __C.DBCONFIG.USER = "root"
# __C.DBCONFIG.PASSWD = "MySql@hangzhou+2017"
# __C.DBCONFIG.DBNAME = "robot_outbound"
# __C.DBCONFIG.CHARSET = "utf8"
#本地
__C.DBCONFIG.HOST = "localhost"
__C.DBCONFIG.PORT = 3306
__C.DBCONFIG.USER = "root"
__C.DBCONFIG.PASSWD = "1234567890"
__C.DBCONFIG.DBNAME = "robot"
__C.DBCONFIG.CHARSET = "utf8"


# ip server and bind config
__C.RPC = edict()
__C.RPC.SERVER = edict()
__C.RPC.SERVER.HOST = "0.0.0.0"
__C.RPC.SERVER.PORT = 5004
__C.RPC.BIND = edict()
__C.RPC.BIND.HOST = "0.0.0.0"
__C.RPC.BIND.PORT = 5004
__C.RPC.SLEEP_SECONDS = 86400


# zookeeper config
__C.ZOOKEEPER = edict()
__C.ZOOKEEPER.CLIENT = edict()
__C.ZOOKEEPER.CLIENT.HOSTS = "123.207.221.203:8001"
__C.ZOOKEEPER.CLIENT.TIMEOUT = 5.0
__C.ZOOKEEPER.SERVICE = edict()
__C.ZOOKEEPER.SERVICE.NAME = "robot_outbound_dev"
__C.ZOOKEEPER.SERVICE.NODE_PATH = "/robot/robot_server/robot_outbound_dev"
__C.ZOOKEEPER.SERVICE.ADDRESS = "123.207.221.203"
__C.ZOOKEEPER.SERVICE.PORT = 9004
__C.ZOOKEEPER.SERVICE.SSLPORT = ""
__C.ZOOKEEPER.SERVICE.PAYLOAD = ""
__C.ZOOKEEPER.SERVICE.SERVICETYPE = "DYNAMIC"
__C.ZOOKEEPER.SERVICE.EPHEMERAL = True
__C.ZOOKEEPER.SERVICE.SEQUENCE = False
__C.ZOOKEEPER.SERVICE.MAKEPATH = True


# thirdparty_configs
# iflytek 科大讯飞 密钥信息
__C.IFLYTEK = edict()
__C.IFLYTEK.APPID = "5f5eceb1"
__C.IFLYTEK.APIKEY = "b3a1883fcaed7469e703f586a5e257e1"
__C.IFLYTEK.APISECRET = "09167e34f01c356bf7ae0e3031d333f0"


# 麦克风监控参数
__C.MICROPHONE = edict()
__C.MICROPHONE.AUDIOSAMPLINGRATE= 2000  #音频采样率
__C.MICROPHONE.CHUNK = 1024
__C.MICROPHONE.RATE = 16000



def _merge_a_into_b(a, b):
    """Merge config dictionary a into config dictionary b, clobbering the
    options in b whenever they are also specified in a.
    """
    if type(a) is not edict:
        return

    for k, v in a.items():
        # a must specify keys that are in b
        k = k.upper()
        if k not in b:
            raise KeyError("{} is not a valid config key".format(k))

        # the types must match, too
        old_type = type(b[k])
        if old_type is not type(v):
            if isinstance(b[k], np.ndarray):
                v = np.array(v, dtype=b[k].dtype)
            else:
                raise ValueError(("Type mismatch ({} vs. {}) "
                                "for config key: {}").format(type(b[k]),
                                                            type(v), k))

        # recursively merge dicts
        if type(v) is edict:
            try:
                _merge_a_into_b(a[k.lower()], b[k])
            except:
                print(("Error under config key: {}".format(k)))
                raise
        else:
            b[k] = v

def init_cfg(filename="parameter.yml"):
    """Load master config file and environment variable from sub file."""
    filename = find_cfg_file(filename)
    with open(filename, "r", encoding="utf-8") as f:
        master_yaml_cfg = edict(yaml.safe_load(f))
    active_suffix = master_yaml_cfg["robot"]["profiles"]["active"]
    sub_cfg_file = find_cfg_file("".join(["parameter_", active_suffix ,".yml"]))
    cfg_from_file(sub_cfg_file)
    return cfg

def find_cfg_file(filename):
    if not os.path.exists(filename):
        filename = osp.abspath(osp.join(__C.ROOT_DIR, "config", filename))
        if not os.path.exists(filename):
            raise ValueError(("Error config file '{}' ").format(filename))
    return filename

def cfg_from_file(filename):
    """Load a config file and merge it into the default options."""
    with open(filename, "r", encoding="utf-8") as f:
        yaml_cfg = edict(yaml.safe_load(f))
    _merge_a_into_b(yaml_cfg, __C)

def cfg_from_list(cfg_list):
    """Set config keys via list (e.g., from command line)."""
    from ast import literal_eval
    assert len(cfg_list) % 2 == 0
    for k, v in zip(cfg_list[0::2], cfg_list[1::2]):
        key_list = k.split(".")
        d = __C
        for subkey in key_list[:-1]:
            assert subkey in d
            d = d[subkey]
        subkey = key_list[-1]
        assert subkey in d
        try:
            value = literal_eval(v)
        except:
            # handle the case when v is a string literal
            value = v
        assert type(value) == type(d[subkey]), \
            "type {} does not match original type {}".format(
            type(value), type(d[subkey]))
        d[subkey] = value

if __name__ == "__main__":
    init_cfg()
    print(cfg)
