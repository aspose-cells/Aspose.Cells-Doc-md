---
title: Formatter les cellules du tableau croisé dynamique
type: docs
weight: 30
url: /fr/nodejs-cpp/format-pivot-table-cells/
description: Comment formater les cellules du tableau croisé dynamique avec Aspose.Cells for Node.js via C++.
keywords: Formater les cellules du tableau croisé dynamique
---

{{% alert color="primary" %}}

Parfois, vous souhaitez formater les cellules du tableau croisé dynamique. Par exemple, vous souhaitez appliquer une couleur de fond aux cellules du tableau croisé dynamique. Aspose.Cells for Node.js via C++ offre deux méthodes [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) et [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-), que vous pouvez utiliser à cette fin.

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) applique le style à l'ensemble du tableau croisé dynamique tandis que [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) applique le style à une seule cellule du tableau croisé dynamique.

{{% /alert %}}
Le code d'exemple suivant charge le [fichier Excel d'exemple](pivot_format.xlsx) contenant deux tableaux croisés dynamiques, et réalise l'opération de mise en forme de l'ensemble du tableau croisé dynamique et de mise en forme des cellules individuelles dans le tableau croisé dynamique.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormatPivotTableCells-1.js" >}}

## Articles Connexes

- [Formatage du tableau croisé dynamique](/cells/fr/nodejs-cpp/formatting-pivot-table/)
- [Travailler avec les formats d'affichage des données de DataField dans le tableau croisé dynamique](/cells/fr/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
