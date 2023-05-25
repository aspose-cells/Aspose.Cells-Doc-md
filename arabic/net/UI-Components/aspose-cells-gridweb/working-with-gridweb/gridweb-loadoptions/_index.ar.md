---
title: LoadOptions لـ GridWeb
type: docs
weight: 90
url: /ar/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

هناك بعض خيارات التحميل التي يمكننا تعيينها قبل استيراد الملف.

 يمكننا ان نستخدم[GridLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)(للملف العام) و[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) (لملف csv)
 
{{% /alert %}} 
##  ** تحميل مع ترميز آخر**
بالنسبة لملف csv ، فهو في الواقع ملف نصي ، بدون الترميز المحدد الموضح في ملف تنسيق xlsx.

لذلك ، يمكن للمستخدمين تعيين ترميز أحرف معين قبل تحميل الملف.

إليك نموذج كود للتحميل بالصينية:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```