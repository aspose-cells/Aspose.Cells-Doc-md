---
title: 使用 GridJs 服务器端
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/server/
description: 本文介绍如何使用 Aspose.Cells.GridJs 库。
---
# 使用 GridJs 服务器端
## 0.在Config中设置正确的文件夹路径
 **`Config.FileCacheDirectory`**对于工作簿缓存文件。
 **`Config.PictureCacheDirectory`**对于工作簿中的图像文件缓存。

有关存储详细信息，请检查此[指导](/net/aspose-cells-gridjs/storage/)

## 1.实现GridCacheForStream
对于本地文件存储，这里有一个例子：

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

对于服务器端存储，我们也提供了一个例子。
请检查：<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

##  2. 从电子表格文件中获取json。
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
##  3. 从电子表格文件中获取图像/形状
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4.更新缓存中的电子表格文件
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5.将电子表格文件保存在缓存中
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

有关详细信息，您可以在此处查看示例：
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>