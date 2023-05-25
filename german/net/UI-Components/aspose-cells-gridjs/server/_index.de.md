---
title: Arbeiten mit GridJs Serverseite
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/server/
description: In diesem Artikel wird beschrieben, wie Sie die Bibliothek Aspose.Cells.GridJs verwenden.
---
#  Arbeiten mit GridJs Serverseite
##  0. Stellen Sie in der Konfiguration den richtigen Ordnerpfad ein
 **`Config.FileCacheDirectory`** für die Arbeitsmappen-Cache-Datei.
 **`Config.PictureCacheDirectory`** für den Bilddatei-Cache in der Arbeitsmappe.

 Einzelheiten zur Lagerung finden Sie hier[Führung](/net/aspose-cells-gridjs/storage/)

##  1. Implementieren Sie GridCacheForStream
Hier ein Beispiel für die lokale Dateispeicherung:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

Für die serverseitige Speicherung stellen wir auch ein Beispiel bereit.
 Überprüfen Sie bitte:<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

##  2. Holen Sie sich JSON aus der Tabellenkalkulationsdatei.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
##  3. Holen Sie sich die Bilder/Formen aus der Tabellenkalkulationsdatei
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
##  4. Tabellendatei im Cache aktualisieren
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
##  5. Tabellendatei im Cache speichern
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

Für detaillierte Informationen können Sie sich das Beispiel hier ansehen:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>