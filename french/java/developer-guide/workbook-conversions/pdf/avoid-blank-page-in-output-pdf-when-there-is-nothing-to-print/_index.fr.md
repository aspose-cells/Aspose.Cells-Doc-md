---
title: Éviter une page vierge dans le PDF de sortie lorsqu il n y a rien à imprimer
type: docs
weight: 30
url: /fr/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel est vide et que l'utilisateur le sauve en PDF à l'aide d'Aspose.Cells, une page vierge est générée dans le PDF de sortie. Parfois, ce comportement par défaut est indésirable. Aspose.Cells fournit la propriété [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) pour gérer ce problème. Si vous le définissez sur **false**, alors [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) se produira chaque fois qu'il n'y a rien à imprimer dans le PDF de sortie.

## **Éviter la page blanche dans le PDF final lorsqu'il n'y a rien à imprimer**

Le code d'exemple suivant crée un classeur vide puis le sauvegarde en tant que PDF de sortie après avoir défini la propriété [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) comme false. Comme il n'y a rien à imprimer dans le PDF de sortie, [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) se produit comme indiqué ci-dessous.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Exception**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
