---
title: Précisez si le tableau croisé dynamique est compatible avec Excel2003 lors de l actualisation du tableau croisé dynamique
type: docs
weight: 80
url: /fr/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells offre la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) que vous pouvez utiliser pour spécifier si le tableau croisé dynamique est compatible avec Excel 2003 lors du rafraîchissement du tableau croisé dynamique. Si true, une chaîne doit être inférieure ou égale à 255 caractères, donc si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si **false**, une chaîne n'aura pas la restriction mentionnée. La valeur par défaut est **true**.

{{% /alert %}}

## **Spécifiez si le PivotTable est compatible pour Excel2003 lors de l'actualisation du PivotTable**

Le code d'exemple suivant explique l'utilisation de la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible). La chaîne d'origine fait 383 caractères de long. Mais lorsque la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) est définie sur **vrai** et que le tableau croisé dynamique est actualisé, les données de la cellule B5 du tableau croisé dynamique sont tronquées et deviennent 255 caractères de long. Cependant, lorsque la propriété [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) est définie sur **faux** et que le tableau croisé dynamique est à nouveau actualisé, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
