---
title: Печать диапазона страниц с использованием SheetRender и WorkbookRender
type: docs
weight: 250
url: /ru/python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет печатать диапазон страниц книги или листа. Ниже приведен скриншот интерфейса Microsoft Excel для указания диапазона страниц.

API Aspose.Cells for Python via .NET предоставляет методы WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) и SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) для этой цели.

{{% /alert %}} 

## **Интерфейс Microsoft Excel для указания диапазона страниц для печати**
В следующем образцовом коде показано использование методов WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) и SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Он печатает страницы 2-5 книги и рабочего листа.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingSpecificRangeOfPages.py" >}}
{{< app/cells/assistant language="python-net" >}}
