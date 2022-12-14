---
title: Supprimer le tableau croisé dynamique d'une feuille de calcul
type: docs
weight: 60
url: /fr/net/delete-pivot-table-from-a-worksheet/
description: C# code pour supprimer le tableau croisé dynamique pour les feuilles de calcul Excel
keywords: c# remove pivot table from worksheet, c# remove pivot table from excel, how to delete pivot table with c#, delete pivot table with c#, delete pivot table from excel with c#, c# delete pivot table, c# remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells fournit une fonctionnalité pour supprimer ou supprimer le tableau croisé dynamique d'une feuille de calcul. Vous pouvez supprimer le tableau croisé dynamique à l'aide de l'objet tableau croisé dynamique ou de la position du tableau croisé dynamique. Veuillez utiliser le[**Feuille de calcul.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) méthode pour supprimer le tableau croisé dynamique à l'aide d'un objet tableau croisé dynamique et[**Feuille de calcul.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) méthode pour supprimer un objet de tableau croisé dynamique en utilisant sa position à l'intérieur de la collection de tableaux croisés dynamiques.

{{% /alert %}}

 L'exemple de code suivant supprime deux tableaux croisés dynamiques de la feuille de calcul. Tout d'abord, il supprime le tableau croisé dynamique à l'aide de[**Feuille de calcul.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) méthode, puis il supprime le tableau croisé dynamique à l'aide[**Feuille de calcul.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) méthode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
