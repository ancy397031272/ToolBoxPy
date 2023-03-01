# -*- coding:utf-8 -*-
import os
import sys
import json
import yaml
import pickle

__all__ = [
    "load_json",
    "dump_json",
    "load_pickle",
    "dump_pickle",
    "load_txt",
    "dump_txt",
    "load_yaml",
    "load_all_yaml",
    "dump_yaml"
]


def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def dump_json(js, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(js, f, indent=4)


def load_pickle(file_name, method='rb'):
    """
    Read a pickled object representation from the open file.
    Return the reconstituted object hierarchy specified in the file.
    """
    if method == "r":
        method = "rb"
        sys.stderr.write("loadPk: using 'rb' instead of 'r'\n")
    with open(file_name, method) as f:
        return pickle.load(f)


def dump_pickle(data, file_name, method='wb'):
    """
    Write a pickled representation of obj to the open file.
    """

    with open(file_name, method) as f:
        pickle.dump(obj=data, file=f)


def dump_txt(file_name, data, mode='w'):
    with open(file_name, mode) as f:
        f.write(data)


def load_txt(file_name, mode='r'):
    with open(file_name, mode) as f:  # 设置文件对象
        data = f.read()
    return data


def load_yaml(file_name, method='r', encoding='utf-8'):
    """
    Parse the first YAML document in a stream
    and produce the corresponding Python object.
    """
    if 'b' in method:
        with open(file_name, method) as f:
            return yaml.load(stream=f, Loader=yaml.FullLoader)
    else:
        with open(file_name, method, encoding=encoding) as f:
            return yaml.load(stream=f, Loader=yaml.FullLoader)


def load_all_yaml(file_name, method='r', encoding='utf-8'):
    """
    Parse all YAML documents in a stream
    and produce corresponding Python objects.
    """
    if 'b' in method:
        with open(file_name, method) as f:
            return [data for data in yaml.load_all(stream=f, Loader=yaml.FullLoader)]
    else:
        with open(file_name, method, encoding=encoding) as f:
            return [data for data in yaml.load_all(stream=f, Loader=yaml.FullLoader)]


def dump_yaml(data, file_name, method='w', encoding='utf-8', safe_mode=False):
    """
    Serialize a Python object into a YAML stream.
    If stream is None, return the produced string instead.
    """
    if safe_mode:
        temp_file_name = file_name + '_temp'
    else:
        temp_file_name = file_name

    with open(temp_file_name, method) as f:
        if 'b' in method:
            ret = yaml.dump(data=data, stream=f, encoding=encoding)
        else:
            ret = yaml.dump(data=data, stream=f)
        if safe_mode:
            f.flush()
            os.fsync(f.fileno())

    if safe_mode:
        os.rename(temp_file_name, file_name)

    return ret
