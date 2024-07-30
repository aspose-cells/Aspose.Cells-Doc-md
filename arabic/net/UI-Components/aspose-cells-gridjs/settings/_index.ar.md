---
title: إعدادات لـ GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/settings/
description: يصف هذا المقال الإعداد لـ GridJs.
keywords: GridJs، الإعدادات، GridWorkbookSettings
aliases:
  - /net/aspose-cells-gridjs/how-to-use-setting/
  - /net/aspose-cells-gridjs/work-with-setting/
---


هناك بعض الإعدادات التي يمكننا تحديدها عن طريق تعيين GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


على سبيل المثال، يقوم الكود التالي بتعيين ReCalculateOnOpen إلى القيمة false لإيقاف الحساب عند فتح الملف:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 الكود التالي يقوم بتعيين المؤلف للملف:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
يمكنك التحقق من المزيد من الإعدادات في هذا الفصيل.

