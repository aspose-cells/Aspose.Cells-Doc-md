---
title: العمل مع جانب خادم GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/server/
description: توضح هذه المقالة كيفية استخدام مكتبة Aspose.Cells.GridJs.
---
# العمل مع جانب خادم GridJs

## 1. تنفيذ GridCacheForStream
بالنسبة لتخزين الملفات المحلية ، إليك مثال:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

بالنسبة للتخزين من جانب الخادم ، نقدم أيضًا مثالاً.
 يرجى المراجعة:<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>
## 2. احصل على json من ملف جدول البيانات.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. احصل على الصور / الأشكال من ملف جدول البيانات
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. تحديث ملف جدول البيانات في ذاكرة التخزين المؤقت
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5. حفظ ملف جدول البيانات في ذاكرة التخزين المؤقت
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

للحصول على معلومات تفصيلية ، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>