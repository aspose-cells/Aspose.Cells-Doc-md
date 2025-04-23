---
title: Копировать высоту строк исходного диапазона в целевой диапазон с помощью C++
linktitle: Копировать высоту строк исходного диапазона в целевой диапазон
type: docs
weight: 590
url: /ru/cpp/copy-row-heights-of-source-range-to-destination-range/
description: Узнайте, как копировать высоту строк из исходного диапазона в целевой с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 Иногда пользователи нуждаются в копировании высоты строк из исходного диапазона в целевой. Aspose.Cells предлагает перечисление [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) для этой задачи. Когда вы установите свойство [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) с этим перечислением [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/), высоты всех строк внутри исходного диапазона будут скопированы в целевой диапазон.

{{% /alert %}}

 Следующий пример кода объясняет, как использовать перечисление [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) для копирования высот строк из исходного диапазона в целевой. После открытия полученного файла Excel в Microsoft Excel, вы увидите, что высоты строк целевого диапазона точно такие же, как и у исходного.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
