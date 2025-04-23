---
title: Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent
type: docs
weight: 60
url: /fr/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Comment trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent avec Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells pour Node.js Excel, bibliothèque Excel Node.js, Trouver et Actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent en utilisant Aspose.Cells pour la bibliothèque Excel Node.js.
---

## **Scénarios d'utilisation possibles**

Parfois, un tableau croisé dynamique utilise un autre tableau croisé dynamique en tant que source de données, on l'appelle un tableau croisé dynamique enfant ou un tableau croisé dynamique imbriqué. Vous pouvez trouver les tableaux croisés dynamiques enfants d'un tableau croisé dynamique parent en utilisant la méthode [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--).

## **Comment trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767747.xlsx) qui contient trois tableaux croisés dynamiques. Les deux tableaux croisés dynamiques inférieurs sont les enfants du tableau croisé dynamique ci-dessus comme indiqué dans cette capture d'écran. Le code trouve les tableaux croisés dynamiques enfants en utilisant la méthode [**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--) et les actualise un par un.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
