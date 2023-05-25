---
title: Lavorare con GridJs lato server
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/server/
description: Questo articolo descrive come utilizzare la libreria Aspose.Cells.GridJs.
---
#  Lavorare con GridJs lato server
##  0. imposta il percorso della cartella corretto in Config
 **`Config.FileCacheDirectory`** per il file di cache della cartella di lavoro.
 **`Config.DirectoryPictureCache`** per la cache dei file immagine nella cartella di lavoro.

 per i dettagli di archiviazione, controlla questo[guida](/net/aspose-cells-gridjs/storage/)

##  1. Implementare GridCacheForStream
Per l'archiviazione di file locale, ecco un esempio:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

Per l'archiviazione lato server, forniamo anche un esempio.
 Si prega di controllare:<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

##  2. Ottieni json dal file del foglio di calcolo.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
##  3. Ottieni le immagini/forme dal file del foglio di calcolo
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
##  4. Aggiorna il file del foglio di calcolo nella cache
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
##  5. Salva il file del foglio di calcolo nella cache
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

Per informazioni dettagliate, puoi controllare l'esempio qui:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>