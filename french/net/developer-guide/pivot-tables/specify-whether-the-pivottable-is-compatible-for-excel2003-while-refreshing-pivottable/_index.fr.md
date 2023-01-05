---
title: Spécifiez si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique
type: docs
weight: 80
url: /fr/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit le[**Tableau croisé dynamique.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)propriété que vous pouvez utiliser pour spécifier si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique. Si vrai, une chaîne doit être inférieure ou égale à 255 caractères, donc si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si**faux** , une chaîne n'aura pas la restriction susmentionnée. La valeur par défaut est**vrai**.

{{% /alert %}}

## **Spécifiez si le tableau croisé dynamique est compatible avec Excel2003 lors de l'actualisation du tableau croisé dynamique**

 L'exemple de code suivant explique l'utilisation de[**Tableau croisé dynamique.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) la propriété. La chaîne d'origine comporte 383 caractères. Mais quand[**Tableau croisé dynamique.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) la propriété est définie**vrai** et que le tableau croisé dynamique est rafraîchi, les données de la cellule B5 du tableau croisé dynamique sont tronquées et deviennent 255 caractères. Cependant, lorsque[**Tableau croisé dynamique.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) la propriété est définie**faux** et que le tableau croisé dynamique est à nouveau rafraîchi, les données de la cellule B5 du tableau croisé dynamique ne sont pas tronquées et restent longues de 383 caractères. Veuillez lire les commentaires à l'intérieur du code pour une meilleure compréhension de cette propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
