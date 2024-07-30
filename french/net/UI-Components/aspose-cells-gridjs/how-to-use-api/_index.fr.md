---
title: Travailler avec GridJs côté serveur
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/how-to-use-api/
description: Cet article décrit comment utiliser les API dans GridJs.
keywords: GridJs,serveur,GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# Travailler avec GridJs côté serveur
## 0. définir le bon chemin du dossier dans Config
 **`Config.FileCacheDirectory`** pour le fichier de cache du classeur.
 **`Config.PictureCacheDirectory`** pour les fichiers image en cache dans le classeur.

pour les détails de stockage, veuillez consulter ce [guide](net/aspose-cells-gridjs/storage/)

## 1. Implémenter GridCacheForStream
Pour le stockage de fichiers local, voici un exemple :

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

Pour le stockage côté serveur, nous fournissons également un exemple.
Please check: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

## 2. Obtenir le json à partir du fichier de tableur.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. Obtenir les images/formes à partir du fichier de tableur.
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. Mettre à jour le fichier de tableur en cache
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5. Sauvegarder le fichier de tableur en cache
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

Pour plus d'informations, vous pouvez consulter l'exemple ici :
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
