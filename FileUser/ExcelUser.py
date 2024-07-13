import pandas as pd

# 读取Excel文件
excel_file='22.xlsx'
df = pd.ExcelFile(excel_file)

# 遍历每个sheet并进行处理
for sheet_name in df.sheet_names:
    de = pd.read_excel(excel_file, sheet_name=sheet_name)
    if(sheet_name=='Sheet1'):
        print(f"Data from sheet '{sheet_name}':")
        print(de)
        # d导出数据为EXCEL
        de.to_excel('output.xlsx', index=False)



