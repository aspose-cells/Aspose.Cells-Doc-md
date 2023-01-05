---
title: إعدادات GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/settings/
description: توضح هذه المقالة إعداد GridJs.
keywords: settings
---
هناك بعض الإعدادات التي يمكننا تحديدها من خلال ضبط GridWorkbookSettings:

 
- **[GridWorkbookSettings] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


على سبيل المثال ، تقوم الشفرة التالية بتعيين ReCalculateOnOpen على false لإيقاف caculate عند فتح الملف:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 قام الكود التالي بتعيين كاتب الملف:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
يمكنك التحقق من المزيد من الإعدادات في هذا الفصل.
 