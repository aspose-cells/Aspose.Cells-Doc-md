---
title: Rechercher et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent
type: docs
weight: 60
url: /fr/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Comment rechercher et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent avec Aspose.Cells for Python via .NET.
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **Scénarios d'utilisation possibles**

Parfois, un tableau croisé dynamique utilise un autre tableau croisé dynamique comme source de données, on l'appelle donc tableau croisé dynamique enfant ou tableau croisé dynamique imbriqué. Vous pouvez trouver les tableaux croisés dynamiques enfants d'un tableau croisé dynamique parent en utilisant le[**Tableau croisé dynamique.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)méthode.

##  **Rechercher et actualiser les tableaux croisés dynamiques imbriqués ou enfants du tableau croisé dynamique parent**

 L'exemple de code suivant charge le[exemple de fichier Excel](61767747.xlsx) qui contient trois tableaux croisés dynamiques. Les deux tableaux croisés dynamiques du bas sont les enfants du tableau croisé dynamique ci-dessus, comme indiqué dans cette capture d'écran. Le code trouve le tableau croisé dynamique des enfants en utilisant le[**Tableau croisé dynamique.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)méthode, puis les actualise un par un.

![tâche : image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
