---
title: Druckbereich von Seiten mit SheetRender und WorkbookRender
type: docs
weight: 250
url: /de/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Ihnen, den Seitenbereich des Arbeitsmappen- oder Arbeitsblattes zu drucken. Der folgende Screenshot zeigt die Microsoft Excel-Benutzeroberfläche zur Angabe des Seitenbereichs.

Aspose.Cells bietet die Methoden WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) und SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) für diesen Zweck.

{{% /alert %}} 
## **Microsoft Excel-Benutzeroberfläche zur Angabe des Seitenbereichs zum Drucken**
Der folgende Beispielcode veranschaulicht die Verwendung der Methoden WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) und SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Es druckt die Seiten 2-5 des Arbeitsbuches und des Arbeitsblattes.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
{{< app/cells/assistant language="csharp" >}}
