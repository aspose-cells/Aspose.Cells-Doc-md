---
title: Travailler avec GridJs côté serveur
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/server/
keywords: cas d utilisation, excel, GridJs, tableur, fichier, téléchargement, modification, éditeur, visualisation, visualiseur
description: Cet article décrit comment utiliser la bibliothèque Aspose.Cells.GridJs.
---


# Travailler avec GridJs côté serveur
## 1. définir le bon chemin du dossier dans Config
utilisez Config.set_file_cache_directory pour définir le chemin du cache.
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

pour les détails de stockage, veuillez consulter ce [guide](/python-net/aspose-cells-gridjs/storage/)


## 2. Obtenir le json à partir du fichier de tableur.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. Obtenir les images/formes à partir du fichier de tableur.
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. Mettre à jour le fichier de tableur en cache
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5. Sauvegarder le fichier de tableur en cache
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

Pour plus d'informations, vous pouvez consulter l'exemple ici :
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
