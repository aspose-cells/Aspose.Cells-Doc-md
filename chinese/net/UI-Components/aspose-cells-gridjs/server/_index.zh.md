---
title: 与GridJs服务器端一起工作
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/server/
description: 本文介绍了如何在GridJs中使用API。
keywords: GridJs，服务器，GridCacheForStream
---


# 与GridJs服务器端一起工作
## 0. 设置Config中的正确文件夹路径
 **`Config.FileCacheDirectory`** 用于工作簿缓存文件。
 **`Config.PictureCacheDirectory`** 用于工作簿中图像文件的缓存。

有关存储详细信息，请查看此[guide](/net/aspose-cells-gridjs/storage/)

## 1. 实现GridCacheForStream
对于本地文件存储，这是一个示例：

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

对于服务器端存储，我们也提供了一个示例。
Please check: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

## 2. 从电子表格文件获取json。
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. 从电子表格文件中获取图像/形状
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. 更新缓存中的电子表格文件
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5. 将电子表格文件保存到缓存中
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

详情请查看这里的示例:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
