---
title: Drucken des Seitenbereichs mit SheetRender und WorkbookRender
type: docs
weight: 250
url: /de/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---
{{% alert color="primary" %}} 

Microsoft Mit Excel können Sie eine Reihe von Seiten einer Arbeitsmappe oder eines Arbeitsblatts drucken. Der folgende Screenshot zeigt die Microsoft Excel-Oberfläche zur Angabe des Seitenbereichs.

Aspose.Cells stellt für diesen Zweck die Methoden WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) und SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) bereit.

{{% /alert %}} 
## **Microsoft Excel-Schnittstelle zum Festlegen des zu druckenden Seitenbereichs**
Der folgende Beispielcode veranschaulicht die Verwendung der Methoden WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) und SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Es druckt die Seiten 2-5 der Arbeitsmappe und des Arbeitsblatts.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
