---
title: Désactivez les rubans de tableau croisé dynamique avec Golang via C++
linktitle: Désactiver les rubans de tableau croisé dynamique
type: docs
weight: 90
url: /fr/go-cpp/disable-pivot-table-ribbons/
description: Apprenez comment désactiver les rubans du tableau croisé dynamique dans les fichiers Excel en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Les rapports basés sur des tableaux croisés dynamiques sont utiles mais sujet à erreur si les utilisateurs cibles ne possèdent pas une connaissance approfondie d'Excel pour configurer ces rapports. Dans ces cas, les organisations voudront restreindre la possibilité pour les utilisateurs de modifier ces rapports. Les fonctionnalités courantes du tableau croisé dynamique, telles que l'ajout de filtres supplémentaires, de trancheurs, de champs ou la modification de l'ordre de certains éléments du rapport, ne sont généralement pas recommandées pour tous les utilisateurs. En revanche, ces utilisateurs doivent aussi pouvoir actualiser le rapport et utiliser les filtres ou trancheurs existants. Aspose.Cells a permis aux développeurs cette capacité pour restreindre la modification de ces rapports lors de leur création. À cette fin, Excel offre une fonctionnalité pour désactiver le ruban du tableau croisé dynamique, et cette fonctionnalité est aussi fournie par Aspose.Cells. Les développeurs peuvent désactiver le ruban qui contient les contrôles pour modifier ces rapports.

{{% /alert %}}

## **Désactiver le ruban du tableau croisé dynamique à l'aide de PivotTable.EnableWizard**

Le code suivant illustre cette fonctionnalité en accédant à un tableau croisé dynamique depuis une feuille, puis en définissant [**GetEnableWizard()**](https://reference.aspose.com/cells/go-cpp/pivottable/getenablewizard/) sur **false**. Un fichier de tableau croisé dynamique d'exemple peut être téléchargé via ce [lien](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisablePivotTableRibbons.go" >}}
