---
title: Working with GridJs Server Side
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/server/
description: This article describes how to use Aspose.Cells.GridJs library.
---


# Working with GridJs Server Side
## 1. set the right folder path in Config
 **`Config.set_file_cache_directory for the workbook cache file.
 

for the storage detail ,please check this [guide](/python-net/aspose-cells-gridjs/storage/)


## 2. Get json from the spreadsheet file.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);
 
ret =gwb.export_to_json();
```
## 3. Get the images/shapes  from the spreadsheet file
```python
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  
 

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

//get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. Update spreadsheet file in cache
```python
gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5.  Save spreadsheet file in cache
```python
gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

For detail info ,you can check the example here:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net>