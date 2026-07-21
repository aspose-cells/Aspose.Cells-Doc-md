---
title: Recherchez et actualisez les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent avec Golang via C++
linktitle: Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants
type: docs
weight: 60
url: /fr/go-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Apprenez comment trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants d’un tableau croisé dynamique parent en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, un tableau croisé dynamique utilise un autre tableau croisé dynamique en tant que source de données, on l'appelle un tableau croisé dynamique enfant ou un tableau croisé dynamique imbriqué. Vous pouvez trouver les tableaux croisés dynamiques enfants d'un tableau croisé dynamique parent en utilisant la méthode [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/).

## **Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767747.xlsx) qui contient trois tableaux croisés dynamiques. Les deux tableaux croisés dynamiques inférieurs sont les enfants du tableau croisé dynamique ci-dessus comme indiqué dans cette capture d'écran. Le code trouve les tableaux croisés dynamiques enfants en utilisant la méthode [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/go-cpp/pivottable/getchildren/) et les actualise un par un.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindAndRefreshTheNestedOrChildrenPivotTablesOfParentPivotTable.go" >}}
