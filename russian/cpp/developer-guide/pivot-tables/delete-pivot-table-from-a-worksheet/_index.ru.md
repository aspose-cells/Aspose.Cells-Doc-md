---
title: Удалить сводную таблицу из рабочего листа с помощью C++
linktitle: Удалить сводную таблицу
type: docs
weight: 60
url: /ru/cpp/delete-pivot-table-from-a-worksheet/
description: Код C++ для удаления сводной таблицы из листов Excel с помощью Aspose.Cells.
keywords: c++ удалить сводную таблицу из рабочего листа, c++ удалить сводную таблицу из Excel, как удалить сводную таблицу с помощью c++, удалить сводную таблицу с помощью c++, удалить сводную таблицу из Excel с помощью c++, c++ удалить сводную таблицу, c++ убрать сводную таблицу, убрать сводную таблицу, удалить сводную таблицу, как удалить сводную таблицу
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет функцию удаления сводной таблицы из листа. Вы можете удалить сводную таблицу, используя объект сводной таблицы или позицию сводной таблицы. Пожалуйста, используйте метод [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/) для удаления сводной таблицы с использованием объекта сводной таблицы, и метод [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) для удаления объекта сводной таблицы, используя его позицию в коллекции сводных таблиц.

{{% /alert %}}

Следующий пример кода удаляет две сводные таблицы из рабочего листа. Сначала он удаляет сводную таблицу с помощью метода [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/remove/), затем — с помощью метода [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/).

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table object
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Remove pivot table using pivot table object
    worksheet.GetPivotTables().Remove(pivotTable);

    // OR you can remove pivot table using pivot table position by uncommenting below line
    // worksheet.GetPivotTables().RemoveAt(0);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Pivot table removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
