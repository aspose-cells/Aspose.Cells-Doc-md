---
title: Печать диапазона страниц с использованием SheetRender и WorkbookRender
type: docs
weight: 250
url: /ru/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---
{{% alert color="primary" %}} 

Microsoft Excel позволяет печатать диапазон страниц книги или листа. На следующем снимке экрана показан интерфейс Excel Microsoft для указания диапазона страниц.

Aspose.Cells предоставляет для этой цели методы WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) и SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount).

{{% /alert %}} 
## **Microsoft Интерфейс Excel для указания диапазона страниц для печати**
В следующем примере кода показано использование методов WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) и SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Он печатает страницы 2-5 книги и рабочего листа.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
