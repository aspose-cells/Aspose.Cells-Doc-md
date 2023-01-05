---
title: Impression d'une plage de pages à l'aide de SheetRender et WorkbookRender
type: docs
weight: 250
url: /fr/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---
{{% alert color="primary" %}} 

Microsoft Excel vous permet d'imprimer une plage de pages de classeur ou de feuille de calcul. La capture d'écran suivante montre l'interface Excel Microsoft pour spécifier la plage de pages.

Aspose.Cells fournit les méthodes WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) et SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) à cette fin.

{{% /alert %}} 
## **Microsoft Interface Excel pour spécifier la plage de pages à imprimer**
L'exemple de code suivant illustre l'utilisation des méthodes WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) et SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Il imprime les pages 2 à 5 du classeur et de la feuille de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
