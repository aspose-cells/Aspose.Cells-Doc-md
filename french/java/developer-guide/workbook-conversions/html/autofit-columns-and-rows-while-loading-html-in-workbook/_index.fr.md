---
title: Ajuster automatiquement les colonnes et les lignes lors du chargement du code HTML dans le classeur
type: docs
weight: 70
url: /fr/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---
## **Scénarios d'utilisation possibles**

 Vous pouvez ajuster automatiquement les colonnes et les lignes lors du chargement de votre fichier HTML dans le**[Classeur](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** objet. Veuillez définir le**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** propriété à**vrai**dans ce but.

## **Ajuster automatiquement les colonnes et les lignes lors du chargement du code HTML dans le classeur**

 L'exemple de code suivant charge d'abord l'exemple de code HTML dans Workbook sans aucune option de chargement et l'enregistre au format XLSX. Il charge ensuite à nouveau l'exemple de code HTML dans le classeur, mais cette fois, il charge le code HTML après avoir défini le**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)** propriété à**vrai**et l'enregistre au format XLSX. Veuillez télécharger les deux fichiers Excel de sortie, c'est-à-dire[Fichier Excel de sortie sans AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx) et[Fichier Excel de sortie avec AutoFitColsAndRows](outputWith_AutoFitColsAndRows.xlsx) . La capture d'écran suivante montre l'effet de**[HtmlLoadOptions.AutoFitColsAndRows](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows)**propriété sur les deux fichiers Excel de sortie.

![tâche : image_autre_texte](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
