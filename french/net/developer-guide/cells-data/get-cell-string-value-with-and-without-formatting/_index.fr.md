---
title: Obtenir la valeur de chaîne Cell avec et sans formatage
type: docs
weight: 240
url: /fr/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit une méthode[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) qui peut être utilisé pour obtenir la valeur de chaîne de la cellule avec ou sans formatage. Supposons que vous ayez une cellule avec la valeur 0,012345 et que vous l'ayez formatée pour n'afficher que deux décimales. Il s'affichera alors sous la forme 0,01 dans Excel. Vous pouvez récupérer des valeurs de chaîne à la fois 0,01 et 0,012345 à l'aide de la[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) méthode. Ça prend[**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)enum comme paramètre qui a les valeurs suivantes

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

 L'exemple de code suivant explique l'utilisation de[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
