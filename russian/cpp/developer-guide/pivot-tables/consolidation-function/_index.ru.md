---
title: Функция консолидации с C++
linktitle: Функция консолидации
type: docs
weight: 20
url: /ru/cpp/consolidation-function/
description: Узнайте, как применить функцию консолидации к полям данных сводной таблицы с помощью Aspose.Cells и C++.
---

## **Функция консолидации**

Aspose.Cells можно использовать для применения функции объединения к полям данных (или значениям) сводной таблицы. В Microsoft Excel вы можете щелкнуть правой кнопкой мыши на поле значения, затем выбрать опцию **Настройки поля значения...**, а затем выбрать вкладку **Сводные значения по**. Оттуда вы можете выбрать любую функцию объединения по своему выбору, такую как Сумма, Количество, Среднее, Максимум, Минимум, Произведение, Уникальное количество и т. д.

Aspose.Cells предоставляет перечисление [**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/) для поддержки следующих функций консолидации.

- ConsolidationFunction::Average
- ConsolidationFunction::Count
- ConsolidationFunction::CountNums
- ConsolidationFunction::DistinctCount
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Product
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Sum
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Применение функции консолидации к данным полей сводной таблицы**

Следующий код применяет функцию объединения **Среднее** к первому полю данных (или значению) и функцию объединения **Уникальное количество** ко второму полю данных (или значению).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Функция консолидации Уникальное количество поддерживается только Microsoft Excel 2013.

{{% /alert %}}
