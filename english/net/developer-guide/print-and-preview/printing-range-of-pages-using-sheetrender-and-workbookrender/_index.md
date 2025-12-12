---
title: Printing Range of Pages using SheetRender and WorkbookRender
type: docs
weight: 250
url: /net/printing-range-of-pages-using-sheetrender-and-workbookrender/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Microsoft Excel allows you to print a range of pages of a workbook or worksheet. The following screenshot shows the Microsoft Excel interface to specify the range of pages.

Aspose.Cells provides the `WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)` and `SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)` methods for this purpose.

{{% /alert %}} 
## **Microsoft Excel Interface to Specify the Range of Pages to Print**
The following sample code illustrates the use of `WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)` and `SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)` methods. It prints pages 2‑5 of both the workbook and the worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
{{< app/cells/assistant language="csharp" >}}
