---
title: Supprimer le tableau croisé dynamique d une feuille de calcul
type: docs
weight: 60
url: /fr/net/delete-pivot-table-from-a-worksheet/
description: Code C# pour supprimer le tableau croisé dynamique des feuilles de calcul Excel
keywords: c# supprimer un tableau croisé dynamique d une feuille de calcul, c# supprimer un tableau croisé dynamique d Excel, comment supprimer un tableau croisé dynamique avec c#, supprimer un tableau croisé dynamique avec c#, supprimer un tableau croisé dynamique d Excel avec c#, c# supprimer un tableau croisé dynamique, c# supprimer un tableau croisé dynamique, supprimer un tableau croisé dynamique, comment supprimer un tableau croisé dynamique
---

{{% alert color="primary" %}}

Aspose.Cells offre une fonctionnalité pour supprimer ou retirer un tableau croisé dynamique d'une feuille de calcul. Vous pouvez supprimer le tableau croisé dynamique en utilisant l'objet tableau croisé dynamique ou la position du tableau croisé dynamique. Veuillez utiliser la méthode [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) pour supprimer le tableau croisé dynamique en utilisant l'objet tableau croisé dynamique et la méthode [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) pour supprimer l'objet tableau croisé dynamique en utilisant sa position dans la collection de tableaux croisés dynamiques.

{{% /alert %}}

Le code d'exemple suivant supprime deux tableaux croisés dynamiques de la feuille de calcul. D'abord, il supprime un tableau croisé dynamique en utilisant la méthode [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) et ensuite il supprime un tableau croisé dynamique en utilisant la méthode [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
