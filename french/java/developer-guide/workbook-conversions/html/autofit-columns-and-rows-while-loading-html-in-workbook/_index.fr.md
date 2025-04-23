---
title: Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur
type: docs
weight: 70
url: /fr/java/autofit-columns-and-rows-while-loading-html-in-workbook/
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajuster automatiquement les colonnes et les lignes tout en chargeant votre fichier HTML à l'intérieur de l'objet [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Veuillez définir la propriété [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) sur **true** à cette fin.

## **Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur**

Le code d'exemple suivant charge d'abord le HTML d'exemple dans Workbook sans aucune option de chargement et le sauvegarde au format XLSX. Ensuite, le code charge à nouveau le HTML d'exemple dans Workbook, mais cette fois-ci, il charge le HTML après avoir défini la propriété [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) sur **true** et le sauvegarde au format XLSX. Veuillez télécharger les deux fichiers Excel de sortie, à savoir [Fichier Excel de sortie sans ajustement automatique des colonnes et des lignes](outputWithout_AutoFitColsAndRows.xlsx) et [Fichier Excel de sortie avec ajustement automatique des colonnes et des lignes](outputWith_AutoFitColsAndRows.xlsx). La capture d'écran suivante montre l'effet de la propriété [**HtmlLoadOptions.AutoFitColsAndRows**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#AutoFitColsAndRows) sur les deux fichiers Excel de sortie.

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-AutoFitColumnsRowsLoadingHTML-1.java" >}}
{{< app/cells/assistant language="java" >}}
