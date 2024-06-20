---
title: Travail sur les formats d affichage des données de DataField dans le tableau croisé dynamique
type: docs
weight: 150
url: /fr/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge tous les formats d'affichage des données de DataField.

{{% /alert %}}

## **Option de format d'affichage "Classer du plus petit au plus grand" et "Classer du plus grand au plus petit"**

Aspose.Cells permet de définir l'option de format d'affichage pour les champs de tableau croisé dynamique. Pour cela, l'API fournit la propriété [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat). Pour classer du plus grand au plus petit, vous pouvez définir la propriété [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) sur [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK_LARGEST_TO_SMALLEST). Le code suivant démontre comment définir les options de format d'affichage.

Les fichiers source et de sortie de l'échantillon peuvent être téléchargés d'ici pour tester le code d'échantillon:

[Fichier Excel source](PivotTableSample.xlsx)

[Fichier Excel de sortie](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
