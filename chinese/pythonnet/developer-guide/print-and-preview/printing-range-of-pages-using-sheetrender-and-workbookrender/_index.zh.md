---
title: 使用 SheetRender 和 WorkbookRender 打印页面范围
type: docs
weight: 250
url: /zh/python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel 允许您打印工作簿或工作表的页面范围。以下截图显示了指定页面范围的 Microsoft Excel 界面。

Aspose.Cells for Python via .NET 为此提供了 WorkbookRender.ToPrinter（字符串打印机名称，整型打印页索引，整型打印页数）和 SheetRender.ToPrinter（字符串打印机名称，整型打印页索引，整型打印页数）方法。

{{% /alert %}} 

## **指定要打印的页面范围的 Microsoft Excel 界面**
以下示例代码演示了使用 WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) 和 SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) 方法。它打印工作簿和工作表的第 2-5 页。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingSpecificRangeOfPages.py" >}}
{{< app/cells/assistant language="python-net" >}}
