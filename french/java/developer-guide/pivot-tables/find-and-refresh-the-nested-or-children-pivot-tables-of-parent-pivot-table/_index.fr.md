---
title: Rechercher et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent
type: docs
weight: 50
url: /fr/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **Scénarios d'utilisation possibles**

Parfois, un tableau croisé dynamique utilise un autre tableau croisé dynamique comme source de données, il est donc appelé tableau croisé dynamique enfant ou tableau croisé dynamique imbriqué. Vous pouvez trouver les tableaux croisés dynamiques enfants d'un tableau croisé dynamique parent à l'aide de la[**Tableau croisé dynamique.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) méthode.

## **Rechercher et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent**

L'exemple de code suivant charge le[exemple de fichier Excel](61767766.xlsx)qui contient trois tableaux croisés dynamiques. Les deux tableaux croisés dynamiques du bas sont les enfants du tableau croisé dynamique ci-dessus, comme illustré dans cette capture d'écran. Le code trouve le tableau croisé dynamique des enfants à l'aide de la[**Tableau croisé dynamique.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) puis les actualise un par un.

![tâche : image_autre_texte](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
