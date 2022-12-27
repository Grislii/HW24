import os
import re


def do_cmd(cmd: str, value: str, data: list[str]) -> list:
    if cmd == 'filter':
        result = list(filter(lambda record: value in record, data))
    elif cmd == 'map':
        col_num = int(value)
        result = list(map(lambda record: record.split()[col_num], data))
    elif cmd == 'unique':
        result = list(set(data))
    elif cmd == 'sort':
        reverse = value == 'desc'
        result = sorted(data, reverse=reverse)
    elif cmd == 'limit':
        col_num = int(value)
        result = [line for line in list(data)[:col_num]]
    elif cmd == 'regex':
        prog = re.compile(value)
        result = prog.findall(str(data))
    return result


def do_query(params: dict, DATA_DIR: str) -> list:
    with open(os.path.join(DATA_DIR, params["file_name"])) as file:
        file_data = file.readlines()

    res = file_data

    num = 1
    cmd = 'cmd' + str(num)
    value = 'value' + str(num)

    while cmd in params.keys() and value in params.keys():
        if cmd in params.keys():
            res = do_cmd(params[cmd], params[value], res)
        cmd = 'cmd' + str(num)
        value = 'value' + str(num)
        num += 1

    return res