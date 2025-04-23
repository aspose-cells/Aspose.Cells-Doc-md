---
title: Stampa Intervallo di pagine utilizzando SheetRender e WorkbookRender
type: docs
weight: 250
url: /it/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel consente di stampare un intervallo di pagine di un documento o di un foglio di lavoro. La seguente schermata mostra l'interfaccia di Microsoft Excel per specificare l'intervallo di pagine.

Aspose.Cells fornisce i metodi WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) e SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) per questo scopo.

{{% /alert %}} 
## **Interfaccia di Microsoft Excel per specificare l'intervallo di pagine da stampare**
Il seguente codice di esempio illustra l'uso dei metodi WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) e SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Stampa le pagine 2-5 del documento e del foglio di lavoro.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
{{< app/cells/assistant language="csharp" >}}
