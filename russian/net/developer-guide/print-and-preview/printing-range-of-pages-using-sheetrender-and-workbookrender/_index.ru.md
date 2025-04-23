---
title: Печать диапазона страниц с использованием SheetRender и WorkbookRender
type: docs
weight: 250
url: /ru/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет печатать диапазон страниц книги или листа. Ниже приведен скриншот интерфейса Microsoft Excel для указания диапазона страниц.

Aspose.Cells предоставляет методы WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) и SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) для этой цели.

{{% /alert %}} 
## **Интерфейс Microsoft Excel для указания диапазона страниц для печати**
В следующем образцовом коде показано использование методов WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) и SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Он печатает страницы 2-5 книги и рабочего листа.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
{{< app/cells/assistant language="csharp" >}}
