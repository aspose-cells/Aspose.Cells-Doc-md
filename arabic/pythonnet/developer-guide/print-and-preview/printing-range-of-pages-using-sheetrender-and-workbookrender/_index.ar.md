---
title: طباعة نطاق الصفحات باستخدام SheetRender و WorkbookRender
type: docs
weight: 250
url: /ar/python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel بطباعة نطاق الصفحات من كتاب العمل أو ورقة العمل. تظهر اللقطة الشاشية التالية واجهة Microsoft Excel لتحديد نطاق الصفحات.

يوفر Aspose.Cells للبايثون via .NET طرق WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) و SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) لهذا الغرض.

{{% /alert %}} 

## **واجهة Microsoft Excel لتحديد نطاق الصفحات المراد طباعتها**
الشيفرة التالية توضح استخدام WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) و SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). إنها تطبع الصفحات 2-5 من الكتاب أو الورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingSpecificRangeOfPages.py" >}}
{{< app/cells/assistant language="python-net" >}}
