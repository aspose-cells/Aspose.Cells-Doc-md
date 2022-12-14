---
title: Exporter les données des lignes visibles à partir de la feuille de calcul
type: docs
weight: 10
url: /fr/net/export-visible-rows-data-from-worksheet/
---
{{% alert color="primary" %}}

 Vous pouvez exporter des données de feuilles de calcul dans des tableaux de données à l'aide de Aspose.Cells. Parfois, vous souhaitez exporter uniquement les données des lignes visibles. Aspose.Cells fournit un moyen d'y parvenir. Utilisez le[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) pour spécifier que vous souhaitez exporter uniquement les données des lignes visibles.

{{% /alert %}}

Cet exemple montre comment exporter des données à partir de la feuille de calcul suivante. Les lignes 5, 6 et 7 sont masquées.

|**Exemples de données dans la feuille de calcul, les lignes 5, 6 et 7 sont masquées**|
|:- |
|![tâche : image_autre_texte](export-visible-rows-data-from-worksheet_1.png)|

Une fois les données exportées vers une table de données à l'aide de la[**Feuille de calcul.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) méthode avec la[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)option, il ressemblera à ceci. Les lignes masquées sont tracées sous forme de lignes vides

|**Les lignes masquées sont exportées vers la table de données en tant que lignes vides**|
|:- |
|![tâche : image_autre_texte](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
