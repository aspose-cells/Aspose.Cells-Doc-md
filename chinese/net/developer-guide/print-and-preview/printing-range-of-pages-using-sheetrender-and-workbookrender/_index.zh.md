---
title: 使用 SheetRender 和 WorkbookRender 打印页面范围
type: docs
weight: 250
url: /zh/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel允许您打印工作簿或工作表的页面范围。 以下屏幕截图显示了指定页面范围的Microsoft Excel界面。

Aspose.Cells为此提供了WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)和SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)方法。

{{% /alert %}} 
## **指定图像或打印选项的PageIndex和PageCount属性渲染页面序列**
下面的示例代码演示了如何使用WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)和SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)方法。它打印工作簿和工作表的第2-5页。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
