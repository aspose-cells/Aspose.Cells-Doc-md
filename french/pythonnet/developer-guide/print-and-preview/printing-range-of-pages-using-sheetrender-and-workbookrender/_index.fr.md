---
title: Impression de la plage de pages à l aide de SheetRender et WorkbookRender
type: docs
weight: 250
url: /fr/python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel vous permet d'imprimer une plage de pages du classeur ou de la feuille de calcul. La capture d'écran suivante montre l'interface de Microsoft Excel pour spécifier la plage de pages.

Aspose.Cells pour Python via .NET fournit les méthodes WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) et SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) à cette fin.

{{% /alert %}} 

## **Interface de Microsoft Excel pour spécifier la plage de pages à imprimer**
Le code d'exemple suivant illustre l'utilisation des méthodes WorkbookRender.ToPrinter(nomImprimante, indexImpression, nombrePagesImpression) et SheetRender.ToPrinter(nomImprimante, indexImpression, nombrePagesImpression). Il imprime les pages 2 à 5 du classeur et de la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingSpecificRangeOfPages.py" >}}
{{< app/cells/assistant language="python-net" >}}
