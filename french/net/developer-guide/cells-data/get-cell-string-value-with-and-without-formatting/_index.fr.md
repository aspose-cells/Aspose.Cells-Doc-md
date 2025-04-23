---
title: Obtenir la valeur de la chaîne de la cellule avec et sans mise en forme
type: docs
weight: 240
url: /fr/net/get-cell-string-value-with-and-without-formatting/
description: Apprenez à obtenir la valeur de la chaîne de la cellule avec et sans mise en forme via l API Aspose.Cells for .NET.
keywords: Obtenir la valeur de la chaîne de la cellule avec et sans mise en forme, récupérer la valeur de la chaîne de la cellule avec et sans mise en forme, obtenir la valeur de la chaîne de la cellule avec et sans mise en forme
---

{{% alert color="primary" %}}

Aspose.Cells fournit une méthode [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue) qui peut être utilisée pour obtenir la valeur de la chaîne de la cellule avec ou sans mise en forme. Supposez que vous ayez une cellule avec la valeur 0.012345 et que vous l'ayez formatée pour afficher uniquement deux décimales. Elle s'affichera alors comme 0.01 dans Excel. Vous pouvez récupérer les valeurs de chaîne à la fois comme 0.01 et comme 0.012345 en utilisant la méthode [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue). Elle prend en paramètre l'énumération [**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/) qui a les valeurs suivantes.

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la méthode [**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
{{< app/cells/assistant language="csharp" >}}
