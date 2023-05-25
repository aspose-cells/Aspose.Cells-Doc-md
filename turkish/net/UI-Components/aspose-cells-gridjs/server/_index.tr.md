---
title: GridJs Sunucu Tarafı ile Çalışma
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/server/
description: Bu makalede, Aspose.Cells.GridJs kitaplığının nasıl kullanılacağı açıklanmaktadır.
---
#  GridJs Sunucu Tarafı ile Çalışma
##  0. Config'de doğru klasör yolunu ayarlayın
 **"Config.FileCacheDirectory"** çalışma kitabı önbellek dosyası için.
 **"Config.PictureCacheDirectory"** çalışma kitabındaki görüntü dosyaları önbelleği için.

 depolama detayı için lütfen bunu kontrol edin[rehber](/net/aspose-cells-gridjs/storage/)

##  1. GridCacheForStream'i uygulayın
Yerel dosya depolaması için işte bir örnek:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

Sunucu tarafında depolama için ayrıca bir örnek sunuyoruz.
 Lütfen kontrol edin:<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

##  2. Elektronik tablo dosyasından json'u alın.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
##  3. Elektronik tablo dosyasından resimleri/şekilleri alın
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
##  4. Elektronik tablo dosyasını önbellekte güncelleyin
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
##  5. Elektronik tablo dosyasını önbelleğe kaydedin
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

Ayrıntılı bilgi için, örneği buradan kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>