---
title: Ajustement automatique des colonnes et des lignes lors du chargement de HTML dans le classeur
type: docs
weight: 120
url: /fr/net/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Scénarios d'utilisation possibles**

Vous pouvez ajuster automatiquement les colonnes et les lignes lors du chargement de votre fichier HTML dans l'objet Workbook. Veuillez définir le**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** propriété à**vrai**dans ce but.

## **Ajustement automatique des colonnes et des lignes lors du chargement de HTML dans le classeur**

 L'exemple de code suivant charge d'abord l'exemple HTML dans Workbook sans aucune option de chargement et l'enregistre au format XLSX. Il charge ensuite à nouveau l'exemple HTML dans Workbook mais cette fois, il charge le HTML après avoir défini le**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)** propriété à**vrai**et l'enregistre au format XLSX. Veuillez télécharger les deux fichiers Excel de sortie, c'est-à-dire[Fichier Excel de sortie sans AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) et[Fichier Excel de sortie avec AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . La capture d'écran suivante montre l'effet de**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/autofitcolsandrows)**propriété sur les deux fichiers Excel de sortie.

![tâche : image_autre_texte](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-AutoFitColumnsandRowsWhileLoadingHTMLInWorkbook-1.cs" >}}

