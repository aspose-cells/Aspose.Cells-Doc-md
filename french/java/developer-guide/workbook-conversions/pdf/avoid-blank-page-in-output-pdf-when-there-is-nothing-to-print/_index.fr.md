---
title: Évitez les pages vierges dans le PDF de sortie lorsqu'il n'y a rien à imprimer
type: docs
weight: 30
url: /fr/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel est vide et que l'utilisateur l'enregistre au format PDF à l'aide de Aspose.Cells, il affiche une page vierge dans le PDF de sortie. Parfois, ce comportement par défaut n'est pas souhaitable. Aspose.Cells fournit le[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) propriété pour régler ce problème. Si vous le définissez comme**faux**, alors[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)se produira chaque fois qu'il n'y a rien à imprimer dans le PDF de sortie.

## **Évitez les pages vierges dans le PDF de sortie lorsqu'il n'y a rien à imprimer**

L'exemple de code suivant crée un classeur vide, puis l'enregistre en tant que sortie PDF après avoir défini le[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) propriété comme**faux**. Puisqu'il n'y a rien à imprimer dans le PDF de sortie, le[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)se produit comme indiqué ci-dessous.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Exception**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
