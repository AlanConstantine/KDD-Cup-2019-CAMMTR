# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2019-05-06 21:25:26

import os
import json
import pandas as pd
import numpy as np
from pprint import pprint as ppt


def process(path):
    with open(path, 'r') as rf:
        subway = json.load(rf)
    path_, filename = os.path.split(path)
    output_path = filename.replace('.json', '.csv')
    weather_pd = parse_json(subway)
    weather_pd.to_csv(r'../../Data/'+output_path, index=False)
    print(output_path, 'done.')


def parse_json(j):
    weather_pd = pd.DataFrame(
        columns=['date', 'max_temp', 'min_temp', 'weather', 'wind'])
    index = 0

    for k, v in j.items():
        insert_list = [k, int(v['max_temp']), int(
            v['min_temp']), v['weather'], int(v['wind'])]
        weather_pd.loc[index] = insert_list
        index += 1

    # types = weather_pd['weather'].unique()
    # add_c = ['weather_'+t for t in types]
    # current_c = list(weather_pd.columns.values)
    # current_c.extend(add_c)
    # weather_pd = weather_pd.reindex(columns=current_c, fill_value=0)
    # for t in add_c:
    #     weather_pd.loc[(weather_pd['weather'] == t.split('_')[-1]), [t]] = 1

    # weather_pd.drop(columns=['weather'], axis=1, inplace=True)

    return weather_pd


if __name__ == "__main__":
    pathpool = [r'../../Config/Weather.json']
    for p in pathpool:
        process(p)
