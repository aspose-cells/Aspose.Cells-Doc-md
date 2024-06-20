---
title: Arbeta med GridJs på serversidan
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/server/
description: Denna artikel beskriver hur man använder API er i GridJs.
keywords: GridJs, server, GridCacheForStream
---


# Arbeta med GridJs på serversidan
## 0. Ange rätt mappväg i Config
 **`Config.FileCacheDirectory`** för arbetsbokscache-filen.
 **`Config.PictureCacheDirectory`**  för bildfilscache i arbetsboken.

För lagringsinformation, se denna [guide](/net/aspose-cells-gridjs/storage/)

## 1. Implementera GridCacheForStream
För lokal fil lagring, här är ett exempel:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

För serversidans lagring, tillhandahåller vi också ett exempel.
Please check: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

## 2. Hämta json från kalkylbladet.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. Hämta bilder/former från kalkylbladet
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. Uppdatera kalkylbladet i cache
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5. Spara kalkylbladet i cache
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

För detaljerad info kan du kolla exemplet här:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
