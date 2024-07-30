---
title: GridJs Sunucu Tarafı ile Çalışmak
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/how-to-use-api/
description: Bu makale, GridJs deki API leri nasıl kullanacağınızı açıklar.
keywords: GridJs, sunucu, GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# GridJs Sunucu Tarafı ile Çalışmak
## 0. Config'de doğru klasör yolunu ayarlayın
 **`Config.FileCacheDirectory`** için çalışbook önbellek dosyası.
 **`Config.PictureCacheDirectory`** çalışbook'taki resim dosyaları önbelleği için.

depolama detayı için lütfen bu [kılavuza](/net/aspose-cells-gridjs/storage/) bakın

## 1. GridCacheForStream’i uygulayın
Yerel dosya depolama için burada bir örnek:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

Sunucu tarafı depolaması için de bir örnek sağlıyoruz.
Please check: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

## 2. Çalışma tablosundan json alın.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. Çalışma tablosundan resimleri/şekilleri alın
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. Önbellekte çalışma tablosunu güncelle
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5.  Önbellekte çalışma tablosunu kaydedin
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

Detaylı bilgiler için buradaki örneği kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
