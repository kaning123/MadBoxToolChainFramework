import os
import json
from multiprocessing import Process, Queue
def get_current_dir():
    return os.path.dirname(os.path.realpath(__file__))

def get_parent_dir(dir_name):
    return os.path.abspath(os.path.join(dir_name, os.pardir))

def read_cfgs(layer_dir):
    with open(os.path.join(layer_dir, 'cfg.json'), 'r') as f:
        a = json.load(f)
    with open(os.path.join(layer_dir, 'recv.json'), 'r') as f:
        b = json.load(f)
    with open(os.path.join(layer_dir, 'send.json'), 'r') as f:
        c = json.load(f)
    return a, b, c
def read_layer_cfgs(layer_dir):
    a = read_cfgs(layer_dir)
    if a[0]["type"] != "layer":
        raise TypeError("Not a layer directory")
    return a
def read_block_cfgs(block_dir):
    a = read_cfgs(block_dir)
    if a[0]["type"] != "block":
        raise TypeError("Not a block directory")
    return a
def get_layer_files():
    a = get_current_dir()
    a = get_parent_dir(a)
    cfgs = read_layer_cfgs(a)
    return cfgs
def parse_layer_cfgs(cfgs):
    cfg = cfgs[0]
    recv = cfgs[1]
    send = cfgs[2]
    reg_blocks = cfg['reg_blocks']
    layer_struct = cfg["structures"]
    for block in reg_blocks:
    
