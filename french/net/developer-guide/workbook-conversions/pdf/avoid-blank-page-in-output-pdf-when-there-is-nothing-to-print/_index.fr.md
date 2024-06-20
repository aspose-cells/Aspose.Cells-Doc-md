---
title: Éviter une page vierge dans le PDF de sortie lorsqu il n y a rien à imprimer
type: docs
weight: 30
url: /fr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel est vide et que l'utilisateur le sauve en PDF à l'aide d'Aspose.Cells, une page vierge est générée dans le PDF de sortie. Parfois, ce comportement par défaut est indésirable. Aspose.Cells fournit la propriété [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) pour gérer ce problème. Si vous le définissez sur **false**, alors [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) se produira chaque fois qu'il n'y a rien à imprimer dans le PDF de sortie.

## **Éviter la page blanche dans le PDF final lorsqu'il n'y a rien à imprimer**

Le code d'exemple suivant crée un classeur vide, puis le sauve sous forme de PDF après avoir défini la propriété [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) sur **false**. Comme il n'y a rien à imprimer dans le PDF de sortie, [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) se produit comme indiqué ci-dessous.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Exception**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
