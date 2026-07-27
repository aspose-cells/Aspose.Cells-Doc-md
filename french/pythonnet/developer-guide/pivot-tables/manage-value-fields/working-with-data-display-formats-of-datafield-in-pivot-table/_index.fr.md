---
title: Travail sur les formats d affichage des données de DataField dans le tableau croisé dynamique
type: docs
weight: 140
url: /fr/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Comment travailler avec les formats d affichage des données DataField dans un tableau croisé dynamique avec Aspose.Cells pour Python via .NET.
keywords: Aspose.Cells pour Python Excel, bibliothèque Python Excel, Travaillez avec les formats d affichage des données DataField dans un tableau croisé dynamique.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET prend en charge tous les formats d'affichage des données de DataField.

{{% /alert %}}

## **Comment définir l'option de format d'affichage "Classer du plus petit au plus grand" et "Classer du plus grand au plus petit"**

Aspose.Cells for Python via .NET offre la possibilité de définir l'option de format d'affichage pour les champs de tableau croisé. Pour cela, l'API fournit la propriété [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/). Pour classer du plus grand au plus petit, vous pouvez définir la propriété [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) sur [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/). Le code suivant montre comment définir les options de format d'affichage.

Les fichiers source et de sortie de l'échantillon peuvent être téléchargés d'ici pour tester le code d'échantillon:

[Fichier Excel source](101089332.xlsx)

[Fichier Excel de sortie](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
