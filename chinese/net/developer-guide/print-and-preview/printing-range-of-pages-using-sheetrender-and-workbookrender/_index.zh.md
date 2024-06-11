---
title: 使用 SheetRender 和 WorkbookRender 打印页面范围
type: docs
weight: 250
url: /zh/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel 允许您打印工作簿或工作表的页面范围。以下截图显示了指定页面范围的 Microsoft Excel 界面。

Aspose.Cells 提供了用于此目的的 WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) 和 SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) 方法。

{{% /alert %}} 
## **指定要打印的页面范围的 Microsoft Excel 界面**
以下示例代码演示了使用 WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) 和 SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) 方法。它打印工作簿和工作表的第 2-5 页。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
