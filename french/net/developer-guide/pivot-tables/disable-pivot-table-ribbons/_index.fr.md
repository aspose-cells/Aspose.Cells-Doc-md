---
title: Désactiver les rubans de tableau croisé dynamique
type: docs
weight: 90
url: /fr/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Les rapports basés sur les tables croisées dynamiques sont utiles mais sujets à erreur si les utilisateurs cibles n'ont pas de connaissance détaillée d'Excel pour configurer ces rapports. Dans ces circonstances, les organisations voudront restreindre les utilisateurs pour qu'ils ne puissent pas modifier un rapport basé sur une table croisée dynamique. Les fonctionnalités courantes des tables croisées dynamiques telles que l'ajout de filtres supplémentaires, de tranches, de champs, ou le changement de l'ordre de certaines choses dans le rapport ne sont généralement pas recommandées pour chaque utilisateur. En revanche, ces utilisateurs devraient également pouvoir actualiser le rapport et utiliser les filtres ou tranches existants. Aspose.Cells a fourni cette capacité aux développeurs pour restreindre les utilisateurs à modifier ces rapports tout en créant ces rapports. À cette fin, Excel fournit une fonctionnalité pour désactiver le ruban de la table croisée dynamique, et Aspose.Cells offre la même fonctionnalité, c'est-à-dire que le développeur peut désactiver le ruban contenant les commandes pour modifier ces rapports.

{{% /alert %}}

## **Désactiver le ruban du tableau croisé dynamique à l'aide de PivotTable.EnableWizard**

Le code suivant démontre cette fonctionnalité en accédant à un tableau croisé dynamique à partir d'une feuille, puis en définissant [**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) sur **false**. Le fichier de tableau croisé dynamique d'exemple peut être téléchargé à partir de ce [lien](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
