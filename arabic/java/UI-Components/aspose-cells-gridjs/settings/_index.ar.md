---
title: إعدادات لـ GridJs
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/settings/
description: يصف هذا المقال الإعداد لـ GridJs.
keywords: GridJs، الإعدادات، GridWorkbookSettings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


هناك بعض الإعدادات التي يمكننا تحديدها عن طريق تعيين GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


على سبيل المثال، يقوم الكود التالي بتعيين ReCalculateOnOpen إلى القيمة false لإيقاف الحساب عند فتح الملف:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 الكود التالي يقوم بتعيين المؤلف للملف:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
يمكنك التحقق من المزيد من الإعدادات في هذا الفصيل.

