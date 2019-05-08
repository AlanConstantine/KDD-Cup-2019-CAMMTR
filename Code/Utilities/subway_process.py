# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-05-01 15:05:09

import os
import json
import pandas as pd
import numpy as np
from pprint import pprint as ppt


def process(path):
    with open(path, 'r', encoding='utf-8') as rf:
        subway = json.load(rf)
    path_, filename = os.path.split(path)
    output_path = filename.replace('.json', '.csv')
    subway_pd = parse_json(subway)
    subway_pd.to_csv(r'../../Data/'+output_path, index=False)
    print(output_path, 'done.')


def parse_json(j):
    subway_pd = pd.DataFrame(
        columns=['station_name', 'station_longitude', 'station_latitude'])
    index = 0
    for line in j['l']:
        for station in line['st']:
            lg, la = station['sl'].split(',')
            insert_list = [
                str(station['n']).strip(),
                float(lg),
                float(la)
            ]
            subway_pd.loc[index] = insert_list
            index += 1
    return subway_pd


if __name__ == "__main__":
    pathpool = [r'../../Config/Beijing.json',
                r'../../Config/Shanghai.json']
    for p in pathpool:
        process(p)
