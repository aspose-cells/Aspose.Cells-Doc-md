---
title: How to Use Color Palette with C++
linktitle: How to Use Color Palette
type: docs
weight: 80
url: /cpp/excel-color-palette/
description: C++ code to add custom colors to the palette and use Excel color palette with Aspose.Cells for C++ API.
keywords: c++ add custom colors to the palette, c++ programmatically excel color palette, programmatically how to use color palette in workbook, c++ how to use color palette in excel
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Colors and Palette**

A palette is the set of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97‑2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills, and lines in a chart.

With Aspose.Cells it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.

This topic discusses how to add custom colors to the palette.

## **Add Custom Colors to Palette**

Aspose.Cells supports Microsoft Excel's 56‑color palette. To use a custom color that is not defined in the palette, add the color to the palette.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class provides a [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) method that takes the following parameters to modify the palette:

- **Custom color** – the custom color to be added.  
- **Index** – the index of the color in the palette that the custom color will replace. The index should be between 0 and 55.

The example below adds a custom color (Orchid) to the palette before applying it to a font.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid is now in the palette
    std::cout << "Is Orchid in palette now? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

The palette holds only 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file that was formatted with the previous color is also changed. Therefore, when you modify the palette, please be very careful. Moreover, this limitation applies only to the XLS (Excel 97‑2003) file format, as there is no such limitation for XLSX or other advanced Microsoft Excel (2007, 2010, or 2013) file formats.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
