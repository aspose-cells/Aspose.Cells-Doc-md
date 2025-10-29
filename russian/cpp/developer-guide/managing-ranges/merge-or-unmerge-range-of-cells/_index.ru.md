---
title: Объединение или разъединение диапазона ячеек с C++
linktitle: Объединение или разъединение диапазона ячеек
type: docs
weight: 190
url: /ru/cpp/merge-or-unmerge-range-of-cells/
description: Объединение и разъединение ячеек в диапазоне в Excel с помощью C++ кода.
keywords: объединение и разъединение ячеек в диапазоне с помощью C++, объединение и разъединение ячеек в диапазоне с помощью C++, объединение и разъединение ячеек в диапазоне с C++, объединение и разъединение ячеек в диапазоне с помощью C++, объединение и разъединение ячеек в Excel с C++, объединение ячеек в Excel с C++, разъединение ячеек в Excel с C++, объединение ячеек в диапазоне с помощью C++
---

{{% alert color="primary" %}}

Вы можете использовать Aspose.Cells для объединения или разделения диапазона ячеек. Aspose.Cells предоставляет методы [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) и [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) для этой цели. В этой статье объясняется, как объединить диапазон ячеек в одну ячейку.

{{% /alert %}}

## **Пример**

Следующий пример кода сначала создает диапазон - A1:D4 - затем объединяет ячейки в диапазоне в одну с помощью метода [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/). Аналогично, можно разбить ячейки, создав диапазон и вызвав метод [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of output excel file
    U16String outputPath = srcDir + u"output.out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range
    Range range = worksheet.GetCells().CreateRange(u"A1:D4");

    // Merge range into a single cell
    range.Merge();

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
