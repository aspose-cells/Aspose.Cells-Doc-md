---
title: Working with GridJs Server Side
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/server/
keywords: use case,excel,GridJs,spreadsheet,file,download,edit,editor,view,viewer
description: This article describes how to use Aspose.Cells.GridJs library.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Working with GridJs Server Side

## 1. Set the right folder path in Config
Use `Config.set_file_cache_directory` to set the cache path.

```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

For the storage details, please check this [guide](/python-net/aspose-cells-gridjs/storage/)

## 2. Get JSON from the spreadsheet file.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);
 
ret =gwb.export_to_json();
```

## 3. Get the images/shapes from the spreadsheet file
```python
# GridJs will automatically zip all the images/shapes into a zip stream and store it in cache  

# Get the file ID in the cache; UID is the unique ID for the spreadsheet instance, and sheet ID is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# Get the zip file by the file ID
os.path.join(Config.file_cache_directory, fileid)
```

## 4. Update spreadsheet file in cache
```python
gwb = new GridJsWorkbook();
# p is the update JSON, UID is the unique ID for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```

## 5. Save spreadsheet file in cache
```python
gwb = new GridJsWorkbook();
# p is the update JSON, UID is the unique ID for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

For detailed info, you can check the example here:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
