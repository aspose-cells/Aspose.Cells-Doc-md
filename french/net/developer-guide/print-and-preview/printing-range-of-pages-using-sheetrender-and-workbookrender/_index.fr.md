---
title: Impression de la plage de pages à l aide de SheetRender et WorkbookRender
type: docs
weight: 250
url: /fr/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel vous permet d'imprimer une plage de pages du classeur ou de la feuille de calcul. La capture d'écran suivante montre l'interface de Microsoft Excel pour spécifier la plage de pages.

Aspose.Cells fournit les méthodes WorkbookRender.ToPrinter(nomImprimante, indexImpression, nombrePagesImpression) et SheetRender.ToPrinter(nomImprimante, indexImpression, nombrePagesImpression) à cet effet.

{{% /alert %}} 
## **Interface de Microsoft Excel pour spécifier la plage de pages à imprimer**
Le code d'exemple suivant illustre l'utilisation des méthodes WorkbookRender.ToPrinter(nomImprimante, indexImpression, nombrePagesImpression) et SheetRender.ToPrinter(nomImprimante, indexImpression, nombrePagesImpression). Il imprime les pages 2 à 5 du classeur et de la feuille de calcul.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
