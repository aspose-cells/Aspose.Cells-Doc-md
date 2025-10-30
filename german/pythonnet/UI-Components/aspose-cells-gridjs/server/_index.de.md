---
title: Arbeiten mit GridJs Server Side
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/server/
keywords: Anwendungsfall, Excel, GridJs, Tabellenkalkulation, Datei, herunterladen, bearbeiten, Editor, anzeigen, Viewer
description: In diesem Artikel wird beschrieben, wie die Aspose.Cells.GridJs Bibliothek verwendet wird.
---


# Arbeiten mit GridJs Server Side
## 1. Setzen Sie den richtigen Ordnerpfad in der Konfiguration
Verwenden Sie Config.set_file_cache_directory, um den Cache-Pfad festzulegen.
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

Für die Speicherdetails überprüfen Sie bitte diese [Anleitung](/python-net/aspose-cells-gridjs/storage/)


## 2. Holen Sie sich JSON aus der Tabellenkalkulationsdatei.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. Holen Sie sich die Bilder/Formen aus der Tabellenkalkulationsdatei
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. Aktualisieren Sie die Tabellenkalkulationsdatei im Cache
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5.  Tabellendatei im Cache speichern
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

Für weitere Details können Sie hier das Beispiel überprüfen:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
