---
title: خيارات التحميل لـ GridWeb
type: docs
weight: 90
url: /ar/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: خيار التحميل ، خيارات التحميل ، إعداد ، تحميل ، خيارات ، خيار
description: يقدم هذا المقال كيفية العمل مع خيارات التحميل في GridWeb.
---

{{% alert color="primary" %}} 

هناك بعض خيارات التحميل يمكننا تحديدها قبل استيراد الملف.

يمكننا استخدام [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (للملف العام) و [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (لملف csv)	

{{% /alert %}} 
## **التحميل بترميز آخر**
بالنسبة لملف csv، فإنه في الواقع ملف قائم على النص، دون الترميز المحدد الموصوف في ملف تنسيق xlsx.

لذلك، يمكن للمستخدمين تحديد ترميز الحروف المحدد قبل تحميل الملف.

إليك رمز عينة للتحميل باللغة الصينية:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
