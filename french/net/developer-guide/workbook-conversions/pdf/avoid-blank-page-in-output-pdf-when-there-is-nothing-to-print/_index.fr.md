---
title: Évitez les pages vierges dans le PDF de sortie lorsqu'il n'y a rien à imprimer
type: docs
weight: 30
url: /fr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel est vide et que l'utilisateur l'enregistre au format PDF à l'aide de Aspose.Cells, il affiche une page vierge dans le PDF de sortie. Parfois, ce comportement par défaut n'est pas souhaitable. Aspose.Cells fournit le[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) propriété pour régler ce problème. Si vous le définissez comme**faux**, alors[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)se produira chaque fois qu'il n'y a rien à imprimer dans le PDF de sortie.

## **Évitez les pages vierges dans le PDF de sortie lorsqu'il n'y a rien à imprimer**

L'exemple de code suivant crée un classeur vide, puis l'enregistre au format PDF après avoir défini le[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) propriété comme**faux**. Puisqu'il n'y a rien à imprimer dans le PDF de sortie, le[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)se produit comme indiqué ci-dessous.

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Exception**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
