---
title: Supprimer le tableau croisé dynamique d'une feuille de calcul
type: docs
weight: 60
url: /fr/python-net/delete-pivot-table-from-a-worksheet/
description: Code Python via .NET pour supprimer le tableau croisé dynamique des feuilles de calcul Excel
keywords: Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET fournit une fonctionnalité permettant de supprimer ou de supprimer un tableau croisé dynamique d'une feuille de calcul. Vous pouvez supprimer le tableau croisé dynamique à l'aide d'un objet de tableau croisé dynamique ou de la position du tableau croisé dynamique. Veuillez utiliser le[**Feuille de travail.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) méthode pour supprimer le tableau croisé dynamique à l’aide de l’objet tableau croisé dynamique et[**Feuille de travail.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)méthode pour supprimer un objet de tableau croisé dynamique en utilisant sa position dans la collection de tableaux croisés dynamiques.

{{% /alert %}}

 L'exemple de code suivant supprime deux tableaux croisés dynamiques de la feuille de calcul. Tout d'abord, il supprime le tableau croisé dynamique en utilisant[**Feuille de travail.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) méthode, puis il supprime le tableau croisé dynamique à l'aide[**Feuille de travail.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) méthode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
