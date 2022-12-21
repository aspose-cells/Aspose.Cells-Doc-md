---
title: GridJs サーバー側での作業
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/server/
description: この記事では、Aspose.Cells.GridJs ライブラリの使用方法について説明します。
---
# GridJs サーバー側での作業

## 1. GridCacheForStream を実装する
ローカル ファイル ストレージの例を次に示します。

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

サーバー側のストレージについては、例も示します。
チェックしてください：<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>
## 2. スプレッドシート ファイルから json を取得します。
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. スプレッドシート ファイルから画像/形状を取得する
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. キャッシュ内のスプレッドシート ファイルを更新する
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5. スプレッドシート ファイルをキャッシュに保存する
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

詳細情報については、ここで例を確認できます。
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>