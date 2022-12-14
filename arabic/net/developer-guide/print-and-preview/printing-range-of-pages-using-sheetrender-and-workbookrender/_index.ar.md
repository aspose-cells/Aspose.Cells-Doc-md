---
title: طباعة مجموعة من الصفحات باستخدام SheetRender و WorkbookRender
type: docs
weight: 250
url: /ar/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---
{{% alert color="primary" %}} 

Microsoft يسمح لك برنامج Excel بطباعة نطاق من صفحات المصنف أو ورقة العمل. تُظهر لقطة الشاشة التالية واجهة Microsoft Excel لتحديد نطاق الصفحات.

يوفر Aspose.Cells طريقتين WorkbookRender.ToPrinter (سلسلة PrinterName، int PrintPageIndex، int PrintPageCount) و SheetRender.ToPrinter (سلسلة PrinterName، int PrintPageIndex، int PrintPageCount) لهذا الغرض.

{{% /alert %}} 
## **Microsoft واجهة Excel لتحديد نطاق الصفحات المطلوب طباعتها**
يوضح نموذج التعليمات البرمجية التالي استخدام WorkbookRender.ToPrinter (سلسلة PrinterName، int PrintPageIndex، int PrintPageCount) و SheetRender.ToPrinter (سلسلة PrinterName، int PrintPageIndex، int PrintPageCount). يقوم بطباعة الصفحات 2-5 من المصنف وورقة العمل.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
