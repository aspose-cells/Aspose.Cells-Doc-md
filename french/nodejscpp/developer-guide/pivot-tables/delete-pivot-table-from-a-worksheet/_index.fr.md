---
title: Supprimer le tableau croisé dynamique d une feuille de calcul
type: docs
weight: 60
url: /fr/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Code Aspose.Cells for Node.js via C++ pour supprimer un tableau croisé dynamique pour les feuilles Excel
keywords: Aspose.Cells for Node.js via C++ Excel, bibliothèque Excel Node.js, supprimer un tableau croisé dynamique d une feuille de calcul, supprimer un tableau croisé dynamique d Excel, comment supprimer un tableau croisé dynamique avec Aspose.Cells for Node.js via C++, supprimer un pivot, supprimer un tableau croisé dynamique d Excel, supprimer un tableau croisé dynamique, Aspose.Cells for Node.js via C++ supprimer tableau croisé dynamique, supprimer tableau croisé dynamique, supprimer un tableau croisé dynamique, comment supprimer un tableau croisé dynamique
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ offre une fonctionnalité pour supprimer ou retirer un tableau croisé dynamique d'une feuille de calcul. Vous pouvez supprimer le tableau croisé dynamique en utilisant l'objet tableau croisé dynamique ou sa position. Veuillez utiliser la méthode [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) pour supprimer le tableau croisé dynamique en utilisant l'objet tableau croisé dynamique et la méthode [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) pour supprimer l'objet tableau croisé dynamique en utilisant sa position dans la collection.

{{% /alert %}}

## **Comment supprimer un tableau croisé dynamique d'une feuille de calcul en utilisant Aspose.Cells for Node.js via C++**

Le code d'exemple suivant supprime deux tableaux croisés dynamiques de la feuille de calcul. D'abord, il supprime un tableau croisé dynamique en utilisant la méthode [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) et ensuite il supprime un tableau croisé dynamique en utilisant la méthode [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
