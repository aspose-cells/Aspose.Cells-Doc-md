---
title: Измерение ширины и высоты значения ячейки в пикселях с помощью C++
linktitle: Измерьте размер
type: docs
weight: 260
url: /ru/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Узнайте, как измерить ширину и высоту значения ячейки в пикселях через API Aspose.Cells for C++.
keywords: Измерьте ширину значения ячейки в пикселях, измерьте высоту значения ячейки в пикселях, получите ширину значения ячейки в пикселях, получите высоту значения ячейки в пикселях
---

{{% alert color="primary" %}}

Иногда вам нужно рассчитать ширину и высоту значения ячейки, чтобы поместить значение внутри ячейки. Aspose.Cells предоставляет [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) и [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) методы для этой цели. Используя эти методы, вы можете рассчитать ширину и высоту значения ячейки, а затем установить ширину столбца и высоту строки этой ячейки соответственно, и это позволит автоматически масштабировать или вписать значение ячейки внутри ячейки.

Альтернативно, вы также можете [автоматически подстроить высоту строк и ширину столбцов вашего диапазона ячеек](/cells/ru/cpp/autofit-rows-and-columns/) с помощью API Aspose.Cells.

{{% /alert %}}

Следующий код объясняет использование методов [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) и [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/)

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

## **Продвинутые темы**
- [Получить ширину текста значения ячейки](/cells/ru/cpp/get-text-width-of-cell-value/)
{{< app/cells/assistant language="cpp" >}}
