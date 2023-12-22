---
title: Travailler avec les formats d'affichage des données de DataField dans le tableau croisé dynamique
type: docs
weight: 140
url: /fr/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Comment travailler avec les formats d'affichage des données de DataField dans le tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Work with data display formats of DataField in Pivot Table.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET prend en charge tous les formats d'affichage des données de DataField.

{{% /alert %}}

##  **Option de format d'affichage « Classer du plus petit au plus grand » et « Classer du plus grand au plus petit »**

Aspose.Cells for Python via .NET offre la possibilité de définir l'option de format d'affichage pour les champs pivots. Pour cela, le API met à disposition le[**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) propriété. Pour classer du plus grand au plus petit, vous pouvez définir le[**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/)propriété à[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/). L'extrait de code suivant illustre la définition des options de format d'affichage.

Des exemples de fichiers source et de sortie peuvent être téléchargés à partir d'ici pour tester l'exemple de code :

[Fichier Excel source](101089332.xlsx)

[Fichier Excel de sortie](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
