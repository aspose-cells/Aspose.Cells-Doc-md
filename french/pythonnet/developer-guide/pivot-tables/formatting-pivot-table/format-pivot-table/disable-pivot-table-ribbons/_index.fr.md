---
title: Désactiver les rubans de tableau croisé dynamique
type: docs
weight: 90
url: /fr/python-net/disable-pivot-table-ribbons/
description: Comment désactiver les rubans de tableau croisé dynamique avec Aspose.Cells pour Python via .NET
keywords: Aspose.Cells pour Python Excel, bibliothèque Python Excel, Désactiver les rubans de tableau croisé dynamique en utilisant la bibliothèque Aspose.Cells pour Python Excel
---

{{% alert color="primary" %}}

Les rapports basés sur les tableaux croisés dynamiques sont utiles mais sujets à des erreurs si les utilisateurs cibles n'ont pas une connaissance détaillée d'Excel pour configurer ces rapports. Dans ces circonstances, les organisations voudront restreindre les utilisateurs de pouvoir modifier un rapport basé sur un tableau croisé dynamique. Des fonctionnalités courantes des tableaux croisés dynamiques comme ajouter des filtres supplémentaires, des trancheurs, des champs, ou changer l'ordre de certaines choses dans le rapport ne sont pas recommandées pour chaque utilisateur. D'un autre côté, ces utilisateurs doivent également pouvoir actualiser le rapport et utiliser des filtres ou des trancheurs existants. Aspose.Cells pour Python via .NET a fourni cette capacité aux développeurs pour restreindre les utilisateurs à changer ces rapports tout en créant ces rapports. À cet effet, Excel fournit une fonctionnalité pour désactiver le ruban de tableau croisé dynamique et la même fonctionnalité est fournie par Aspose.Cells pour Python via .NET, c'est-à-dire que le développeur peut désactiver le ruban qui contient des commandes pour modifier ces rapports.

{{% /alert %}}

## **Comment désactiver le ruban de tableau croisé dynamique en utilisant la bibliothèque Aspose.Cells pour Python Excel**

Le code suivant démontre cette fonctionnalité en accédant à un tableau croisé dynamique à partir d'une feuille, puis en définissant [**enable_wizard**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) sur **false**. Le fichier de tableau croisé dynamique d'exemple peut être téléchargé à partir de ce [lien](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
{{< app/cells/assistant language="python-net" >}}
