---
title: العمل مع الخادم الجانبي لـ GridJs
type: docs
weight: 250
url: /ar/python-net/aspose-cells-gridjs/server/
keywords: حالة الاستخدام, إكسل, GridJs, جدول البيانات, ملف, تنزيل, تحرير, محرر, عرض, عارض
description: يصف هذا المقال كيفية استخدام مكتبة Aspose.Cells.GridJs.
---


# العمل مع الخادم الجانبي لـ GridJs
## 1. قم بتعيين مسار المجلد الصحيح في التكوين
استخدام Config.set_file_cache_directory لتعيين مسار الذاكرة المؤقتة.
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

بالنسبة لتفاصيل التخزين ، يرجى التحقق من هذا ال[دليل](/python-net/aspose-cells-gridjs/storage/)


## 2. احصل على json من ملف جدول البيانات.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. احصل على الصور/الأشكال من ملف جدول البيانات
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. تحديث ملف جدول البيانات في الذاكرة المؤقتة
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5.  حفظ ملف جدول البيانات في الذاكرة المؤقتة
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

للحصول على معلومات مفصلة ، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net>
