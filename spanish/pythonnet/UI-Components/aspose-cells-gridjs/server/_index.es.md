---
title: Trabajando con GridJs del lado del servidor
type: docs
weight: 250
url: /es/python-net/aspose-cells-gridjs/server/
keywords: caso de uso,excel,GridJs,hoja de cálculo,archivo,descargar,editar,editor,ver,visor
description: Este artículo describe cómo utilizar la biblioteca Aspose.Cells.GridJs.
---


# Trabajando con GridJs del lado del servidor
## 1. Configurar la ruta correcta de la carpeta en Configuración
utilice Config.set_file_cache_directory para establecer la ruta de la caché.
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

para obtener detalles de almacenamiento, consulte esta [guía](/python-net/aspose-cells-gridjs/storage/)


## 2. Obtener json del archivo de hoja de cálculo.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. Obtener las imágenes/formas del archivo de hoja de cálculo
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. Actualizar archivo de hoja de cálculo en caché
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5.  Guardar archivo de hoja de cálculo en caché
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

Para obtener información detallada, puede consultar el ejemplo aquí:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
