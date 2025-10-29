--- 
title: Exporter les commentaires lors de l enregistrement d un fichier Excel en HTML avec Golang via C++ 
linktitle: Exporter les commentaires lors de l enregistrement d un fichier Excel en HTML 
type: docs 
weight: 40 
url: /fr/go-cpp/export-comments-while-saving-excel-file-to/ 
description: Apprenez comment exporter des commentaires lors de l enregistrement de fichiers Excel en HTML en utilisant Aspose.Cells avec Golang via C++. 
--- 

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, les commentaires ne sont pas exportés. Cependant, Aspose.Cells offre cette fonctionnalité via la propriété [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/isexportcomments/). Si vous la définissez à **true**, les commentaires présents dans votre fichier Excel seront également affichés dans le HTML.

## **Exporter les commentaires lors de l'enregistrement d'un fichier Excel en HTML**

Le code d'exemple ci-dessous explique l'utilisation de la propriété [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/isexportcomments/). La capture d'écran montre l'effet du code sur le HTML lorsqu'il est défini à **true**. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) et le [HTML généré](5052826.txt) en référence.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportCommentsWhileSavingExcelFileToHtml.go" >}}
