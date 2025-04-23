---
title: Exporter les propriétés du classeur et des feuilles de calcul du document en Excel vers la conversion HTML
type: docs
weight: 50
url: /fr/net/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
---

## **Scénarios d'utilisation possibles**

Lorsque le fichier Excel Microsoft est exporté en HTML à l'aide de Microsoft Excel ou Aspose.Cells, il exporte également divers types de propriétés du Document, du Classeur et des Feuilles de calcul comme le montre la capture d'écran suivante. Vous pouvez éviter d'exporter ces propriétés en définissant les propriétés [**HtmlSaveOptions.ExportDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportdocumentproperties), [**HtmlSaveOptions.ExportWorkbookProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworkbookproperties) et [**HtmlSaveOptions.ExportWorksheetProperties**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetproperties) sur **false**. La valeur par défaut de ces propriétés est **true**. La capture d'écran suivante montre à quoi ressemblent ces propriétés dans le HTML exporté.

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)

## **Exporter les propriétés du Document, du Classeur et des Feuilles de calcul lors de la conversion d'Excel en HTML**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767776.xlsx) et le convertit en HTML sans exporter les propriétés du Document, du Classeur et des Feuilles de calcul dans le [HTML de sortie](61767779.zip).

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExportDocumentWorkbookAndWorksheetPropertiesInHTML.cs" >}}
{{< app/cells/assistant language="csharp" >}}
