---
title: Работа с форматами отображения данных поля данных в сводной таблице на C++
linktitle: Работа с форматами отображения данных поля данных в сводной таблице
type: docs
weight: 140
url: /ru/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Узнайте, как работать с форматами отображения данных поля данных в сводной таблице с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает все форматы отображения данных DataField.

{{% /alert %}}

## **Опция отображения "Ранг по возрастанию" и "Ранг по убыванию"**

Aspose.Cells предоставляет возможность установить опцию формата отображения для полей сводной таблицы. Для этого API предоставляет свойство [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/). Для ранжирования от большего к меньшему установите свойство [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotshowvaluessetting/getcalculationtype/) в [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). Ниже приведен пример кода установки опций формата отображения.

Образцы и выходные файлы можно загрузить отсюда для тестирования образца кода:

[Исходный файл Excel](101089332.xlsx)

[Файл Excel с результатом](101089333.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load a template file
    Workbook workbook(srcDir + u"PivotTableSample.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    int pivotIndex = 0;

    // Accessing the PivotTable
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Accessing the data fields
    PivotFieldCollection pivotFields = pivotTable.GetDataFields();

    // Accessing the first data field in the data fields
    PivotField pivotField = pivotFields.Get(0);

    // Setting data display format
    pivotField.GetShowValuesSetting().SetCalculationType(PivotFieldDataDisplayFormat::RankLargestToSmallest);

    // Calculate data
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outDir + u"PivotTableDataDisplayFormatRanking_out.xlsx");

    std::cout << "PivotTable data display format ranking applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
