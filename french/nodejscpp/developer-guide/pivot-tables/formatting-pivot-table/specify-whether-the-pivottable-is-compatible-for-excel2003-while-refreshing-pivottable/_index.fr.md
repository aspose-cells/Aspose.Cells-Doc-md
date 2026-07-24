---
title: Précisez si le tableau croisé dynamique est compatible avec Excel2003 lors de l actualisation du tableau croisé dynamique
type: docs
weight: 80
url: /fr/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ fournit la propriété [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) que vous pouvez utiliser pour spécifier si la PivotTable est compatible avec Excel 2003 lors de la mise à jour. Si vrai, une chaîne doit faire moins de 255 caractères, sinon elle sera tronquée. Si **faux**, il n’y a pas cette restriction. La valeur par défaut est **true**.

{{% /alert %}}

## **Spécifiez si le PivotTable est compatible pour Excel2003 lors de l'actualisation du PivotTable**

Le code d'exemple suivant explique l'utilisation de la propriété [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-). La chaîne d'origine fait 383 caractères de long. Mais lorsque la propriété [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) est définie sur **vrai** et que le tableau croisé dynamique est actualisé, les données de la cellule B5 du tableau croisé dynamique sont tronquées et deviennent 255 caractères de long. Cependant, lorsque la propriété [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) est définie sur **faux** et que le tableau croisé dynamique est à nouveau actualisé, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
