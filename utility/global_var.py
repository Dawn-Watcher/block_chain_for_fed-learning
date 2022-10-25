# -*- coding: utf-8 -*-

def _init():  # 初始化
    global _global_dict
    global _model_map
    _global_dict = {}
    _model_map={}#key:哈希值,value：python端口

def set_value(key, value):
    _global_dict[key] = value

def get_value(key):
    return _global_dict[key]

def add_model(key, value):
    _model_map[key] = value

def get_model(key):
    return _model_map[key]

def delete_model(key):
    return _model_map.pop(key)