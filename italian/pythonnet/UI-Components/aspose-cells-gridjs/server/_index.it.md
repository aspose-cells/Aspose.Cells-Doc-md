---
title: Lavorare con GridJs lato server
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/server/
keywords: caso d uso, excel, GridJs, foglio elettronico, file, download, modifica, editor, visualizzazione, visualizzatore
description: Questo articolo descrive come utilizzare la libreria Aspose.Cells.GridJs.
---


# Lavorare con GridJs lato server
## 1. imposta il percorso della cartella corretta in Config
usa Config.set_file_cache_directory per impostare il percorso della cache.
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

per i dettagli di archiviazione, controlla questa [guida](/python-net/aspose-cells-gridjs/storage/)


## 2. Ottieni json dal file del foglio di calcolo.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. Ottieni le immagini/forme dal file del foglio di calcolo
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. Aggiorna il file del foglio di calcolo in cache
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5. Salva il file del foglio di calcolo in cache
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

Per ulteriori informazioni, puoi controllare l'esempio qui:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
