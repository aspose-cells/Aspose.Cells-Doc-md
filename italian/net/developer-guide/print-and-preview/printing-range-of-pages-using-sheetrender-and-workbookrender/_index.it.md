---
title: Stampa dell'intervallo di pagine utilizzando SheetRender e WorkbookRender
type: docs
weight: 250
url: /it/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---
{{% alert color="primary" %}} 

Microsoft Excel consente di stampare un intervallo di pagine della cartella di lavoro o del foglio di lavoro. Lo screenshot seguente mostra l'interfaccia di Microsoft Excel per specificare l'intervallo di pagine.

Aspose.Cells fornisce i metodi WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) e SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) per questo scopo.

{{% /alert %}} 
## **Interfaccia Microsoft Excel per specificare l'intervallo di pagine da stampare**
Il codice di esempio seguente illustra l'uso dei metodi WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) e SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Stampa le pagine 2-5 della cartella di lavoro e del foglio di lavoro.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
