---
title: Utilisation des formats d'affichage de données de DataField dans le tableau croisé dynamique
type: docs
weight: 150
url: /fr/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---
{{% alert color="primary" %}}

Aspose.Cells prend en charge tous les formats d'affichage de données de DataField.

{{% /alert %}}

## **Option de format d'affichage "Classer du plus petit au plus grand" et "Classer du plus grand au plus petit"**

Aspose.Cells offre la possibilité de définir l'option de format d'affichage pour les champs pivots. Pour cela, le API fournit le[**PivotField.DataDisplayFormatPivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) la propriété. Pour classer le plus grand au plus petit, vous pouvez définir le[**PivotField.DataDisplayFormatPivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat)propriété à[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK_LARGEST_TO_SMALLEST). L'extrait de code suivant illustre la définition des options de format d'affichage.

Des exemples de fichiers source et de sortie peuvent être téléchargés ici pour tester l'exemple de code :

[Fichier Excel source](PivotTableSample.xlsx)

[Fichier Excel de sortie](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
