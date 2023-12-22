---
title: Désactiver les rubans de tableau croisé dynamique
type: docs
weight: 90
url: /fr/python-net/disable-pivot-table-ribbons/
description: Comment désactiver les rubans de tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Disable Pivot Table Ribbons.
---
{{% alert color="primary" %}}

Les rapports basés sur des tableaux croisés dynamiques sont utiles mais sujets aux erreurs si les utilisateurs cibles n'ont pas une connaissance détaillée d'Excel pour configurer ces rapports. Dans ces circonstances, les organisations voudront empêcher les utilisateurs de modifier un rapport basé sur un tableau croisé dynamique. Les fonctionnalités courantes des tableaux croisés dynamiques, telles que l'ajout de filtres, de segments, de champs supplémentaires ou la modification de l'ordre de certains éléments dans le rapport, ne sont généralement pas recommandées à tous les utilisateurs. D'un autre côté, ces utilisateurs pourront également actualiser le rapport et utiliser les filtres ou slicers existants. Aspose.Cells for Python via .NET a fourni cette possibilité aux développeurs pour empêcher les utilisateurs de modifier ces rapports lors de leur création. À cette fin, Excel fournit une fonctionnalité permettant de désactiver le ruban du tableau croisé dynamique et la même chose est fournie par Aspose.Cells for Python via .NET, c'est-à-dire que le développeur peut désactiver le ruban qui contient des contrôles pour modifier ces rapports.

{{% /alert %}}

##  **Désactiver le ruban du tableau croisé dynamique à l'aide de PivotTable.EnableWizard**

 Le code suivant illustre cette fonctionnalité en accédant à un tableau croisé dynamique à partir d'une feuille, puis en définissant[**activer_wizard**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) à *faux**. Un exemple de fichier de tableau croisé dynamique peut être téléchargé à partir de ce site[lien](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
