---
title: Printing Range of Pages using SheetRender and WorkbookRender
type: docs
weight: 250
url: /python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel allows you to print range of pages of workbook or worksheet. The following screenshot shows the Microsoft Excel interface to specify the range of pages.

Aspose.Cells provides the WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) and SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) methods for this purpose.

{{% /alert %}} 
## **Microsoft Excel Interface to specify the Range of Pages to Print**
The following sample code illustrates the use of WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) and SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) methods. It prints the pages 2-5 of the workbook and worksheet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
{{< app/cells/assistant language="csharp" >}}
