---
title: Exporter les commentaires lors de l enregistrement d un fichier Excel en HTML
type: docs
weight: 40
url: /fr/java/export-comments-while-saving-excel-file-to-html/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, les commentaires ne sont pas exportés. Cependant, Aspose.Cells propose cette fonctionnalité en utilisant la propriété [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#IsExportComments). Si vous la définissez sur **true**, alors HTML affichera également les commentaires présents dans votre fichier Excel.

## **Exporter les commentaires lors de l'enregistrement d'un fichier Excel en HTML**

Le code d'exemple suivant explique l'utilisation de la propriété [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#IsExportComments). La capture d'écran montre l'effet du code sur le HTML lorsque la propriété est définie sur **true**. Veuillez télécharger le [fichier Excel d'exemple](50528270.xlsx) et le [HTML généré](50528269) pour référence.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ExportCommentsWhileSavingExcelFileToHtml.java" >}}
