---
title: Impresión de rango de páginas usando SheetRender y WorkbookRender
type: docs
weight: 250
url: /es/python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel te permite imprimir un rango de páginas de un libro o una hoja de trabajo. La siguiente captura de pantalla muestra la interfaz de Microsoft Excel para especificar el rango de páginas.

Aspose.Cells para Python via .NET ofrece los métodos WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) y SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) para este propósito.

{{% /alert %}} 

## **Interfaz de Microsoft Excel para especificar el rango de páginas a imprimir**
El siguiente código de ejemplo ilustra el uso de los métodos WorkbookRender.ToPrinter (string PrinterName, int PrintPageIndex, int PrintPageCount) y SheetRender.ToPrinter (string PrinterName, int PrintPageIndex, int PrintPageCount). Imprime las páginas 2-5 del libro y la hoja de trabajo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingSpecificRangeOfPages.py" >}}
