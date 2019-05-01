# KDD-Cup-2019-CAMMTR

## Competition Website
[Context-Aware Multi-Modal Transportation Recommendation](https://dianshi.baidu.com/competition/29/rule)

## File Structure
```
.
├── Code # 代码
│   │
│   ├── ExploratoryDataAnalysis.ipynb # EDA
│   ├── FeatureEngineering # 数据处理和特征工程
│   │   ├── train_queries_processing.ipynb
│   │   ├── train_plans_processing.ipynb
│   │   └── ...
│   │
│   ├── Models # 模型
│   │   ├── lightgbm.ipynb
│   │   ├── xgboost.ipynb
│   │   └── ...
│   │
│   └── Pipline # 最终的pipline
│       ├── pipline.py
│       └── ...
│
├── Data # 数据文件
│   │
│   ├── data_set_phase1
│   │   ├── profiles.csv
│   │   ├── test_plans.csv
│   │   ├── test_queries.csv
│   │   ├── train_clicks.csv
│   │   ├── train_plans.csv
│   │   └── train_queries.csv
│   │
│   ├── BeijingSubway.json # 北京地铁坐标数据
│   ├── ShanghaiSubway.json # 上海地铁坐标数据
│   └── ...
│
├── .git
│
├── .gitignore
│
└── README.md
```

## Reference
* [ContextAware MultiModal Transportation Recommendation_Part1_赛题解析](https://mp.weixin.qq.com/s/3Qgz-swaSVsqHU86B5mfOA)
* [ContextAware MultiModal Transportation Recommendation_Part2_EDA](https://mp.weixin.qq.com/s/rlp2c3k8Y7NC73SPoONAMQ)
* [CAMMTR(KDD19)_Part3_多分类Baseline分享(含Code)](https://mp.weixin.qq.com/s/CHLxzXo2dV6RY-JVam510w)