---
title: Travail sur les formats d affichage des données de DataField dans le tableau croisé dynamique
type: docs
weight: 140
url: /fr/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ supporte tous les formats d’affichage des données de DataField.

{{% /alert %}}

## **Option de format d'affichage "Classer du plus petit au plus grand" et "Classer du plus grand au plus petit"**

ASpose.Cells permet de définir l'option de format d'affichage pour les champs de tableau croisé dynamique. Pour cela, l'API fournit la propriété [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-). Pour classer du plus grand au plus petit, vous pouvez définir la propriété [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) sur [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/). Le code suivant montre comment définir les options de format d'affichage.

Les fichiers source et de sortie de l'échantillon peuvent être téléchargés d'ici pour tester le code d'échantillon:

[Fichier Excel source](101089332.xlsx)

[Fichier Excel de sortie](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}

