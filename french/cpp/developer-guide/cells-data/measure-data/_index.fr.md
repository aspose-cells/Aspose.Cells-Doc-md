---
title: Mesurer la largeur et la hauteur de la valeur de la cellule en unités de pixels avec C++
linktitle: Mesurer la taille.
type: docs
weight: 260
url: /fr/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Apprenez comment mesurer la largeur et la hauteur de la valeur de la cellule en unités de pixels via l’API Aspose.Cells for C++.
keywords: Mesurez la largeur de la valeur de la cellule en unité de pixels, mesurez la hauteur de la valeur de la cellule en unité de pixels, obtenez la largeur de la valeur de la cellule en unité de pixels, obtenez la hauteur de la valeur de la cellule en unité de pixels
---

{{% alert color="primary" %}}

Parfois, vous devez calculer la largeur et la hauteur de la valeur de la cellule pour adapter la valeur de la cellule à l'intérieur de la cellule. Aspose.Cells fournit des méthodes [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) et [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) à cet effet. En utilisant ces méthodes, vous pouvez calculer la largeur et la hauteur de la valeur de la cellule, puis définir respectivement la largeur de la colonne et la hauteur de la ligne de cette cellule, ce qui ajustera ou adaptera la valeur de la cellule à l'intérieur de la cellule.

 Alternativement, vous pouvez également [ajuster automatiquement les lignes et colonnes de votre cellule ou plage de cellules](/cells/fr/cpp/autofit-rows-and-columns/) en utilisant les API Aspose.Cells.

{{% /alert %}}

Le code suivant explique l'utilisation des méthodes [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) et [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell B2 and add some value inside it
    Cell cell = worksheet.GetCells().Get(u"B2");
    cell.PutValue(u"Welcome to Aspose!");

    // Enlarge its font to size 16
    Style style = cell.GetStyle();
    style.GetFont().SetSize(16);
    cell.SetStyle(style);

    // Calculate the width and height of the cell value in unit of pixels
    int32_t widthOfValue = cell.GetWidthOfValue();
    int32_t heightOfValue = cell.GetHeightOfValue();

    // Print both values
    std::wcout << u"Width of Cell Value: " << widthOfValue << std::endl;
    std::wcout << u"Height of Cell Value: " << heightOfValue << std::endl;

    // Set the row height and column width to adjust/fit the cell value inside cell
    worksheet.GetCells().SetColumnWidthPixel(1, widthOfValue);
    worksheet.GetCells().SetRowHeightPixel(1, heightOfValue);

    // Save the output excel file
    U16String outFilePath = u"output_out.xlsx";
    workbook.Save(outFilePath);

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Obtenir la largeur de texte de la valeur de la cellule](/cells/fr/cpp/get-text-width-of-cell-value/)
