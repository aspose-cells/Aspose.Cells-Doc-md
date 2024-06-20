---
title: Trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent
type: docs
weight: 60
url: /fr/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Comment trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent avec Aspose.Cells pour Python via .NET
keywords: Aspose.Cells pour Python Excel, bibliothèque Python Excel, Trouver et Actualiser les Tableaux Croisés Dynamiques Imbriqués ou Enfants du Tableau Croisé Dynamique Parent en Utilisant la Bibliothèque Aspose.Cells pour Python Excel
---

## **Scénarios d'utilisation possibles**

Parfois, un tableau croisé dynamique utilise un autre tableau croisé dynamique en tant que source de données, on l'appelle un tableau croisé dynamique enfant ou un tableau croisé dynamique imbriqué. Vous pouvez trouver les tableaux croisés dynamiques enfants d'un tableau croisé dynamique parent en utilisant la méthode [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#).

## **Comment trouver et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent**

Le code d'exemple suivant charge le [fichier Excel d'exemple](61767747.xlsx) qui contient trois tableaux croisés dynamiques. Les deux tableaux croisés dynamiques inférieurs sont les enfants du tableau croisé dynamique ci-dessus comme indiqué dans cette capture d'écran. Le code trouve les tableaux croisés dynamiques enfants en utilisant la méthode [**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#) et les actualise un par un.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
