---
title: 与GridJs服务器端配合工作
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/server/
keywords: 用例，Excel，GridJs，电子表格，文件，下载，编辑，编辑器，视图，查看器
description: 本文描述了如何使用Aspose.Cells.GridJs库。
---


# 与GridJs服务器端配合工作
## 1. 在Config中设置正确的文件夹路径
使用Config.set_file_cache_directory来设置缓存路径。
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

有关存储详情，请查看此[指南](/python-net/aspose-cells-gridjs/storage/)


## 2. 从电子表格文件中获取JSON。
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. 从电子表格文件中获取图像/形状
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. 在缓存中更新电子表格文件
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5. 将电子表格文件保存在缓存中
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

有关详细信息，请查看此处的示例：
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net>
