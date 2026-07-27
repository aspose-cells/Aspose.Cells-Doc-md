---
title: Travail sur les formats d affichage des données de DataField dans le tableau croisé dynamique
type: docs
weight: 140
url: /fr/net/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge tous les formats d'affichage des données de DataField.

{{% /alert %}}

## **Option de format d'affichage "Classer du plus petit au plus grand" et "Classer du plus grand au plus petit"**

ASpose.Cells permet de définir l'option de format d'affichage pour les champs de tableau croisé dynamique. Pour cela, l'API fournit la propriété [**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/). Pour classer du plus grand au plus petit, vous pouvez définir la propriété [**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/) sur [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfielddatadisplayformat). Le code suivant montre comment définir les options de format d'affichage.

Les fichiers source et de sortie de l'échantillon peuvent être téléchargés d'ici pour tester le code d'échantillon:

[Fichier Excel source](101089332.xlsx)

[Fichier Excel de sortie](101089333.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTables-PivotTableDataDisplayFormatRanking-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
