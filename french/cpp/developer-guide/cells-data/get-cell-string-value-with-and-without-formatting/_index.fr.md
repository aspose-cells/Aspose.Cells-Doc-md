---
title: Obtenir la valeur sous forme de chaîne de la cellule avec ou sans formatage avec C++
linktitle: Obtenir la valeur de la chaîne de la cellule
type: docs
weight: 240
url: /fr/cpp/get-cell-string-value-with-and-without-formatting/
description: Apprenez comment obtenir la valeur de la chaîne de la cellule avec ou sans formatage via l’API Aspose.Cells for C++.
keywords: Obtenir la valeur de la chaîne de la cellule avec et sans mise en forme, récupérer la valeur de la chaîne de la cellule avec et sans mise en forme, obtenir la valeur de la chaîne de la cellule avec et sans mise en forme
---

{{% alert color="primary" %}}

Aspose.Cells fournit une méthode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/) qui peut être utilisée pour obtenir la valeur string de la cellule avec ou sans formatage. Supposons que vous ayez une cellule avec la valeur 0.012345 et que vous l’ayez formatée pour afficher seulement deux décimales. Elle s’affichera alors comme 0,01 dans Excel. Vous pouvez récupérer des valeurs de chaîne à la fois sous forme de 0,01 et de 0,012345 en utilisant la méthode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/). Elle prend en paramètre l’énumération [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) qui a les valeurs suivantes :

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

Le code d'exemple suivant explique l'utilisation de la méthode [**Cell::GetStringValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put value inside the cell
    cell.PutValue(0.012345);

    // Format the cell to display 0.01 instead of 0.012345
    Style style = cell.GetStyle();
    style.SetNumber(2);
    cell.SetStyle(style);

    // Get string value as Cell Style
    U16String value = cell.GetStringValue(CellValueFormatStrategy::CellStyle);
    std::cout << value.ToUtf8() << std::endl;

    // Get string value without any formatting
    value = cell.GetStringValue(CellValueFormatStrategy::None);
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
