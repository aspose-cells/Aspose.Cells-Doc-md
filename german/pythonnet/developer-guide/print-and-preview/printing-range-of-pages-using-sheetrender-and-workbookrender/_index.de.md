---
title: Druckbereich von Seiten mit SheetRender und WorkbookRender
type: docs
weight: 250
url: /de/python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Ihnen, den Seitenbereich des Arbeitsmappen- oder Arbeitsblattes zu drucken. Der folgende Screenshot zeigt die Microsoft Excel-Benutzeroberfläche zur Angabe des Seitenbereichs.

Aspose.Cells für Python via .NET stellt die Methoden WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) und SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) für diesen Zweck bereit.

{{% /alert %}} 

## **Microsoft Excel-Benutzeroberfläche zur Angabe des Seitenbereichs zum Drucken**
Der folgende Beispielcode veranschaulicht die Verwendung der Methoden WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) und SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Es druckt die Seiten 2-5 des Arbeitsbuches und des Arbeitsblattes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingSpecificRangeOfPages.py" >}}
