---
title: Поиск и замена данных в диапазоне с C++
linktitle: Поиск и замена данных в диапазоне
type: docs
weight: 170
url: /ru/cpp/search-and-replace-data-in-a-range/
description: Данная статья показывает, как искать и заменять данные в диапазоне в Excel с помощью C++ кода.
keywords: поиск и замена данных в Excel с помощью C++, поиск данных в Excel с C++, поиск и замена данных в диапазоне с C++, поиск данных в диапазоне, поиск данных в диапазоне с помощью C++, поиски данных в диапазоне, поиск данных в Excel, поиск данных в диапазоне, поиск и замена данных в Excel с помощью C++, поиск и замена данных в диапазоне с помощью C++, поиск и замена данных в диапазоне с C++
---

{{% alert color="primary" %}}

Иногда необходимо искать и заменять конкретные данные в диапазоне, игнорируя значения ячеек за пределами этого диапазона. Aspose.Cells позволяет ограничить поиск конкретным диапазоном. В этой статье объясняется, как это сделать.

{{% /alert %}}

Aspose.Cells предоставляет метод [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/) для указания диапазона при поиске данных. Пример кода ниже демонстрирует, как искать и заменять данные в диапазоне.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"input.xlsx";

    // Create workbook
    Workbook workbook(filePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Specify the range where you want to search
    // Here the range is E9:H15
    CellArea area = CellArea::CreateCellArea(u"E9", u"H15");

    // Specify Find options
    FindOptions opts;
    opts.SetLookInType(LookInType::Values);
    opts.SetLookAtType(LookAtType::EntireContent);
    opts.SetRange(area);

    Cell cell;
    do
    {
        // Search the cell with value search within range
        cell = worksheet.GetCells().Find(u"search", cell, opts);

        // If no such cell found, then break the loop
        if (!cell)
            break;

        // Replace the cell with value replace
        cell.PutValue(u"replace");

    } while (true);

    // Save the workbook
    U16String outputPath = srcDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
