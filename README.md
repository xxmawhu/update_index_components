- acquire_index_components.py执行之前需要设置setup.sh中的COMPONENTSPATH，改成项目仓库地址；crontab -e中的setup.sh路径地址也需要改变。
- check.txt用来检查结果，如果每天10点之后最后一条记录包含当天，则代表第一步执行成功
- k_line_data_check直接运行，用于检查股票数据缺失