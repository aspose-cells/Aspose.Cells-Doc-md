---
title: GridJsサーバーサイドで作業する
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-use-api/
description: この記事では、GridJsでAPIを使用する方法について説明しています。
keywords: GridJs,server,GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# GridJsサーバーサイドで作業する
## 0. Configで正しいフォルダパスを設定する
 ワークブックキャッシュファイルのための**`Config.FileCacheDirectory`**。
 ワークブック内の画像ファイルのキャッシュには**`Config.PictureCacheDirectory`**を使用します。

ストレージの詳細については、[ガイド](/net/aspose-cells-gridjs/storage/)をご確認ください。

## 1. GridCacheForStreamを実装する
ローカルファイルストレージの例は次のとおりです:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

サーバーサイドストレージでは、例も提供しています。
Please check: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

## 2. スプレッドシートファイルからJSONを取得します。
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. スプレッドシートファイルから画像/図形を取得します
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. キャッシュ内のスプレッドシートファイルを更新します
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5. キャッシュ内のスプレッドシートファイルを保存します
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

詳細については、こちらの例をご覧ください：
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
