---
title: Désactiver les rubans du tableau croisé dynamique
type: docs
weight: 90
url: /fr/net/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

Les rapports basés sur des tableaux croisés dynamiques sont utiles mais sujets aux erreurs si les utilisateurs cibles n'ont pas une connaissance détaillée d'Excel pour configurer ces rapports. Dans ces circonstances, les organisations voudront empêcher les utilisateurs de modifier un rapport basé sur un tableau croisé dynamique. Les fonctionnalités courantes des tableaux croisés dynamiques, telles que l'ajout de filtres, de segments, de champs supplémentaires ou la modification de l'ordre de certaines choses dans le rapport, ne sont généralement pas recommandées pour tous les utilisateurs. D'autre part, ces utilisateurs pourront également actualiser le rapport et utiliser des filtres ou des trancheurs existants. Aspose.Cells a fourni cette capacité aux développeurs pour empêcher les utilisateurs de modifier ces rapports lors de la création de ces rapports. À cette fin, Excel fournit une fonctionnalité pour désactiver le ruban du tableau croisé dynamique et la même chose est fournie par Aspose.Cells, c'est-à-dire que le développeur peut désactiver le ruban qui contient des contrôles pour modifier ces rapports.

{{% /alert %}}

## **Désactiver le ruban du tableau croisé dynamique à l'aide de PivotTable.EnableWizard**

Le code suivant illustre cette fonctionnalité en accédant à un tableau croisé dynamique à partir d'une feuille, puis en définissant[**Activer l'assistant**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) à**faux** . Un exemple de fichier de tableau croisé dynamique peut être téléchargé à partir de ce[lien](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
