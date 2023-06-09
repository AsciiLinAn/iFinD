import pandas as pd

# 读取股票数据库并进行预处理
data = pd.read_excel('D:/0.Need to be the top/Y/task/517_1.0/stock.xlsx')

# 指定要操作的列名和分组列名
value_columns = ['open', 'close', 'high', 'low']
group_column = 'thscode'

# 获取分组列的唯一值
group_values = data[group_column].unique()

# 创建一个空的 DataFrame 用于存储结果
result = pd.DataFrame()

# 对每个列、每个分组和每个间隔进行操作，并将结果添加到结果 DataFrame
for col in value_columns:
    for group in group_values:
        group_data = data[data[group_column] == group]
        for interval in range(1,21):
            values = []
            for i in range(0, len(group_data), interval):
                value = group_data[col].iloc[i]  # 获取指定间隔的单元格值
                values.append(value)
            flattened_values = values + [float('nan')] * (len(group_data) - len(values))
            # 将结果填充到结果 DataFrame，并确保填充缺失值为 NaN
            result[f'{col}_group{group}_interval{interval}'] = flattened_values

# 将结果保存为新的 Excel 文件
result.to_excel('D:/0.Need to be the top/Y/task/517_1.0/result_file.xlsx', index=False)

# 整理数据库的格式以便操作
df = pd.read_excel(r'D:/0.Need to be the top/Y/task/517_1.0/path_to_transposed_excel_file.xlsx')
database = []
for index, row in df.iterrows():
    data_list = list(row)
    database.append(data_list)

# 导入需要查找的股票的数据
df = pd.read_excel(r'D:/0.Need to be the top/Y/task/517_1.0/extract.xlsx')
tolerance = 0.01#浮点数比对，一定的容错率
extract = []
for column in df:
    data_list = list(df[column])
    extract.append(data_list)

# 对比并输出匹配的记录对应的股票名
for i, alist in enumerate(extract):
    match = False
    for record in database:
        if all(abs(extract_value - db_value) <= tolerance for extract_value, db_value in zip(alist, record[1:])):
            print(f"Matched: {record[0]}")
            match = True
            break
    if not match:
        print("No match found")