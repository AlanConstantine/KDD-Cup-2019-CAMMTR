# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-05-01 15:05:09

import os
import json
import math
import pandas as pd
import numpy as np
from pprint import pprint as ppt


def process(path):
    with open(path, 'r') as rf:
        subway = json.load(rf)
    path_, filename = os.path.split(path)
    output_path = filename.replace('.json', '.csv')
    subway_pd = parse_json(subway)
    subway_pd.to_csv(r'../../Data/'+output_path, index=False)
    print(output_path, 'done.')


def GCJ2WGS(location):
    # location格式如下：locations[1] = "113.923745,22.530824"
    lon = float(location[0:location.find(",")])
    lat = float(location[location.find(",") + 1:len(location)])
    a = 6378245.0  # 克拉索夫斯基椭球参数长半轴a
    ee = 0.00669342162296594323  # 克拉索夫斯基椭球参数第一偏心率平方
    PI = math.pi  # 圆周率
    # 以下为转换公式
    x = lon - 105.0
    y = lat - 35.0
    # 经度
    dLon = 300.0 + x + 2.0 * y + 0.1 * x * x + \
        0.1 * x * y + 0.1 * math.sqrt(abs(x))
    dLon += (20.0 * math.sin(6.0 * x * PI) + 20.0 *
             math.sin(2.0 * x * PI)) * 2.0 / 3.0
    dLon += (20.0 * math.sin(x * PI) + 40.0 *
             math.sin(x / 3.0 * PI)) * 2.0 / 3.0
    dLon += (150.0 * math.sin(x / 12.0 * PI) + 300.0 *
             math.sin(x / 30.0 * PI)) * 2.0 / 3.0
    # 纬度
    dLat = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * \
        y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
    dLat += (20.0 * math.sin(6.0 * x * PI) + 20.0 *
             math.sin(2.0 * x * PI)) * 2.0 / 3.0
    dLat += (20.0 * math.sin(y * PI) + 40.0 *
             math.sin(y / 3.0 * PI)) * 2.0 / 3.0
    dLat += (160.0 * math.sin(y / 12.0 * PI) + 320 *
             math.sin(y * PI / 30.0)) * 2.0 / 3.0
    radLat = lat / 180.0 * PI
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * PI)
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * PI)
    wgsLon = lon - dLon
    wgsLat = lat - dLat
    return wgsLon, wgsLat


def parse_json(j):
    subway_pd = pd.DataFrame(
        columns=['station_name', 'station_longitude', 'station_latitude'])
    index = 0
    for line in j['l']:
        for station in line['st']:
            lg, la = GCJ2WGS(station['sl'])
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
