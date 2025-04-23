---
title: Exporter les données des lignes visibles de la feuille de calcul
type: docs
weight: 10
url: /fr/net/export-visible-rows-data-from-worksheet/
description: Apprenez comment exporter les données des lignes visibles de la feuille de calcul via l API Aspose.Cells for .NET.
keywords: Exporter les données des lignes visibles dans le DataTable, Exporter les données des lignes non masquées dans le DataTable, Exporter les données des lignes dans le DataTable et Exclure les lignes masquées, Ignorer les lignes masquées lors de l exportation des données de la feuille de calcul dans le DataTable
---

{{% alert color="primary" %}}

Vous pouvez exporter des données des feuilles de calcul dans des tables de données en utilisant Aspose.Cells. Parfois, vous voulez exporter uniquement les données des lignes visibles. Aspose.Cells fournit un moyen d'y parvenir. Utilisez [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) pour spécifier que vous voulez exporter uniquement les données des lignes visibles.

{{% /alert %}}

Cet exemple montre comment exporter les données de la feuille de calcul suivante. Les lignes 5, 6 et 7 sont masquées.

|**Exemple de données dans la feuille de calcul, les lignes 5, 6 et 7 sont masquées**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

Une fois que les données sont exportées vers un DataTable en utilisant la méthode [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) avec l'option [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows), elles ressembleront à ceci. Les lignes masquées sont représentées sous forme de lignes vierges

|**Les lignes masquées sont exportées vers le tableau de données sous forme de lignes vides**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
