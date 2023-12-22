---
title: Exporter les données des lignes visibles à partir d'une feuille de calcul
type: docs
weight: 10
url: /fr/net/export-visible-rows-data-from-worksheet/
description: Découvrez comment exporter les données des lignes visibles à partir d'une feuille de calcul via le Aspose.Cells for .NET API.
keywords: Export Visible Rows Data to DataTable, Export unhidden Rows Data to DataTable, Export Rows Data to DataTable and Exclude hidden rows, Ignore Hidden Rows while Exporting Worksheet Data to Data Table
---
{{% alert color="primary" %}}

 Vous pouvez exporter les données des feuilles de calcul vers des tableaux de données à l'aide de Aspose.Cells. Parfois, vous souhaitez exporter uniquement les données des lignes visibles. Aspose.Cells fournit un moyen d’y parvenir. Utilisez le[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)pour spécifier que vous souhaitez exporter uniquement les données des lignes visibles.

{{% /alert %}}

Cet exemple montre comment exporter les données de la feuille de calcul suivante. Les lignes 5, 6 et 7 sont masquées.

|**Exemples de données dans la feuille de calcul, les lignes 5, 6 et 7 sont masquées**|
| :- |
|![tâche : image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

 Une fois les données exportées vers une table de données à l'aide du[**Feuille de calcul.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) méthode avec le[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)option, cela ressemblera à ceci. Les lignes masquées sont tracées sous forme de lignes vides

|**Les lignes masquées sont exportées vers la table de données sous forme de lignes vides**|
| :- |
|![tâche : image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
