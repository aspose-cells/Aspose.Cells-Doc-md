---
title: Работа с GridJs на стороне сервера
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/server/
description: Эта статья описывает, как использовать API в GridJs .
keywords: GridJs, сервер, GridCacheForStream
---


# Работа с сервером GridJs
## 0. установите правильный путь к папке в Config
 **`Config.FileCacheDirectory`** для файла кэша рабочей книги.
 **`Config.PictureCacheDirectory`** для кэширования изображений в рабочей книге.

для более подробной информации о хранении, пожалуйста, ознакомьтесь с этим [руководством](/net/aspose-cells-gridjs/storage/)

## 1. Реализация GridCacheForStream
Для локального хранения файлов вот пример:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

Для хранения на стороне сервера мы также предоставляем пример.
Please check: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

## 2. Получить json из файла электронной таблицы.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. Получить изображения/формы из файла электронной таблицы
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. Обновить файл электронной таблицы в кэше
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5.  Сохранить файл электронной таблицы в кэше
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

Для получения дополнительной информации, вы можете проверить пример здесь:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
