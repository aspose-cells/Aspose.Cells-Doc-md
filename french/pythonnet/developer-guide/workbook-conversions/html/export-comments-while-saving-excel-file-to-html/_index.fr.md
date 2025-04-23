---
title: Exporter les commentaires lors de l enregistrement d un fichier Excel en HTML
type: docs
weight: 40
url: /fr/python-net/export-comments-while-saving-excel-file-to/
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, les commentaires ne sont pas exportés. Cependant, Aspose.Cells pour Python via .NET offre cette fonctionnalité en utilisant la propriété [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). Si vous la définissez sur **true**, alors le HTML affichera aussi les commentaires présents dans votre fichier Excel.

## **Exporter les commentaires lors de l'enregistrement d'un fichier Excel en HTML**

Le code d'exemple suivant explique l'utilisation de la propriété [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). La capture d'écran montre l'effet du code sur le HTML lorsqu'il est défini sur **true**. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) et le [HTML généré](5052826.txt) pour référence.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
