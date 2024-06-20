---
title: Désactiver les rubans de tableau croisé dynamique
type: docs
weight: 40
url: /fr/java/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Les rapports basés sur les tables croisées dynamiques sont utiles mais sujets à erreur si les utilisateurs cibles n'ont pas de connaissance détaillée d'Excel pour configurer ces rapports. Dans ces circonstances, les organisations voudront restreindre les utilisateurs pour qu'ils ne puissent pas modifier un rapport basé sur une table croisée dynamique. Les fonctionnalités courantes des tables croisées dynamiques telles que l'ajout de filtres supplémentaires, de tranches, de champs, ou le changement de l'ordre de certaines choses dans le rapport ne sont généralement pas recommandées pour chaque utilisateur. En revanche, ces utilisateurs devraient également pouvoir actualiser le rapport et utiliser les filtres ou tranches existants. Aspose.Cells a fourni cette capacité aux développeurs pour restreindre les utilisateurs à modifier ces rapports tout en créant ces rapports. À cette fin, Excel fournit une fonctionnalité pour désactiver le ruban de la table croisée dynamique, et Aspose.Cells offre la même fonctionnalité, c'est-à-dire que le développeur peut désactiver le ruban contenant les commandes pour modifier ces rapports.

{{% /alert %}}

## **Désactiver le ruban de la table croisée dynamique en utilisant PivotTable.setEnableWizard**

Le code suivant démontre cette fonctionnalité en accédant à une table croisée dynamique à partir d'une feuille, puis en appelant la [**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) pour définir ce drapeau **false**. Le fichier de table croisée dynamique d'exemple peut être téléchargé depuis ce [lien](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
