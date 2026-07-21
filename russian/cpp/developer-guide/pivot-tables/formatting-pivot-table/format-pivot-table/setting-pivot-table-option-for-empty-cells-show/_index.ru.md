---
title: Настройка параметра сводной таблицы  для отображения пустых ячеек с помощью C++
linktitle: Настройка параметра сводной таблицы  Показывать пустые ячейки
type: docs
weight: 40
url: /ru/cpp/setting-pivot-table-option-for-empty-cells-show/
description: Узнайте, как установить опцию "Для пустых ячеек показать" в сводных таблицах с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Вы можете установить различные параметры сводной таблицы с помощью Aspose.Cells. Один из таких параметров - "Показывать для пустых ячеек". Установив этот параметр, все пустые ячейки в сводной таблице отображаются как указанная строка.

{{% /alert %}}

## **Установка параметров сводной таблицы в Microsoft Excel**

Чтобы найти и установить этот параметр в Microsoft Excel:

1. Выберите сводную таблицу и щелкните правой кнопкой мыши.
1. Выберите **Параметры сводной таблицы**.
1. Выберите вкладку **Макет и формат**.
1. Выберите опцию **Показывать пустые ячейки** и укажите строку.

## **Установка параметра сводной таблицы с помощью Aspose.Cells**

Aspose.Cells предоставляет свойства [**PivotTable.GetDisplayNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getdisplaynullstring/) и [**PivotTable.GetNullString()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getnullstring/) для установки параметра сводной таблицы "Показывать для пустых ячеек".

```c++
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
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Get the first pivot table
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    PivotTable pt = pivotTables.Get(0);

    // Indicating if or not display the empty cell value
    pt.SetDisplayNullString(true);

    // Indicating the null string
    pt.SetNullString(u"null");

    // Calculate pivot table data
    pt.CalculateData();

    // Set refresh data on opening file to false
    pt.SetRefreshDataOnOpeningFile(false);

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Pivot table settings applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Связанные статьи

- [Форматирование сводной таблицы](/cells/ru/cpp/formatting-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
