---
title: Arbeta med GridJs på serversidan
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/server/
keywords: användningsfall, excel, GridJs, kalkylblad, fil, nedladdning, redigering, redigerare, vy, visare
description: Denna artikel beskriver hur man använder Aspose.Cells.GridJs biblioteket.
---


# Arbeta med GridJs på serversidan
## 1. ange rätt mappväg i konfigurationen
använd Config.set_file_cache_directory för att ange cacheläge.
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

för lagringsdetaljer, se denna [guide](/python-net/aspose-cells-gridjs/storage/)


## 2. Hämta json från kalkylbladet.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. Hämta bilder/former från kalkylbladet
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. Uppdatera kalkylbladet i cache
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5. Spara kalkylbladet i cache
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

För detaljerad info kan du kolla exemplet här:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net>
