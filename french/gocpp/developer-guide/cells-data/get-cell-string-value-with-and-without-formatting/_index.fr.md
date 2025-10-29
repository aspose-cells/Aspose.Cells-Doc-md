---
title: Obtenir la valeur en chaîne de la cellule avec ou sans mise en forme avec Golang via C++
linktitle: Obtenir la valeur de la chaîne de la cellule
type: docs
weight: 240
url: /fr/go-cpp/get-cell-string-value-with-and-without-formatting/
description: Apprenez comment obtenir la valeur de la chaîne de la cellule avec ou sans formatage via l’API Aspose.Cells for C++.
keywords: Obtenir la valeur de la chaîne de la cellule avec et sans mise en forme, récupérer la valeur de la chaîne de la cellule avec et sans mise en forme, obtenir la valeur de la chaîne de la cellule avec et sans mise en forme
---

{{% alert color="primary" %}}

Aspose.Cells fournit une méthode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) qui peut être utilisée pour obtenir la valeur string de la cellule avec ou sans formatage. Supposons que vous ayez une cellule avec la valeur 0.012345 et que vous l’ayez formatée pour afficher seulement deux décimales. Elle s’affichera alors comme 0,01 dans Excel. Vous pouvez récupérer des valeurs de chaîne à la fois sous forme de 0,01 et de 0,012345 en utilisant la méthode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/). Elle prend en paramètre l’énumération [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) qui a les valeurs suivantes :

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la méthode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
