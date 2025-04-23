---
title: Désactiver les rubans de tableau croisé dynamique
type: docs
weight: 90
url: /fr/nodejs-cpp/disable-pivot-table-ribbons/
description: Comment désactiver les rubans du tableau croisé dynamique avec Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells pour Node.js Excel, bibliothèque Excel Node.js, désactiver les rubans du tableau croisé dynamique en utilisant la bibliothèque Excel Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Les rapports basés sur des tableaux croisés dynamiques sont utiles mais susceptibles d'erreur si les utilisateurs cibles n'ont pas une connaissance approfondie d'Excel pour configurer ces rapports. Dans ces cas, les organisations voudront restreindre les utilisateurs pour qu'ils ne puissent pas modifier ces rapports de tableau croisé dynamique. Les fonctionnalités courantes comme l'ajout de filtres supplémentaires, de trancheurs, de champs, ou le changement de l'ordre de certains éléments dans le rapport ne sont pas recommandées pour tous les utilisateurs. En revanche, ces utilisateurs doivent pouvoir actualiser le rapport et utiliser les filtres ou trancheurs existants. Aspose.Cells for Node.js via C++ fournit cette capacité aux développeurs pour limiter les modifications de ces rapports lors de leur création. Pour cela, Excel offre une fonction pour désactiver le ruban du tableau croisé dynamique et cela est également fourni par Aspose.Cells for Node.js via C++, c'est-à-dire que le développeur peut désactiver le ruban contenant les contrôles pour modifier ces rapports.

{{% /alert %}}

## **Comment désactiver le ruban du tableau croisé dynamique en utilisant Aspose.Cells for Node.js via C++**

Le code suivant démontre cette fonctionnalité en accédant à un tableau croisé dynamique à partir d'une feuille, puis en définissant [**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-) sur **false**. Le fichier de tableau croisé dynamique d'exemple peut être téléchargé à partir de ce [lien](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
