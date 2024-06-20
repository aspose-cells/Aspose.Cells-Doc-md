---
title: Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur
type: docs
weight: 120
url: /fr/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajuster automatiquement les colonnes et les lignes lors du chargement de votre fichier HTML à l'intérieur de l'objet Workbook. Veuillez définir la propriété [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) sur **true** à cette fin.

## **Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur**

Le code d'exemple suivant charge d'abord le fichier HTML d'exemple dans Workbook sans aucune option de chargement et l'enregistre au format XLSX. Ensuite, il charge à nouveau le fichier HTML d'exemple dans Workbook mais cette fois, il charge le HTML après avoir défini la propriété [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) sur **true** et l'enregistre au format XLSX. Veuillez télécharger les deux fichiers Excel en sortie, à savoir [Fichier Excel en sortie sans ajustement automatique des colonnes et des lignes](outputWithout_AutoFitColsAndRows.xlsx) et [Fichier Excel en sortie avec ajustement automatique des colonnes et des lignes](outputWith_AutoFitColsAndRows.xlsx). La capture d'écran suivante montre l'effet de la propriété [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows) sur les deux fichiers Excel en sortie.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

