---
title: Exporter les propriétés du classeur et des feuilles de calcul du document en Excel vers la conversion HTML
type: docs
weight: 50
url: /fr/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Scénarios d'utilisation possibles**

Lorsque le fichier Microsoft Excel est exporté au format HTML à l'aide de Microsoft Excel ou d'Aspose.Cells, il exporte également divers types de propriétés de document, de classeur et de feuille de calcul comme le montre la capture d'écran suivante. Vous pouvez éviter d'exporter ces propriétés en définissant les [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties) et [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties) comme **faux**. La valeur par défaut de ces propriétés est **vrai**. La capture d'écran suivante montre à quoi ressemblent ces propriétés dans le HTML exporté.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exporter les propriétés du Document, du Classeur et des Feuilles de calcul lors de la conversion d'Excel en HTML**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767784.xlsx) et le convertit en HTML sans exporter les propriétés du document, du classeur et de la feuille de calcul dans le [HTML de sortie](61767783.zip).

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
