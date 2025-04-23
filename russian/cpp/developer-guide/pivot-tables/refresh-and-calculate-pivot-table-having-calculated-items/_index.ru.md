---
title: Обновление и вычисление сводной таблицы с рассчитанными элементами с помощью C++
linktitle: Обновление и вычисление сводной таблицы с вычисляемыми элементами
type: docs
weight: 40
url: /ru/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Обновить и вычислить сводную таблицу с рассчитанными элементами с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells теперь поддерживает обновление и вычисление сводной таблицы с использованием вычислимых элементов. Пожалуйста, используйте [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) и [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) как обычно, чтобы выполнить эту функцию.

{{% /alert %}}

## **Обновление и вычисление сводной таблицы с вычисляемыми элементами**

Следующий пример кода загружает [исходный файл Excel](5115238.xlsx), содержащий сводную таблицу с тремя рассчитанными элементами, такими как "add", "div", "div2". Сначала мы изменяем значение ячейки D2 на 20, затем обновляем и пересчитываем сводную таблицу с помощью API Aspose.Cells и сохраняем рабочую книгу в формате PDF. Результаты в [выходном PDF](5115229.pdf) показывают, что Aspose.Cells успешно обновил и пересчитал сводную таблицу с рассчитанными элементами. Вы можете проверить это вручную, установив значение 20 в ячейке D2 в Excel и обновив сводную таблицу с помощью сочетания клавиш Alt+F5 или кнопки обновления сводной таблицы.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
