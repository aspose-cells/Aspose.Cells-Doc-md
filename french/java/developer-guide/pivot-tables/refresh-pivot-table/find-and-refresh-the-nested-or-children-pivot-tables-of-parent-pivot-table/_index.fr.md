---
title: Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent
type: docs
weight: 50
url: /fr/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **Scénarios d'utilisation possibles**

Parfois, un tableau croisé dynamique utilise un autre tableau croisé dynamique en tant que source de données, on l'appelle un tableau croisé dynamique enfant ou un tableau croisé dynamique imbriqué. Vous pouvez trouver les tableaux croisés dynamiques enfants d'un tableau croisé dynamique parent en utilisant la méthode [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--).

## **Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767766.xlsx) qui contient trois tableaux croisés dynamiques. Les deux tableaux croisés dynamiques du bas sont les enfants du tableau croisé dynamique ci-dessus, comme le montre cette capture d'écran. Le code trouve les tableaux croisés dynamiques enfants en utilisant la méthode [**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--) puis les rafraîchit un par un.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
{{< app/cells/assistant language="java" >}}
