---
title: Exporter les propriétés du classeur de document et de la feuille de calcul dans Excel vers la conversion HTML
type: docs
weight: 50
url: /fr/java/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---
## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel Microsoft est exporté au format HTML à l'aide de Microsoft Excel ou Aspose.Cells, il exporte également divers types de propriétés de document, de classeur et de feuille de calcul, comme indiqué dans la capture d'écran suivante. Vous pouvez éviter d'exporter ces propriétés en définissant le paramètre[**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportDocumentProperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorkbookProperties)et[**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportWorksheetProperties)comme**faux**. La valeur par défaut de ces propriétés est**vrai**. La capture d'écran suivante montre à quoi ressemblent ces propriétés dans le code HTML exporté.

![tâche : image_autre_texte](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exporter les propriétés du document, du classeur et de la feuille de calcul dans Excel vers la conversion HTML**

L'exemple de code suivant charge le[exemple de fichier Excel](61767784.xlsx)et le convertit en HTML et n'exporte pas les propriétés Document, Workbook et Worksheet dans[sortie HTML](61767783.zip).

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.java" >}}
