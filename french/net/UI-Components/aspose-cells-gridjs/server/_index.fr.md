---
title: Travailler avec GridJs côté serveur
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/server/
description: Cet article décrit comment utiliser la bibliothèque Aspose.Cells.GridJs.
---
#  Travailler avec GridJs côté serveur
##  0. définir le bon chemin de dossier dans Config
 **`Config.FileCacheDirectory`** pour le fichier cache du classeur.
 **`Config.PictureCacheDirectory`** pour le cache des fichiers image dans le classeur.

 pour les détails de stockage, veuillez vérifier ceci[guide](/net/aspose-cells-gridjs/storage/)

##  1. Implémenter GridCacheForStream
Pour le stockage de fichiers local, voici un exemple :

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

Pour le stockage côté serveur, nous fournissons également un exemple.
 Vérifiez s'il vous plaît:<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

##  2. Obtenez json à partir du fichier de feuille de calcul.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
##  3. Obtenez les images/formes à partir du fichier de feuille de calcul
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
##  4. Mettre à jour le fichier de feuille de calcul dans le cache
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
##  5. Enregistrer le fichier de feuille de calcul dans le cache
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

Pour plus d'informations, vous pouvez consulter l'exemple ici :
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>