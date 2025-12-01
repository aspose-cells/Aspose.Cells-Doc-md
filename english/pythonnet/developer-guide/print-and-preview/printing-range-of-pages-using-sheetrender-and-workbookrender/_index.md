---
title: Printing Range of Pages using SheetRender and WorkbookRender
type: docs
weight: 250
url: /python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Microsoft Excel allows you to print range of pages of workbook or worksheet. The following screenshot shows the Microsoft Excel interface to specify the range of pages.

Aspose.Cells for Python via .NET provides the WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) and SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) methods for this purpose.

{{% /alert %}} 

## **Microsoft Excel Interface to specify the Range of Pages to Print**
The following sample code illustrates the use of WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) and SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) methods. It prints the pages 2-5 of the workbook and worksheet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingSpecificRangeOfPages.py" >}}
{{< app/cells/assistant language="python-net" >}}
