---
title: Trabajando con GridJs del lado del servidor
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/server/
description: Este artículo describe cómo usar APIs en GridJs.
keywords: GridJs, servidor, GridCacheForStream
---


# Trabajando con GridJs del lado del servidor
## 0. configurar la ruta de carpeta correcta en Config
 **`Config.FileCacheDirectory`** para el archivo de caché del libro de trabajo.
 **`Config.PictureCacheDirectory`** para los archivos de imagen en caché en el libro de trabajo.

para los detalles de almacenamiento, por favor revisa esta [guía](/net/aspose-cells-gridjs/storage/)

## 1. Implementar GridCacheForStream
Para el almacenamiento de archivos local, aquí hay un ejemplo:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

Para el almacenamiento en el lado del servidor, también proporcionamos un ejemplo.
Please check: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

## 2. Obtener json del archivo de hoja de cálculo.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. Obtener las imágenes/formas del archivo de hoja de cálculo
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. Actualizar archivo de hoja de cálculo en caché
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5.  Guardar archivo de hoja de cálculo en caché
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

Para obtener información detallada, puede consultar el ejemplo aquí:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
