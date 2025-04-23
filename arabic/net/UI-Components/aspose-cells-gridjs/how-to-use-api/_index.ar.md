---
title: العمل مع الخادم الجانبي لـ GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/how-to-use-api/
description: يصف هذا المقال كيفية استخدام واجهات برمجة التطبيقات في جريدجس.
keywords: جريدجس، الخادم، GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# العمل مع الخادم الجانبي لـ GridJs
## 1. أضف خدمة في ConfigureServices في startup.cs 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. تعيين مسار تخزين ملفات التخزين المؤقتة

يمكنك اختيار أي من الطرق التالية:

 الخيار 1: تعيين GridJsOptions في ConfigureServices في Startup.cs
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 الخيار 2: تعيين الخاصية الثابتة مباشرة
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 الخيار 3: تحديد قاعدة تخزين ذاكرة التخزين المؤقت الخاصة بك من خلال تنفيذ GridCacheForStream

بالنسبة لتخزين الملفات المحلي ، إليك مثال:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


بالنسبة للتخزين في جانب الخادم، نوفر أيضًا مثالًا. يرجى التحقق من: 

<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


لمزيد من التفاصيل حول التخزين، يرجى الرجوع إلى [الدليل](/cells/ar/net/aspose-cells-gridjs/storage/)


## 3. تنفيذ إجراءات وحدة التحكم

### 1. إنشاء وحدة تحكم تمتد من GridJsControllerBase
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2 الحصول على JSON في الإجراء

هناك طريقتان للحصول على بيانات JSON في الإجراء الخاص بك:

الخيار 1: باستخدام GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
الخيار 2: باستخدام IGridJsService في GridJsControllerBase
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

للحصول على معلومات مفصلة ، يمكنك التحقق من المثال هنا:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
